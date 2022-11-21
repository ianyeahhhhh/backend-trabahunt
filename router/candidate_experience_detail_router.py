from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

from models import Candidate_Experience_Detail
from schemas import Candidate_Experience_Detail_Form

router = APIRouter(
    prefix='/candidate_experience_detail',
    tags=['Candidate_Experience_Detail']
)


# get all info
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Experience_Detail).all()

    return data


# get a specific info
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Experience_Detail).filter(
        Candidate_Experience_Detail.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Experience_Detail_Form, db: Session = Depends(get_db)):
    column = Candidate_Experience_Detail(
        user_account_id=req.user_account_id,
        experience_level=req.experience_level,
        experience_description=req.experience_description,
        year_month_work_experience=req.year_month_work_experience
    )

    db.add(column)
    db.commit()

    column.created_by = column.user_account_id
    column.updated_by = column.user_account_id
    column.updated_at = datetime.now()
    column.created_at = datetime.now()
    db.commit()

    return {
        'msg': 'Candidate_Experience_Detail info created.',
        'data': {
            'candidate_experience_detail_id': column.candidate_experience_detail_id,
            'experience_level': column.experience_level,
            'experience_description': column.experience_description,
            'year_month_work_experience': column.year_month_work_experience,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Experience_Detail_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Experience_Detail).filter(
        Candidate_Experience_Detail.user_account_id == id).first()

    if column:
        column.experience_level = req.experience_level
        column.experience_description = req.experience_description
        column.user_account_id = req.user_account_id
        column.year_month_work_experience = req.year_month_work_experience
        column.updated_at = datetime.now()

        db.commit()
        return {
            'msg': 'Candidate_Experience_Detail info updated.',
            'data': {
                'candidate_experience_detail_id': column.candidate_experience_detail_id,
                'experience_level': column.experience_level,
                'experience_description': column.experience_description,
                'year_month_work_experience': column.year_month_work_experience,
                'user_account_id': column.user_account_id,
                'created_by': column.created_by,
                'updated_by': column.updated_by,
                'created_at': column.created_at,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'Candidate Experience Detail not found.'
    }
