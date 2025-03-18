from pydantic import BaseModel
from fastapi import HTTPException
import re

class User(BaseModel):
    login: str
    password: str

def register_check(username: str, password: str, users: dict):
    """
    Функция для проверки вводимых данных для регистрации пользователя.
    Возвращаемое значение:
    True, если вводные данные прошли все проверки.
    """

    # Убираем лишние пробелы
    username = username.strip()  
    password = password.strip()
    
    LOGIN_REGEX = r'^[\wа-яА-Я][\wа-яА-Я._-]{4,}$'
    if not re.match(LOGIN_REGEX, username):
        raise HTTPException(
            status_code=400,
            detail="Логин должен начинаться с буквы и иметь только буквы, цифры, подчеркивания, точки или тире."
        )

    # Проверка на наличие пользователя
    for id in users:
        if username == users[id]:
            raise HTTPException(status_code=409, detail='Данный пользователь уже зарегистрирован!')
        
    return True