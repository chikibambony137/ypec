from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models import User
import schemas

from fastapi.security import OAuth2PasswordRequestForm
from jwt import create_access_token

router = APIRouter()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/register")
async def register(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = User(login=form_data.username, password=form_data.password)
    users = dict(db.query(User.id, User.login))

    schemas.register_check(form_data.username, form_data.password, users)
    user.set_password(form_data.password)

    db.add(user)
    db.commit()
    return {"msg": "Пользователь зарегистрирован!"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(User).filter(User.login == form_data.username).first()

    if not user or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.login})
    return {"access_token": access_token, "token_type": "bearer", "id": user.id}
