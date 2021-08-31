from fastapi import APIRouter

from models.cars import Cars




cars_route = APIRouter()


@cars_route.post('/')
async def create(user:Cars):
    return await user.save()

@cars_route.get('/')
async def get_all():
    return await Cars.objects.all()

@cars_route.post('/{cars_id}')
async def get_one(cars_id:int):
    return await Cars.objects.get_or_none(id=cars_id)



