import ormar


from config.db_config import database, metadata


class Ballons(ormar.Model):
    class Meta:
        tablename = 'ballons'
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    typeballons: str = ormar.String(max_length=255, nullable=False)
    