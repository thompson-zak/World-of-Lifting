import database.dbUtils as dbUtils
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import numpy as np
from scipy import stats
import math

SQUAT_COL = 'best3squatkg'
BENCH_COL = 'best3benchkg'
DEADLIFT_COL = 'best3deadliftkg'


def analyze_powerlifting(lift_data):
    # Grab all user provided data that is relevant to powerlifting analysis
    squat = lift_data.get('squat')
    bench = lift_data.get('bench')
    deadlift = lift_data.get('deadlift')
    lift_units = lift_data.get('liftUnits')

    if lift_units == 'lbs':
        squat = convert_to_kg(squat)
        bench = convert_to_kg(bench)
        deadlift = convert_to_kg(deadlift)

    bw = lift_data.get('bodyweight')
    bw_units = lift_data.get('bodyweightUnits')
    age = lift_data.get('age')
    sex = lift_data.get('sex')
    equipped = lift_data.get('equipped')

    # Query all relevant SBD data from DB and load into dataframe
    engine = dbUtils.getDatabaseConnection()

    query_select = 'SELECT * FROM powerlifting WHERE'

    # TODO - end analysis if age class is invalid
    age_class = get_age_class(age)

    # Need to allow for age or ageClass since neither are guaranteed in dataset
    age_clause = '(age={} OR age={} OR age={})'.format(age, (age + .5), (age - .5))
    age_class_clause = "(ageClass='{}')".format(age_class)
    age_condition = '({} OR {})'.format(age_clause, age_class_clause)

    # Allow for range of 2.5kg up and down for bodyweight
    if bw_units == 'lbs':
        bw = convert_to_kg(bw)
    bw_clause = '(bodyweightKg BETWEEN {} AND {})'.format((bw - 2.5), (bw + 2.5))
    # TODO - eventually allow for BW class to include more data, however it
    # will be more imprecise. Maybe allow user to choose accuracy level?

    sex_clause = "sex='{}'".format(sex)
    equipped_clause = "equipment!='Raw'" if equipped else "equipment='Raw'"

    query_conditions = '{AGE} AND {BODYWEIGHT} AND {SEX} AND {EQUIPMENT}'.format(
        AGE=age_condition, BODYWEIGHT=bw_clause, SEX=sex_clause, EQUIPMENT=equipped_clause)
    query = '{SELECT} {CONDITION}'.format(
        SELECT=query_select, CONDITION=query_conditions)
    df = pd.read_sql(query, engine)

    # Calculate data required for plotting lift performance

    # Convert all relevant kg values into lbs if specified by user
    if lift_units == 'lbs':
        df[SQUAT_COL] *= 2.2049
        df[BENCH_COL] *= 2.2049
        df[DEADLIFT_COL] *= 2.2049
        squat = convert_to_lb(squat)
        bench = convert_to_lb(bench)
        deadlift = convert_to_lb(deadlift)

    squat_col = df[SQUAT_COL]
    bench_col = df[BENCH_COL]
    deadlift_col = df[DEADLIFT_COL]

    squat_percentile = round(
        stats.percentileofscore(
            squat_col,
            squat,
            nan_policy='omit'))
    bench_percentile = round(
        stats.percentileofscore(
            bench_col,
            bench,
            nan_policy='omit'))
    deadlift_percentile = round(
        stats.percentileofscore(
            deadlift_col,
            deadlift,
            nan_policy='omit'))

    count = df.count()

    # TODO - add X axis labels

    squat_coords, squat_highlight = get_coordinates_list(
        round(squat_col.mean(), 2), round(squat_col.std(), 2), squat)
    bench_coords, bench_highlight = get_coordinates_list(
        round(bench_col.mean(), 2), round(bench_col.std(), 2), bench)
    deadlift_coords, deadlift_highlight = get_coordinates_list(
        round(deadlift_col.mean(), 2), round(deadlift_col.std(), 2), deadlift)

    return {
        'squat': {
            'percentile': squat_percentile,
            'count': int(count[SQUAT_COL]),
            'coordinates': squat_coords,
            'highlight': squat_highlight},
        'bench': {
            'percentile': bench_percentile,
            'count': int(count[BENCH_COL]),
            'coordinates': bench_coords,
            'highlight': bench_highlight},
        'deadlift': {
            'percentile': deadlift_percentile,
            'count': int(count[DEADLIFT_COL]),
            'coordinates': deadlift_coords,
            'highlight': deadlift_highlight}}


def get_coordinates_list(mean, deviation, lift):
    x_data = np.arange(mean - (3 * deviation), mean + (3 * deviation), 1)
    y_data = stats.norm.pdf(x_data, mean, deviation)

    highlight_index = find_nearest_index(x_data, lift)
    highlight_x = x_data[highlight_index]
    highlight_y = y_data[highlight_index]

    # Naive merge, assuming lists of same length
    return [{'x': x_data[i], 'y': y_data[i]}
            for i in range(0, len(x_data))], {'x': highlight_x, 'y': highlight_y}


def find_nearest_index(array, value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(
            value - array[idx - 1]) < math.fabs(value - array[idx])):
        return idx - 1
    else:
        return idx


def convert_to_kg(weight):
    return weight / 2.2049


def convert_to_lb(weight):
    return weight * 2.2049


def get_age_class(age):
    if age >= 5 and age <= 12:
        return '5-12'
    elif age >= 13 and age <= 15:
        return '13-15'
    elif age >= 16 and age <= 17:
        return '16-17'
    elif age >= 18 and age <= 19:
        return '18-19'
    elif age >= 20 and age <= 23:
        return '20-23'
    elif age >= 24 and age <= 34:
        return '24-34'
    elif age >= 35 and age <= 39:
        return '35-39'
    elif age >= 40 and age <= 44:
        return '40-44'
    elif age >= 45 and age <= 49:
        return '45-49'
    elif age >= 50 and age <= 54:
        return '50-54'
    elif age >= 55 and age <= 59:
        return '55-59'
    elif age >= 60 and age <= 64:
        return '60-64'
    elif age >= 65 and age <= 69:
        return '65-69'
    elif age >= 70 and age <= 74:
        return '70-74'
    elif age >= 75 and age <= 79:
        return '75-79'
    elif age >= 80:
        return '80-999'
    else:
        return '0'
