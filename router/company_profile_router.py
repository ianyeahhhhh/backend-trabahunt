from datetime import datetime
from database import get_db

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Company_Profile
from schemas import Company_Profile_Form, Login_Form
from oauth2 import get_current_user

router = APIRouter(
    prefix='/company_profile',
    tags=['Company_Profile']
)


# get all active
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Company_Profile).all()

    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Profile).filter(
        Company_Profile.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Company_Profile_Form, db: Session = Depends(get_db)):
    column = Company_Profile(
        user_account_id=req.user_account_id,
        company_name=req.company_name,
        profile_description=req.profile_description,
        establishment_date=req.establishment_date,
        company_website_url=req.company_website_url,
        company_logo=req.company_logo,
        review_status=req.review_status
    )
    db.add(column)
    db.commit()

    column.created_by = column.company_id
    column.updated_by = column.company_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Employer/Company Profile Created.',
        'data': {
            'company_id': column.company_id,
            'company_name': column.company_name,
            'profile_description': column.profile_description,
            'establishment_date': column.establishment_date,
            'company_website_url': column.company_website_url,
            'company_logo': column.company_logo,
            'user_account_id': column.user_account_id,
            'review_status': column.review_status
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Company_Profile_Form, db: Session = Depends(get_db)
                 # , current_user: Login_Form = Depends(get_current_user)
                 ):
    column = db.query(Company_Profile).filter(
        Company_Profile.user_account_id == id).first()

    if column:
        column.company_name = req.company_name
        column.profile_description = req.profile_description
        column.establishment_date = req.establishment_date
        column.company_website_url = req.company_website_url
        column.company_logo = req.company_logo
        column.user_account_id = req.user_account_id
        column.updated_at = datetime.now()
        column.review_status = req.review_status

        db.commit()
        return {
            'msg': 'Employer/Company info updated.',
            'company_name': column.company_name,
            'profile_description': column.profile_description,
            'establishment_date': column.establishment_date,
            'company_website_url': column.company_website_url,
            'company_logo': column.company_logo,
            'review_status': column.review_status
        }
    return {
        'msg': 'Employer/Company cannot be found.'
    }


# deactivate
@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    column = db.query(Company_Profile).filter(
        Company_Profile.company_id == id).first()

    if column:
        column.review_status = 'Inactive'

        db.commit()
        return {
            'msg': 'Employer/Company deactivated.',
            'company_name': column.company_name
        }
    return {
        'msg': 'Employer/Company cannot be found.'
    }


@router.put('/grantaccess/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Company_Profile).filter(
        Company_Profile.user_account_id == id).first()

    if column:
        column.review_status = 'Active'
        db.commit()
        return {
            'msg': 'Company Activated'
        }

