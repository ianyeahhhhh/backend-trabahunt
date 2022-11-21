from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Company_Subscription
from oauth2 import get_current_user
from schemas import Login_Form, Company_Subscription_Form

router = APIRouter(
    prefix='/company_subscription',
    tags=['Company_Subscription']
)


# get all active
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Company_Subscription).filter(
        Company_Subscription.subscription_status == 'Active').all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Subscription).filter(
        Company_Subscription.user_account_id == id).first()
    return data


# get all basic
@router.get('/all_basic/{id}')
async def get_all_basic(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Subscription).filter(
        Company_Subscription.subscription_type_code == id).all()
    return data


# get all branded
@router.get('/all_branded/{id}')
async def get_all_branded(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Subscription).filter(
        Company_Subscription.subscription_type_code == id).all()
    return data


# post or create
@router.post('/')
async def create(req: Company_Subscription_Form, db: Session = Depends(get_db)):
    column = Company_Subscription(
        subscription_date=req.subscription_date,
        expiry_date=req.expiry_date,
        package_quantity=req.package_quantity,
        subscription_status=req.subscription_status,
        subscription_type_code=req.subscription_type_code,
        subscription_type=req.subscription_type,
        company_id=req.company_id,
        package_id=req.package_id,
        user_account_id=req.user_account_id
    )
    db.add(column)
    db.commit()

    column.created_by = column.company_id
    column.updated_by = column.company_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Company_Subscription info created.',
        'data': {
            'subscription_date': column.subscription_date,
            'expiry_date': column.expiry_date,
            'package_quantity': column.package_quantity,
            'subscription_status': column.subscription_status,
            'subscription_type_code': column.subscription_type_code,
            'subscription_type': column.subscription_type,
            'company_id': column.company_id,
            'package_id': column.package_id,
            'created_at': column.created_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Company_Subscription_Form, db: Session = Depends(get_db)):
    column = db.query(Company_Subscription).filter(
        Company_Subscription.company_id == id).first()

    if column:
        if column.admin_status == 'Active':
            column.subscription_date = req.subscription_date
            column.expiry_date = req.expiry_date
            column.package_quantity = req.package_quantity
            column.subscription_status = req.subscription_status
            column.company_id = req.company_id
            column.package_id = req.package_id
            column.updated_by = req.company_id
            column.updated_at = datetime.now()
            column.updated_at = datetime.now()
            db.commit()
            return {
                'msg': 'Company_Subscription info updated.',
                'data': {
                    'subscription_date': column.subscription_date,
                    'expiry_date': column.expiry_date,
                    'package_quantity': column.package_quantity,
                    'subscription_status': column.subscription_status,
                    'company_id': column.company_id,
                    'package_id': column.package_id
                }
            }
        return {
            'msg': 'Cannot update information. Company Subscription Info is deactivated.'
        }
    return {
        'msg': 'Company Subscription cannot be found.'
    }


# deactivate
@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    column = db.query(Company_Subscription).filter(
        Company_Subscription.company_id == id).first()

    if column:
        if column.subscription_status == 'Active':
            column.subscription_status = 'Inactive'

            db.commit()
            return {
                'msg': 'Subscription deactivated.',
                'email': column.company_id
            }
        return {
            'msg': 'Subscription is already deactivated.'
        }
    return {
        'msg': 'Subscription cannot be found.'
    }
