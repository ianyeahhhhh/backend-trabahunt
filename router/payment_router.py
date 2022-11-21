from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Payment
from oauth2 import get_current_user
from schemas import Login_Form, Payment_Form

router = APIRouter(
    prefix='/payment',
    tags=['Payment']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Payment).all()
    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Payment).filter(
        Payment.company_subscription_id == id).first()
    return data


@router.post('/')
async def create(req: Payment_Form, db: Session = Depends(get_db)):
    column = Payment(
        payment_description=req.payment_description,
        payment_type=req.payment_type,
        company_id=req.company_id,
        company_subscription_id=req.company_subscription_id
    )
    db.add(column)
    db.commit()

    column.created_by = column.company_subscription_id
    column.updated_by = column.company_subscription_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Payment info created.',
        'data': {
            'payment_description': column.payment_description,
            'payment_type': column.payment_type,
            'company_id': column.company_id,
            'company_subscription_id': column.company_subscription_id
        }
    }


@router.put('/{id}')
async def update(id: int, req: Payment_Form, db: Session = Depends(get_db)):
    column = db.query(Payment).filter(
        Payment.company_subscription_id == id).first()

    if column:
        column.payment_description = req.payment_description
        column.payment_type = req.payment_type
        column.company_id = req.company_id
        column.company_subscription_id = req.company_subscription_id
        db.commit()

        return {
            'msg': 'Payment info updated.',
            'data': {
               'payment_description': column.payment_description,
               'payment_type': column.payment_type,
                'company_id': column.company_id,
                'company_subscription_id': column.company_subscription_id
            }
        }
    return {
        'msg': 'Payment cannot be found.'
    }
