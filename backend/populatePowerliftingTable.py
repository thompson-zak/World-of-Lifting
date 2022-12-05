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

# Currently pandas kills the process during dataframe creation
## 1. Add dType to read_csv call
## 2. If still an issue, chunk the csv processing
print('Creating dataframe from powerlifting csv...')
df = pd.read_csv('../backend/downloads/openpowerlifting.csv')
print('Dataframe created. Printing first 10 entries of open powerlifting csv...')
print(df.head(10))

print('Cleaning up downloaded and extracted files...')
os.remove('../backend/downloads/openpowerlifting.csv')
# TODO - add this back once a full download is being performed for every run of this script
#os.remove('../backend/downloads/openpowerlifting-latest.zip')
print('Downloaded and extracted files have been deleted.')
print('Weekly refresh has been completed.')
