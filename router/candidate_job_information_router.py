from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Job_Information
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Job_Information_Form

router = APIRouter(
    prefix='/candidate_job_information',
    tags=['Candidate_Job_Information']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Job_Information).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Job_Information).filter(
        Candidate_Job_Information.user_account_id == id).first()
    return data


# post or create Candidate Personal Info
@router.post('/')
async def create(req: Candidate_Job_Information_Form, db: Session = Depends(get_db)):
    column = Candidate_Job_Information(
        department=req.department,
        position=req.position,
        employee_category=req.employee_category,
        employment_type=req.employment_type,
        specialization=req.specialization,
        date_hired=req.date_hired,
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
        'msg': 'Candidate Job Info created.',
        'data': {
            'department': column.department,
            'position': column.position,
            'employee_category': column.employee_category,
            'employment_type': column.employment_type,
            'specialization': column.specialization,
            'date_hired': column.date_hired,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Job_Information_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Job_Information).filter(
        Candidate_Job_Information.user_account_id == id).first()

    if column:
        column.department = req.department,
        column.position = req.position,
        column.employee_category = req.employee_category,
        column.employment_type = req.employment_type,
        column.specialization = req.specialization,
        column.date_hired = req.date_hired,
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Job Info updated.',
            'data': {
                'department': column.department,
                'position': column.position,
                'employee_category': column.employee_category,
                'employment_type': column.employment_type,
                'specialization': column.specialization,
                'date_hired': column.date_hired,
                'user_account_id': column.user_account_id,
                'created_by': column.created_by,
                'created_at': column.created_at,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at,
            }
        }
    return {
        'msg': 'User Account cannot be found.'
    }

