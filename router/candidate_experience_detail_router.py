from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Experience_Detail
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Experience_Detail_Form

router = APIRouter(
    prefix='/candidate_experience_detail',
    tags=['Candidate_Experience_Detail']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Experience_Detail).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Experience_Detail).filter(
        Candidate_Experience_Detail.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Experience_Detail_Form, db: Session = Depends(get_db)):
    column = Candidate_Experience_Detail(
        experience_level=req.experience_level,
        work_experience=req.work_experience,
        personal_skills=req.personal_skills,
        achievements=req.achievements,
        certification=req.certification,
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
        'msg': 'Candidate Experience Detail created.',
        'data': {
            'experience_level': column.experience_level,
            'work_experience': column.work_experience,
            'personal_skills': column.personal_skills,
            'achievements': column.achievements,
            'certification': column.certification,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
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
        column.work_experience = req.work_experience
        column.personal_skills = req.personal_skills
        column.achievements = req.achievements
        column.certification = req.certification
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Experience Detail updated.',
            'data': {
                'experience_level': column.experience_level,
                'work_experience': column.work_experience,
                'personal_skills': column.personal_skills,
                'achievements': column.achievements,
                'certification': column.certification,
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
