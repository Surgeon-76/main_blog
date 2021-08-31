from fastapi import APIRouter

from models.users import Users

user_route = APIRouter()

from pydantic import BaseModel

class CreateUser(BaseModel):
    email: str
    password: str
    name: str

@user_route.post('/')
async def create(user:CreateUser):
    return await Users.objects.create(**user.dict())

@user_route.get('/')
async def get_all():
    return await Users.objects.select_related('cars').all()

@user_route.get('/{user_id}')
async def get_one(user_id:int):
    return await Users.objects.get_or_none(id=user_id)