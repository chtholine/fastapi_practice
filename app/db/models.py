from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from app.db.database import Base


class UserData(Base):
    __tablename__ = "user_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    user_firstname: Mapped[str] = mapped_column(nullable=True)
    user_lastname: Mapped[str] = mapped_column(nullable=True)
    user_status: Mapped[str] = mapped_column(nullable=True)
    user_city: Mapped[str] = mapped_column(nullable=True)
    user_phone: Mapped[str] = mapped_column(nullable=True)
    user_links: Mapped[str] = mapped_column(nullable=True)
    user_avatar: Mapped[str] = mapped_column(nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=True)
    is_superuser: Mapped[bool] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

