from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://ttagninobdspjj:eb6c2712eb3bee9778e212ea59afd229e2cb00e8ef68643026650af98d489d1b@ec2-52-23-131-232.compute-1.amazonaws.com:5432/d85k517loivd29"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/trabahunt"

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost/trabahunt"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, max_overflow=-1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

