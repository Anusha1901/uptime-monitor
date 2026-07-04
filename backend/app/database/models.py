from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database.database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    health_checks = relationship(
        "HealthCheck",
        back_populates="url",
        cascade="all, delete"
    )


class HealthCheck(Base):
    __tablename__ = "health_checks"

    id = Column(Integer, primary_key=True, index=True)

    url_id = Column(
        Integer,
        ForeignKey("urls.id"),
        nullable=False
    )

    status_code = Column(Integer, nullable=True)

    response_time = Column(
        Float,
        nullable=True
    )

    is_up = Column(Boolean, default=False)

    error_message = Column(String, nullable=True)

    checked_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    url = relationship(
        "URL",
        back_populates="health_checks"
    )