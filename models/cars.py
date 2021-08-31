from typing import List, Optional
import ormar

from config.db_config import database, metadata
from .users import Users
from .ballons import Ballons


class Cars(ormar.Model):
    class Meta:
        tablename = 'cars'
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    modelcars: str = ormar.String(max_length=255, nullable=False)
    user: Optional[Users] = ormar.ForeignKey(Users)
    ballons: Optional[List[Ballons]] = ormar.ManyToMany(Ballons)