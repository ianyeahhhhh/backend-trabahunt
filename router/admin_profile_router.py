from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Admin_Profile
from oauth2 import get_current_user
from schemas import Login_Form, Admin_Profile_form

router = APIRouter(
    prefix='/admin_profile',
    tags=['Admin_Profile']
)


# get all active admin
@router.get('/')
async def get_all(db: Session = Depends(get_db)
                  # , current_user: Login_Form = Depends(get_current_user)
                  ):
    data = db.query(Admin_Profile).filter(
        Admin_Profile.admin_status == 'Active').all()
    return data


# get a specific admin
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Admin_Profile).filter(Admin_Profile.admin_id == id).first()
    return data


# post or create an admin
@router.post('/')
async def create(req: Admin_Profile_form, db: Session = Depends(get_db)):
    column = Admin_Profile(
        email=req.email,
        password=Hash.bcrypt(req.password),
        first_name=req.first_name,
        middle_name=req.middle_name,
        last_name=req.last_name,
        suffix_name=req.suffix_name,
        full_name= req.first_name + " " + req.middle_name + " " + req.last_name,
    )
    db.add(column)
    db.commit()

    column.created_by = column.admin_id
    column.updated_by = column.admin_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Admin_Profile info created.',
        'data': {
            'email': column.email,
            'password': Hash.bcrypt(column.password),
            'first_name': column.first_name,
            'middle_name': column.middle_name,
            'last_name': column.last_name,
            'suffix_name': column.suffix_name,
            'full_name': column.full_name
        }
    }


# update an admin
@router.put('/{id}')
async def update(id: int, req: Admin_Profile_form, db: Session = Depends(get_db)):
    column = db.query(Admin_Profile).filter(Admin_Profile.admin_id == id).first()

    if column:
        if column.admin_status == 'Active':
            column.email = req.email
            column.password = Hash.bcrypt(req.password)
            column.first_name = req.first_name
            column.middle_name = req.middle_name
            column.last_name = req.last_name
            column.suffix_name = req.suffix_name
            column.full_name= req.first_name + " " + req.middle_name + " " + req.last_name
            column.updated_at = datetime.now()

            db.commit()

            column.created_by = column.admin_id
            column.updated_by = column.admin_id
            column.created_at = datetime.now()
            column.updated_at = datetime.now()
            db.commit()
            return {
                'msg': 'User_Account info updated.',
                'data': {
                    'email': column.email,
                    'password': Hash.bcrypt(column.password),
                    'first_name': column.first_name,
                    'middle_name': column.middle_name,
                    'last_name': column.last_name,
                    'suffix_name': column.suffix_name,
                    'full_name': column.full_name
                }
            }
        return {
            'msg': 'Cannot update information. User Account is deactivated.'
        }
    return {
        'msg': 'User Account cannot be found.'
    }


# deactivate an admin
@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    column = db.query(Admin_Profile).filter(
        Admin_Profile.admin_id == id).first()

    if column:
        if column.admin_status == 'Active':
            column.admin_status = 'Inactive'

            db.commit()
            return {
                'msg': 'Admin Account deactivated.',
                'email': column.email
            }
        return {
            'msg': 'Admin Account is already deactivated.'
        }
    return {
        'msg': 'Admin Account cannot be found.'
    }
