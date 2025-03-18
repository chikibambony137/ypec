from datetime import datetime, timedelta
from jose import JWTError, jwt
from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict) -> str:
    """
    Функция для создания JWT-токена доступа.
    Возвращаемое значение:
    str: Созданный JWT-токен.
    """
    # Копируем данные, чтобы избежать изменения оригинального словаря
    to_encode = data.copy()
    # Устанавливаем время истечения срока действия токена
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Добавляем время истечения срока действия в данные для кодирования
    to_encode.update({"exp": expire})
    # Кодируем данные в JWT-токен с использованием секретного ключа и алгоритма шифрования
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # Возвращаем созданный токен
    return encoded_jwt

def verify_token(token: str):
    """
    Функция для проверки и расшифровки JWT-токена.

    Аргументы:
    token (str): Токен, который необходимо проверить.

    Возвращаемое значение:
    dict: Расшифрованные данные из токена, если проверка прошла успешно, иначе None.
    """
    try:
        # Декодируем токен с использованием секретного ключа и алгоритма шифрования
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Возвращаем распакованные данные из токена
        return payload
    except JWTError:
        # Если возникает ошибка при проверке токена, возвращаем None
        return None
    
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Функция для проверки токена пользователя.
    Возвращает True, если токен прошел проверку.
    """
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload