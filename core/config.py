from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Url = "mysql+pymysql://root@localhost:3306/sand"
# Url = "postgresql://peerview_user:gjxBgtimqUOxy19TAan4sPWcTooqQVaQ@dpg-cmp6040l5elc73fn1170-a.oregon-postgres.render.com/peerview"

engine = create_engine(url=Url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("Connection succesfull !")
Base = declarative_base()

def getDb():
    try:
        return session()
    except Exception as  er:
        session().close()
        return {"error":"Connection failed to database !"}