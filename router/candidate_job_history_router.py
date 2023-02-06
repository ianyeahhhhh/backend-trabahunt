from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Job_History
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Job_History_Form

router = APIRouter(
    prefix='/candidate_job_history',
    tags=['Candidate_Job_History']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Job_History).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Job_History).filter(
        Candidate_Job_History.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Job_History_Form, db: Session = Depends(get_db)):
    column = Candidate_Job_History(
        previous_job_title=req.previous_job_title,
        employer=req.employer,
        start_date=req.start_date,
        end_date=req.end_date,
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
        'msg': 'Candidate Job History created.',
        'data': {
            'previous_job_title': column.previous_job_title,
            'employer': column.employer,
            'start_date': column.start_date,
            'end_date': column.end_date,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Job_History_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Job_History).filter(
        Candidate_Job_History.user_account_id == id).first()

    if column:
        column.previous_job_title = req.previous_job_title
        column.employer = req.employer
        column.start_date = req.start_date
        column.end_date = req.end_date
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Job History updated.',
            'data': {
                'previous_job_title': column.previous_job_title,
                'employer': column.employer,
                'start_date': column.start_date,
                'end_date': column.end_date,
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
