from fastapi import APIRouter
from src.api.dtos.users import UserRegistration,UserLogin
from src.datalayer.models.users import UserModel
from src.api.exceptions.users import login_wrong_exception,email_already_registered_exception

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register(body:UserRegistration):

        email_exist= await UserModel.get(email=body.email)
        if email_exist:
                raise email_already_registered_exception()

        user = await UserModel.create (
                name = body.name,
                email = body.email,
                password = body.password,
        )
        return {'created':user}

@router.post("/login")
async def login(body:UserLogin):

        user=None
        try:
              user = await UserModel.get(email=body.email)
        except Exception:
                raise login_wrong_exception()

        if user.password != body.password:
                raise login_wrong_exception()

        return user

