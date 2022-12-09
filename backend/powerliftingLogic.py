import databaseUtilities
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd


def analyze_powerlifting(lift_data):

	#Grab all user provided data that is relevant to powerlifting analysis
	squat = lift_data.get('squat')
    bench = lift_data.get('bench')
    deadlift = lift_data.get('deadlift')
    lift_units = lift_data.get('liftUnits')

    bodyweight = lift_data.get('bodyweight')
    bodyweight_units = lift_data.get('bodyweightUnits')
    age = lift_data.get('age')

    #Query all relevant SBD data from DB and load into dataframe
    engine = databaseUtilities.getDatabaseConnection()
    sql_query = 'SELECT * FROM powerlifting WHERE '
    df = engine.connect().execute(text())
