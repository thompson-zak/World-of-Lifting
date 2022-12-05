import zipfile
import pandas as pd
import re
import os

# TODO - full download of the ZIP file from open powerlifting
# Leave this until nearly done so as to avoid unnecessary downloads

zf = zipfile.ZipFile('../backend/downloads/openpowerlifting-latest.zip')
for info in zf.infolist():
	if re.match('openpowerlifting.*/openpowerlifting.*\.csv', info.filename):
		info.filename = 'openpowerlifting.csv'
		print('Extracting powerlifting csv to downloads folder...')
		zf.extract(info, '../backend/downloads/')
		print('Extraction complete')

print('Ingesting powerlifting data to DB...')
requiredColumns=['Sex','Equipment','Age','AgeClass','Best3SquatKg','Best3BenchKg','Best3DeadliftKg','Place','Federation','Date']
dateColumns=['Date']
dataTypes={'Sex': 'string', 'Age': float, 'AgeClass': 'string', 'Best3SquatKg': float, 'Best3BenchKg': float, 'Best3DeadliftKg': float, 'Place': 'string', 'Federation': 'string'}
# TODO - increase chunk size
with pd.read_csv('../backend/downloads/openpowerlifting.csv', chunksize=100, usecols=requiredColumns, dtype=dataTypes, parse_dates=dateColumns) as reader:
	for chunk in reader:
		# TODO - insert data into table here
		print(chunk)
		# TODO - remove this break once done
		break
print('Ingestion complete.')

print('Cleaning up downloaded and extracted files...')
os.remove('../backend/downloads/openpowerlifting.csv')
# TODO - add this back once a full download is being performed for every run of this script
#os.remove('../backend/downloads/openpowerlifting-latest.zip')
print('Downloaded and extracted files have been deleted.')
print('Weekly refresh has been completed.')
