import yaml
from sqlalchemy import create_engine

def getDatabaseConnection() :
	config = yaml.safe_load(open("./config.yml"))
	return create_engine(config['database']['connection']['string'])
