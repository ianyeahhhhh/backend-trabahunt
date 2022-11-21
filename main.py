from fastapi import FastAPI
import models
import schemas
from database import engine

# UPLOAD FILE
from fastapi import File, UploadFile
import secrets
from fastapi.staticfiles import StaticFiles
from fastapi import Depends
from database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

from router import authentication
from router import user_account_router
from router import candidate_profile_router, candidate_education_detail_router, candidate_experience_detail_router, candidate_resume_router
from router import company_profile_router, company_addition_info_router, company_subscription_router, payment_router
from router import admin_profile_router, admin_login_router
from router import session_info_router
from router import job_post_router, job_additional_info_router, job_location_router, job_application_router
from router import interview_info_router, employee_info_router, job_offer_router
from router import request_form_router

from jose import jwt, JWTError
from datetime import datetime, timedelta

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='TrabaHunt'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File Upload
# static file setup config
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.post('/file_upload')
async def file_upload(file: UploadFile = File(...), db: Session = Depends(get_db), ):
    flag = 0
    FILEPATH = './static/files/'
    filename = file.filename
    extension = filename.split('.')[1]

    if extension not in ['pdf']:
        return {
            'status': 'error',
            'detail': 'File extension not allowed'
        }

    token_name = secrets.token_hex(10)+'.'+extension
    generated_name = FILEPATH + token_name
    file_content = await file.read()

    with open(generated_name, 'wb') as file:
        file.write(file_content)
        flag = 1

    file.close()
    file_url = 'localhost:8000' + generated_name[1:]

    column = models.Files(
        file_name=generated_name,
        file_content=file_content
    )
    db.add(column)
    db.commit()
    
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'File UPLOADED.',
        'data': {
            'file_url': file_url,
            'flag': flag
        }
    }


# TOKEN.PY
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
# TOKEN.PY


# Include routers
app.include_router(admin_login_router.router)
app.include_router(admin_profile_router.router)
app.include_router(session_info_router.router)
app.include_router(authentication.router)
app.include_router(user_account_router.router)
app.include_router(candidate_profile_router.router)
app.include_router(candidate_education_detail_router.router)
app.include_router(candidate_resume_router.router)
app.include_router(candidate_experience_detail_router.router)
app.include_router(company_profile_router.router)
app.include_router(company_addition_info_router.router)
app.include_router(company_subscription_router.router)
app.include_router(job_post_router.router)
app.include_router(job_additional_info_router.router)
app.include_router(job_location_router.router)
app.include_router(job_application_router.router)
app.include_router(job_offer_router.router)
app.include_router(payment_router.router)
app.include_router(interview_info_router.router)
app.include_router(employee_info_router.router)
app.include_router(request_form_router.router)
