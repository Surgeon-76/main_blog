import ormar 
from config.db_config import database, metadata

class Users(ormar.Model):
    class Meta:
        tablename = 'users_car'
        database = database
        metadata = metadata


    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=255, nullable=False)
    password: str = ormar.String(max_length=255)
    name: str = ormar.String(max_length=500)