from fastapi import FastAPI


from config.db_config import engine, metadata, database
from models.ballons import *
from models.cars import *
from models.users import *



app = FastAPI()


metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


