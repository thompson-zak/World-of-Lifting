import zipfile
import pandas as pd
import re
import os
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import time
import urllib.request

print('Starting download of open powerlifting data')
startDownloadTime = time.time()
urllib.request.urlretrieve('https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip', '../backend/downloads/openpowerlifting-latest.zip')
print('Completed download of open powerlifting data in {} seconds'.format(round(time.time() - startDownloadTime, 2)))

zf = zipfile.ZipFile('../backend/downloads/openpowerlifting-latest.zip')
for info in zf.infolist():
	if re.match('openpowerlifting.*/openpowerlifting.*\.csv', info.filename):
		info.filename = 'openpowerlifting.csv'
		print('Extracting powerlifting csv to downloads folder...')
		zf.extract(info, '../backend/downloads/')
		print('Extraction complete')

print('Ingesting powerlifting data to DB...')
requiredColumns=['Sex','Equipment','Age','AgeClass','BodyweightKg','WeightClassKg','Best3SquatKg','Best3BenchKg','Best3DeadliftKg','Place','Federation','Date']
dateColumns=['Date']
dataTypes={'Sex': 'string', 'Age': float, 'AgeClass': 'string', 'Best3SquatKg': float, 'Best3BenchKg': float, 'Best3DeadliftKg': float, 'Place': 'string', 'Federation': 'string'}

engine = dbUtils.getDatabaseConnection()
startIngestionTime = time.time()

try:
	engine.connect().execution_options(autocommit=True).execute(text('TRUNCATE TABLE powerlifting'))
	with pd.read_csv('../backend/downloads/openpowerlifting.csv', chunksize=50000, usecols=requiredColumns, dtype=dataTypes, parse_dates=dateColumns) as reader:
		for chunk in reader:
			chunk.columns = [colName.lower() for colName in requiredColumns]
			chunk.to_sql('powerlifting', engine, if_exists='append', index=False)
	print('Ingestion complete. Finished in {} seconds'.format(round(time.time() - startIngestionTime, 2)))
except Exception as e:
	print(e)
	print('There was an issue. Ingestion did not complete successfully. Finished in {} seconds'.format(round(time.time() - startIngestionTime, 2)))

print('Cleaning up downloaded and extracted files...')
os.remove('../backend/downloads/openpowerlifting.csv')
os.remove('../backend/downloads/openpowerlifting-latest.zip')
print('Downloaded and extracted files have been deleted.')
print('Weekly refresh has been completed.')
