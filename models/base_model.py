from datetime import datetime
from typing import Optional, Dict
from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.orm import Session
from db import Base


class BaseModel(Base):
    __abstract__ = True
    """
    Adds 'id', 'is_active', `created` and `updated` columns to derived models.
    """
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated = Column(DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)


class BaseQueries:
    model: Optional = None

    @classmethod
    def get_record_with_id(cls, model_id: str, db: Session):
        return db.query(cls.model).filter(cls.model.id == model_id).first()

    @classmethod
    def get_record_with_(cls, db: Session, **kwargs):
        return db.query(cls.model).filter_by(**kwargs).first()

    @classmethod
    def get_all_record_with_(cls, db: Session, **kwargs):
        return db.query(cls.model).filter_by(**kwargs).all()

    @classmethod
    def get_all_records(cls, db: Session, limit=100, skip=0):
        return db.query(cls.model).offset(skip).limit(limit).all()

    @classmethod
    def create_record(cls, values: Dict, db: Session):
        obj = cls.model(**values)
        db.add(obj)
        db.flush()
        return obj
