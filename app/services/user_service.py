from app.dao.user_dao import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_token


def register(db, u, e, p):
    if get_user_by_email(db, e):
        raise Exception("Email exists")

    user = create_user(db, u, e, hash_password(p))
    return {"user_id": user.id}


def login(db, e, p):
    user = get_user_by_email(db, e)

    if not user or not verify_password(p, user.password):
        raise Exception("Invalid credentials")

    return {"token": create_token(user.id)}
