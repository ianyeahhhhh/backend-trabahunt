from fastapi import FastAPI
import models
import schemas
from database import engine

from router import authentication, candidate_experience_detail_router
from router import user_account_router
from router import candidate_profile_router, candidate_education_detail_router, candidate_resume_router
from router import company_profile_router, company_addition_info_router, company_subscription_router, payment_router
from router import admin_profile_router, admin_login_router
from router import session_info_router
from router import job_post_router, job_additional_info_router, job_location_router, job_application_router
from router import interview_info_router, employee_info_router, job_offer_router
from router import request_form_router, for_HR_router, aws_files_router, company_legal_document_router

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
app.include_router(aws_files_router.router)
app.include_router(for_HR_router.router)
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
app.include_router(company_legal_document_router.router)
app.include_router(job_post_router.router)
app.include_router(job_additional_info_router.router)
app.include_router(job_location_router.router)
app.include_router(job_application_router.router)
app.include_router(job_offer_router.router)
app.include_router(payment_router.router)
app.include_router(interview_info_router.router)
app.include_router(employee_info_router.router)
app.include_router(request_form_router.router)
