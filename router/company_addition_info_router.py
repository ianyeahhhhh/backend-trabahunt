from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

from models import Company_Addition_Info
from schemas import Company_Addition_Info_Form, Login_Form
from oauth2 import get_current_user


router = APIRouter(
    prefix='/company_addition_info',
    tags=['Company_Addition_Info']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Company_Addition_Info).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Addition_Info).filter(Company_Addition_Info.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Company_Addition_Info_Form, db: Session = Depends(get_db)):
    column = Company_Addition_Info(
        user_account_id=req.user_account_id,
        registration_number=req.registration_number,
        country=req.country,
        region=req.region,
        zip_code=req.zip_code,
        city=req.city,
        company_contact_number=req.company_contact_number
    )
    db.add(column)
    db.commit()

    column.created_by = column.company_addition_info_id
    column.updated_by = column.company_addition_info_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Company Addition Info created.',
        'data': {
            'company_addition_info_id': column.company_addition_info_id,
            'registration_number': column.registration_number,
            'country': column.country,
            'region': column.region,
            'zip_code': column.zip_code,
            'city': column.city,
            'company_contact_number': column.company_contact_number,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Company_Addition_Info_Form, db: Session = Depends(get_db)
                # , current_user: Login_Form = Depends(get_current_user)
                ):
    column = db.query(Company_Addition_Info).filter(
        Company_Addition_Info.user_account_id == id).first()

    if column:
        column.registration_number = req.registration_number
        column.country = req.country
        column.region = req.region
        column.zip_code = req.zip_code
        column.city = req.city
        column.company_contact_number = req.company_contact_number
        column.user_account_id = req.user_account_id
        column.updated_at = datetime.now()

        db.commit()
        return {
            'msg': 'Company Addition Info updated.',
            'data': {
                'registration_number': column.registration_number,
                'country': column.country,
                'region': column.region,
                'zip_code': column.zip_code,
                'city': column.city,
                'company_contact_number': column.company_contact_number,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'Company Addition Info ID does not exist.'
    }
