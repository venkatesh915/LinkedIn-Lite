from app.models.user import User
def create_user(db,user):
    db.add(user)
    db.commit
    db.refresh(user)
    return user
def get_userby_id(db,user_id):
    return db.query(user).filter(User.id==user_id).first()
def get_all_users(db):
    return db.query.all()
def get_user_by_email(db, email):
    return db.query(User).filter(User.email == email).first()
