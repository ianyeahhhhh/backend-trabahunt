from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Family_Background
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Family_Background_Form

router = APIRouter(
    prefix='/candidate_family_background',
    tags=['Candidate_Family_Background']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Family_Background).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Family_Background).filter(
        Candidate_Family_Background.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Family_Background_Form, db: Session = Depends(get_db)):
    column = Candidate_Family_Background(
        # mothers_first_name=req.mothers_first_name,
        # mothers_middle_name=req.mothers_middle_name,
        # mothers_last_name=req.mothers_last_name,
        mothers_name=req.mothers_name,
        mothers_occupation=req.mothers_occupation,
        mothers_birth_date=req.mothers_birth_date,
        # fathers_first_name=req.fathers_first_name,
        # fathers_middle_name=req.fathers_middle_name,
        # fathers_last_name=req.fathers_last_name,
        fathers_name=req.fathers_name,
        fathers_occupation=req.fathers_occupation,
        fathers_birth_date=req.fathers_birth_date,
        number_of_siblings=req.number_of_siblings,
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
        'msg': 'Candidate Family Background created.',
        'data': {
            # 'mothers_first_name': column.mothers_first_name,
            # 'mothers_middle_name': column.mothers_middle_name,
            # 'mothers_last_name': column.mothers_last_name,
            'mothers_name': column.mothers_name,
            'mothers_occupation': column.mothers_occupation,
            'mothers_birth_date': column.mothers_birth_date,
            'fathers_name': column.fathers_name,
            # 'fathers_first_name': column.fathers_first_name,
            # 'fathers_middle_name': column.fathers_middle_name,
            # 'fathers_last_name': column.fathers_last_name,
            'fathers_occupation': column.fathers_occupation,
            'fathers_birth_date': column.fathers_birth_date,
            'number_of_siblings': column.number_of_siblings,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Family_Background_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Family_Background).filter(
        Candidate_Family_Background.user_account_id == id).first()

    if column:
        # column.mothers_first_name = req.mothers_first_name
        # column.mothers_middle_name = req.mothers_middle_name
        # column.mothers_last_name = req.mothers_last_name
        column.mothers_name = req.mothers_name
        column.mothers_occupation = req.mothers_occupation
        column.mothers_birth_date = req.mothers_birth_date
        # column.fathers_first_name = req.fathers_first_name
        # column.fathers_middle_name = req.fathers_middle_name
        # column.fathers_last_name = req.fathers_last_name
        column.fathers_name = req.fathers_name
        column.fathers_occupation = req.fathers_occupation
        column.fathers_birth_date = req.fathers_birth_date
        column.number_of_siblings = req.number_of_siblings
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Family Background updated.',
            'data': {
                # 'mothers_first_name': column.mothers_first_name,
                # 'mothers_middle_name': column.mothers_middle_name,
                # 'mothers_last_name': column.mothers_last_name,
                'mothers_name': column.mothers_name,
                'mothers_occupation': column.mothers_occupation,
                'mothers_birth_date': column.mothers_birth_date,
                # 'fathers_first_name': column.fathers_first_name,
                # 'fathers_middle_name': column.fathers_middle_name,
                # 'fathers_last_name': column.fathers_last_name,
                'fathers_name': column.fathers_name,
                'fathers_occupation': column.fathers_occupation,
                'fathers_birth_date': column.fathers_birth_date,
                'number_of_siblings': column.number_of_siblings,
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
