from app.repositories.follow_repository import FollowRepository
from app.schemas.follow import FollowCreate

follow_repository = FollowRepository()




def follow_user(db, follower_id: int, following_id: int):
    follow = FollowCreate(
        follower_id=follower_id,
        following_id=following_id
    )
    return follow_repository.create_follow(db, follow)
def unfollow_user(db, follower_id: int, following_id: int):
    return follow_repository.delete_follow(
        db,
        follower_id,
        following_id
    )



def get_followers(db, user_id: int):
    
    return follow_repository.get_followers(db, user_id)



def get_following(db, user_id: int):
    return follow_repository.get_following(db, user_id)