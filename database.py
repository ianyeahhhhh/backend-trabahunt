from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# HEROKU
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://ldyhafsrprlffy:9b7f9b8892d2192e943f083b25260b231d492ded7e9e057fd152043b96b7a176@ec2-3-209-39-2.compute-1.amazonaws.com:5432/d3u983e2hmjmne"

# LOCAL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/trabahunt"

# RENDER
# SQLALCHEMY_DATABASE_URL = "postgresql://ian:7lP5zqrWKgEYcXGu2gwahH23X2yMerSv@dpg-ce2o1n14reb2j5ilsdj0-a.oregon-postgres.render.com/trabahunt_fur9"


# FORMAT
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

