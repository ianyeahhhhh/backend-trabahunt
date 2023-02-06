from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Character_References
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Character_References_Form

router = APIRouter(
    prefix='/candidate_character_references',
    tags=['Candidate_Character_References']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Character_References).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Character_References).filter(
        Candidate_Character_References.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Character_References_Form, db: Session = Depends(get_db)):
    column = Candidate_Character_References(
        char_ref_name_1=req.char_ref_name_1,
        position_1=req.position_1,
        telephone_1=req.telephone_1,
        company_1=req.company_1,
        char_ref_name_2=req.char_ref_name_2,
        position_2=req.position_2,
        telephone_2=req.telephone_2,
        company_2=req.company_2,
        char_ref_name_3=req.char_ref_name_3,
        position_3=req.position_3,
        telephone_3=req.telephone_3,
        company_3=req.company_3,
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
        'msg': 'Candidate Character References created.',
        'data': {
            'char_ref_name_1': column.char_ref_name_1,
            'position_1': column.position_1,
            'telephone_1': column.telephone_1,
            'company_1': column.company_1,
            'char_ref_name_2': column.char_ref_name_2,
            'position_2': column.position_2,
            'telephone_2': column.telephone_2,
            'company_2': column.company_2,
            'char_ref_name_3': column.char_ref_name_3,
            'position_3': column.position_3,
            'telephone_3': column.telephone_3,
            'company_3': column.company_3,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Character_References_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Character_References).filter(
        Candidate_Character_References.user_account_id == id).first()

    if column:
        column.char_ref_name_1 = req.char_ref_name_1
        column.position_1 = req.position_1
        column.telephone_1 = req.telephone_1
        column.company_1 = req.company_1
        column.char_ref_name_2 = req.char_ref_name_2
        column.position_2 = req.position_2
        column.telephone_2 = req.telephone_2
        column.company_2 = req.company_2
        column.char_ref_name_3 = req.char_ref_name_3
        column.position_3 = req.position_3
        column.telephone_3 = req.telephone_3
        column.company_3 = req.company_3
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Character References updated.',
            'data': {
                'char_ref_name_1': column.char_ref_name_1,
                'position_1': column.position_1,
                'telephone_1': column.telephone_1,
                'company_1': column.company_1,
                'char_ref_name_2': column.char_ref_name_2,
                'position_2': column.position_2,
                'telephone_2': column.telephone_2,
                'company_2': column.company_2,
                'char_ref_name_3': column.char_ref_name_3,
                'position_3': column.position_3,
                'telephone_3': column.telephone_3,
                'company_3': column.company_3,
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
