from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import User_Account
from oauth2 import get_current_user
from schemas import Login_Form, User_Account_Form

router = APIRouter(
    prefix='/user_account',
    tags=['User_Account']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)
                  # , current_user: Login_Form = Depends(get_current_user)
                  ):
    data = db.query(User_Account).filter(
        User_Account.account_status == 'Active').all()

    return data


@router.get('/all_candidate')
async def get_all(db: Session = Depends(get_db)
                  # , current_user: Login_Form = Depends(get_current_user)
                  ):
    data = db.query(User_Account).filter(
        User_Account.user_account_type == 'Candidate').all()

    return data


@router.get('/all_employer')
async def get_all(db: Session = Depends(get_db)
                  # , current_user: Login_Form = Depends(get_current_user)
                  ):
    data = db.query(User_Account).filter(
        User_Account.user_account_type == 'Employer').all()

    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(User_Account).filter(
        User_Account.user_account_id == id).first()
    return data


@router.post('/')
async def create(req: User_Account_Form, db: Session = Depends(get_db)):
    column = User_Account(
        email=req.email,
        password=Hash.bcrypt(req.password),
        user_account_type=req.user_account_type,
        contact_number=req.contact_number
    )
    db.add(column)
    db.commit()

    column.created_by = column.user_account_id
    column.updated_by = column.user_account_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'User_Account info created.',
        'data': {
            'user_account_id': column.user_account_id,
            'user_account_type': column.user_account_type,
            'email': column.email,
            'password': column.password,
            'user_account_type': column.user_account_type,
            'contact_number': column.contact_number,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


@router.put('/{id}')
async def update(id: int, req: User_Account_Form, db: Session = Depends(get_db)
                #, current_user: Login_Form = Depends(get_current_user)
                ):
    column = db.query(User_Account).filter(
        User_Account.user_account_id == id).first()

    if column:
        if column.account_status == 'Active':
            column.email = req.email
            column.password = Hash.bcrypt(req.password)
            column.user_account_type = req.user_account_type
            column.contact_number = req.contact_number
            column.account_status = req.account_status
            column.updated_at = datetime.now()

            db.commit()
            return {
                'msg': 'User_Account info updated.',
                'data': {
                    'user_account_type': column.user_account_type,
                    'email': column.email,
                    'password': column.password,
                    'user_account_type': column.user_account_type,
                    'contact_number': column.contact_number,
                    'updated_by': column.updated_by,
                    'updated_at': column.updated_at
                }
            }
        return {
            'msg': 'Cannot update information. User Account is deactivated.'
        }
    return {
        'msg': 'User Account cannot be found.'
    }


@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)
                #, current_user: Login_Form = Depends(get_current_user)
                ):
    column = db.query(User_Account).filter(
        User_Account.user_account_id == id).first()

    if column:
        if column.account_status == 'Active':
            column.account_status = 'Inactive'

            db.commit()
            return {
                'msg': 'User_Account deactivated.',
                'user_account': column.email
            }
        return {
            'msg': 'User Account is already deactivated.'
        }
    return {
        'msg': 'User Account cannot be found.'
    }
