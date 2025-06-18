from fastapi import APIRouter
from src.api.dtos.users import UserRegistration

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("register")
async def register(body:UserRegistration):
        return {'status':'ok'}