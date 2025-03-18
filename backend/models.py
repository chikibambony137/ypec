from sqlalchemy import Column, BIGINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase
from passlib.context import CryptContext

# Создание контекста для хеширования паролей с использованием схемы bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(BIGINT, primary_key=True, index=True)
    login = Column(VARCHAR, unique=True)
    password = Column(VARCHAR)

    # Метод для установки пароля пользователя
    def set_password(self, password: str):
        # Хеширование пароля перед сохранением
        self.password = pwd_context.hash(password)

    # Метод для проверки введенного пользователем пароля
    def verify_password(self, password: str):
        # Проверка совпадения хеша пароля
        return pwd_context.verify(password, self.password)
