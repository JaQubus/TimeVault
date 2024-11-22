from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import uuid
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, DateTime
from pydantic import BaseModel, EmailStr
import datetime

from sqlalchemy_utils import UUIDType

Base = declarative_base()

engine = create_async_engine('sqlite+aiosqlite:///sqlalchemy.sqlite', echo=False)
SessionLocal = async_sessionmaker(engine)


def generate_uuid():
    return int(uuid.uuid4())

async def get_db() -> AsyncSession:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await SessionLocal().close()
    return SessionLocal()

# async def get_db() -> AsyncSession:
#     async with SessionLocal() as session:  # Correctly using session
#         yield session  # FastAPI will handle session closure automatically

class UserCreate(BaseModel):
    user_id: uuid.UUID
    email: EmailStr
    username: str
    password: str

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column("user_id", UUIDType(binary=False), primary_key=True, index=True)

    email: Mapped[String] = mapped_column("email", String, nullable=False, unique=True)
    username: Mapped[String] = mapped_column("username", String, nullable=False)
    password: Mapped[String] = mapped_column("password", String, nullable=False)

    def __init__(self, user_id, email, username, password):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.password = password

    def dict(self):
        return {
            "id": self.user_id,
            "email": self.email,
            "name": self.username,
        }


class EmailRequestCreateSchema(BaseModel):
    user_id: uuid.UUID | None = None
    sender: EmailStr
    receiver: EmailStr
    date_to_send: datetime.datetime
    message: str


class EmailRequestCreate(Base):
    __tablename__ = "emails_sent"

    user_id: Mapped[uuid.UUID] = mapped_column("user_id", UUIDType(binary=False), primary_key=True, index=True)
    sender: Mapped[String] = mapped_column("sender", String, nullable=False, unique=True)
    receiver: Mapped[String] = mapped_column("receiver", String, nullable=False)
    date_to_send: Mapped[datetime.datetime] = mapped_column("date_to_send", DateTime, nullable=False)
    message: Mapped[String] = mapped_column("message", String, nullable=False)

    def __init__(self, user_id, sender, receiver, date_to_send, message):
        self.user_id = user_id
        self.sender = sender
        self.receiver = receiver
        self.date_to_send = date_to_send
        self.message = message

    def dict(self):
        return {
            "id": self.user_id,
            "email": self.sender,
            "name": self.receiver,
            "date_to_send": self.date_to_send,
            "message": self.message,
        }


