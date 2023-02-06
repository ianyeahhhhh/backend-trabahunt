from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Emergency_Contact
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Emergency_Contact_Form

router = APIRouter(
    prefix='/candidate_emergency_contact',
    tags=['Candidate_Emergency_Contact']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Emergency_Contact).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Emergency_Contact).filter(
        Candidate_Emergency_Contact.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Emergency_Contact_Form, db: Session = Depends(get_db)):
    column = Candidate_Emergency_Contact(
        name=req.name,
        relationship=req.relationship,
        contact_number=req.contact_number,
        address=req.address,
        user_account_id=req.user_account_id
    )
    db.add(column)
    db.commit()

    column.created_by = column.user_account_id
    column.updated_by = column.user_account_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Candidate Emergency Contact created.',
        'data': {
            'name': column.name,
            'relationship': column.relationship,
            'contact_number': column.contact_number,
            'address': column.address,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Emergency_Contact_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Emergency_Contact).filter(
        Candidate_Emergency_Contact.user_account_id == id).first()

    if column:
        column.name = req.name
        column.relationship = req.relationship
        column.contact_number = req.contact_number
        column.address = req.address
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Emergency Contact updated.',
            'data': {
                'name': column.name,
                'relationship': column.relationship,
                'contact_number': column.contact_number,
                'address': column.address,
                'user_account_id': column.user_account_id,
                'created_by': column.created_by,
                'created_at': column.created_at,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'User Account cannot be found.'
    }
