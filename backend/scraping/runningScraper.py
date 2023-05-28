import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# All states with a non-zero amount of race entries
states_list = [
				"CA", "CT", "DC", "FL", 
				"MA", "MD", "NC", "ND", 
				"NH", "NJ", "NY", "RI", 
				"VA", "VT", "WA", "WI", 
			]

valid_events = [
				"5 KM",
				"10 KM"
			]

def scrape_race_wire():
	single_result_url = "https://my.racewire.com/results/"

	event_ids = {
					"5 KM": [],
					"10 KM": []
				}

	start_time = time.time()

    # Use RaceWire api to retrieve all race ids that match the race lengths care about
	for state in states_list:
		# Use 2022 for increased results - need to make calls parallel in order to increase range of years queried
		state_results = requests.get("https://api.racewire.com/resultslist/{}/2022".format(state)).json().get("Results")
		for result in state_results:
			race_events = result.get("RaceEvents")
			if len(race_events) > 0:
				race_type = race_events[0].get("Title")
				if(race_type in valid_events):
					race_id = result.get("RaceId")
					event_ids.get(race_type).append(race_id)

	print("All valid race IDs fetched in {} seconds".format(time.time() - start_time))
	print(event_ids)

	# Use race ids to fetch results pages and scrape data from them
	#page = requests.get(URL)
	#soup = BeautifulSoup(page.content, "html.parser")
	#tables = soup.findAll("table", class_="table is-striped is-fullwidth is-narrow-mobile")
