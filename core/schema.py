from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .config import Base, engine

class UserTable(Base):

    __tablename__ = "User"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)
    token = Column(String(100), nullable=False)


class PapersTable(Base):
    __tablename__ = "Paper"

    id = Column(Integer,autoincrement=True, primary_key=True)
    file = Column(String(30),nullable=False)
    year = Column(String(4),nullable=False)
    sem = Column(Integer,nullable=False)
    dept = Column(String(20),nullable=False)
    sub = Column(String(30), nullable=True)

Base.metadata.create_all(engine)
