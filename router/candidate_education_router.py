from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Education
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Education_Form

router = APIRouter(
    prefix='/candidate_education',
    tags=['Candidate_Education']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Education).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Education).filter(
        Candidate_Education.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Education_Form, db: Session = Depends(get_db)):
    column = Candidate_Education(
        highest_educational_attainment=req.highest_educational_attainment,
        institute_name=req.institute_name,
        institute_location=req.institute_location,
        field_of_study=req.field_of_study,
        major=req.major,
        date_graduated=req.date_graduated,
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
        'msg': 'Candidate Education created.',
        'data': {
            'highest_educational_attainment': column.highest_educational_attainment,
            'institute_name': column.institute_name,
            'institute_location': column.institute_location,
            'field_of_study': column.field_of_study,
            'major': column.major,
            'date_graduated': column.date_graduated,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Education_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Education).filter(
        Candidate_Education.user_account_id == id).first()

    if column:
        column.highest_educational_attainment = req.highest_educational_attainment
        column.institute_name = req.institute_name
        column.institute_location = req.institute_location
        column.field_of_study = req.field_of_study
        column.major = req.major
        column.date_graduated = req.date_graduated
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Education updated.',
            'data': {
                'highest_educational_attainment': column.highest_educational_attainment,
                'institute_name': column.institute_name,
                'institute_location': column.institute_location,
                'field_of_study': column.field_of_study,
                'major': column.major,
                'date_graduated': column.date_graduated,
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
