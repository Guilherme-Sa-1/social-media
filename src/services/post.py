from src.datalayer.models.users import UserModel
from src.datalayer.models.post import PostModel, PostLikeModel, PostCommentModel
from tortoise.exceptions import DoesNotExist
from src.api.exceptions.post import post_notfound

class PostService:

    def __init__(self):
        pass

    
    async def create_post(self, user: UserModel, message: str):
        new_post = await PostModel.create(
            user = user,
            message = message,
        )
        return new_post
    

    async def get_post_comments(self, post_id: int):
        return await PostCommentModel.filter(post_id = post_id).order_by('-created_at')

    async def get_all_posts(self):
        return await PostModel.all().order_by('-created_at')
        
    async def get_user_posts(self, user_id: int):
        return await PostModel.filter(user_id=user_id)