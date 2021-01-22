from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from app import app, db, ma, SQLALCHEMY_DATABASE_URI

Engine = create_engine(SQLALCHEMY_DATABASE_URI, encoding="utf-8", echo=False)


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())


class Status(BaseModel):
    __tablename__ = "status"
    __table_args__ = {"extend_existing": True}
    person = Column(Integer)
    umbrella = Column(Integer)
    capture = Column(String(100))
    updated = Column(DateTime, unique=True)


class StatusSchema(ma.Schema):
    class Meta:
        fields = ("id", "person", "umbrella","updated")


status_schema = StatusSchema(many=True)
