import databases
import sqlalchemy
#import sqlalchemy
#from sqlalchemy import MetaData, engine
#from databases import *
#import sqlalchemy

user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'test_db'

database = databases.Database(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")
