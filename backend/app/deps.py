from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import database, models
from .utils import auth as auth_utils
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    yield from database.get_db()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = auth_utils.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid auth token")
    email = payload.get("sub")
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user