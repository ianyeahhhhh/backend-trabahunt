from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# LOCAL
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/trabahunt-new1"

# RENDER
SQLALCHEMY_DATABASE_URL = "postgresql://ian:nq0Ngv9rA6fhA1UzWAGhm0QbUmxQDDOo@dpg-cfnivqta499f28bvpo10-a.singapore-postgres.render.com/trabahunt_7q49"

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

