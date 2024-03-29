import zipfile
import pandas as pd
import re
import os
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import time
import urllib.request
import database.dbUtils as dbUtils

def init_pl():
	print('Starting download of open powerlifting data...')
	startDownloadTime = time.time()
	urllib.request.urlretrieve('https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip', './openpowerlifting-latest.zip')
	print('Completed download of open powerlifting data in {} seconds'.format(round(time.time() - startDownloadTime, 2)))

	zf = zipfile.ZipFile('./openpowerlifting-latest.zip')
	for info in zf.infolist():
		if re.match('openpowerlifting.*/openpowerlifting.*\.csv', info.filename):
			info.filename = 'openpowerlifting.csv'
			print('Extracting powerlifting csv...')
			zf.extract(info, './')
			print('Extraction complete')

	print('Ingesting powerlifting data to DB...')
	requiredColumns=['Sex','Equipment','Age','AgeClass','BodyweightKg','WeightClassKg','Best3SquatKg','Best3BenchKg','Best3DeadliftKg','Place','Federation','Date']
	dateColumns=['Date']
	dataTypes={'Sex': 'string', 'Age': float, 'AgeClass': 'string', 'Best3SquatKg': float, 'Best3BenchKg': float, 'Best3DeadliftKg': float, 'Place': 'string', 'Federation': 'string'}

	engine = dbUtils.getDatabaseConnection()
	startIngestionTime = time.time()

	try:
		engine.connect().execution_options(autocommit=True).execute(text('TRUNCATE TABLE powerlifting'))
		with pd.read_csv('./openpowerlifting.csv', chunksize=50000, usecols=requiredColumns, dtype=dataTypes, parse_dates=dateColumns) as reader:
			for chunk in reader:
				chunk.columns = [colName.lower() for colName in requiredColumns]
				chunk.to_sql('powerlifting', engine, if_exists='append', index=False)
		print('Ingestion complete. Finished in {} seconds'.format(round(time.time() - startIngestionTime, 2)))
	except Exception as e:
		print(e)
		errorMsg = 'There was an issue. Ingestion did not complete successfully. Finished in {} seconds'.format(round(time.time() - startIngestionTime, 2))
		print(errorMsg)
		return { 'success': bool(0), 'errorMessage': errorMsg }

	print('Cleaning up downloaded and extracted files...')
	os.remove('./openpowerlifting.csv')
	os.remove('./openpowerlifting-latest.zip')
	print('Downloaded and extracted files have been deleted.')
	print('Table refresh completed.')
	return {'success': bool(1), 'errorMessage': ''}