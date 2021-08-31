from fastapi import FastAPI


from config.db_config import engine, metadata, database
from models.ballons import *
from models.cars import *
from models.users import *
from routes import users, cars, ballons


app = FastAPI()


metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(
    users.user_route,
    prefix='/users',
    tags=['Корытодержатели'],
)

app.include_router(
    cars.cars_route,
    prefix='/cars',
    tags=['Сами КорытА'],
)

app.include_router(
    ballons.ballons_route,
    prefix='/ballons',
    tags=['Тапки'],
)
