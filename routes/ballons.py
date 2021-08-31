from fastapi import APIRouter

from models.ballons import Ballons

ballons_route = APIRouter()


@ballons_route.post('/')
async def create(user:Ballons):
    return await user.save()

@ballons_route.get('/')
async def get_all():
    return await Ballons.objects.all()

@ballons_route.get('/{Ballons_id}')
async def get_one(Ballons_id:int):
    return await Ballons.objects.get_or_none(id=Ballons_id)

    