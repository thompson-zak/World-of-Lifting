import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#import database.dbUtils as dbUtils

# All states with a non-zero amount of race entries
states_list = [
				'CA', 'CT', 'DC', 'FL', 
				'MA', 'MD', 'NC', 'ND', 
				'NH', 'NJ', 'NY', 'RI', 
				'VA', 'VT', 'WA', 'WI', 
			]


valid_events = [
				'5 KM',
				'10 KM'
			]


def scrape_race_wire():
	event_ids = get_race_wire_event_ids()	

	engine = dbUtils.getDatabaseConnection()
	query = 'SELECT DISTINCT SOURCEID FROM RUNNING'
	ignorable_events = pd.read_sql(query, engine)
	# Get ids that are not already in the database
	events_to_ingest = set(event_ids.get('5 KM')) ^ set(ignorable_events)

	# Use race ids to fetch results pages and scrape data from them (only 5k for now due to limited 10k entries)
	# for event_id in events_to_ingest:
		# There is a case where the initial page links to multiple races, add support this later. For now, ignore and move on
		
		

def insert_race_wire_event():
	columns = [
		'Sex',
		'Age',
		'Event',
		'FinishTime',
		'DataSource',
		'SourceId'
	]

	df = pd.DataFrame(columns = columns)

	cdm = ChromeDriverManager().install()

	chrome_options = Options()  
	chrome_options.add_argument("--headless")

	driver = webdriver.Chrome(cdm, options=chrome_options)

	driver.get('https://my.racewire.com/results/{}'.format(37454))
	html = driver.page_source

	soup = BeautifulSoup(html, 'html.parser')
	tables = soup.find_all('table', id='grid')

	if len(tables) > 0:
		table_body = tables[0].find('tbody')
		rows = table_body.find_all('tr')
		for row in rows:
		    cols = row.find_all('td')
		    cols = [col.text for col in cols]
		    athlete_details = cols[2].split(' | ')
		    age = athlete_details[0]
		    sex = athlete_details[1]
		    finish_time = cols[3]
		    new_row = {
		    	'Sex': sex, 
		    	'Age': age, 
		    	'Event': '5 KM', 
		    	'FinishTime': finish_time, 
		    	'DataSource': "RaceWire", 
		    	'SourceId': 37454
		    }
		    df.loc[len(df.index)] = new_row

	print(df)

	# Insert df into DB here


def get_race_wire_event_ids():
	event_ids = {
					'5 KM': [],
					'10 KM': []
				}

	start_time = time.time()

	# Use RaceWire api to retrieve all race ids that match the race lengths care about
	for state in states_list:
		# Use 2022 for increased results - need to make calls parallel in order to increase range of years queried
		state_results = requests.get('https://api.racewire.com/resultslist/{}/2022'.format(state)).json().get('Results')
		for result in state_results:
			race_events = result.get('RaceEvents')
			if len(race_events) > 0:
				race_type = race_events[0].get('Title')
				if(race_type in valid_events):
					race_id = result.get('RaceId')
					event_ids.get(race_type).append(race_id)

	print('All valid race IDs fetched in {} seconds'.format(time.time() - start_time))
	print(event_ids)

	return event_ids