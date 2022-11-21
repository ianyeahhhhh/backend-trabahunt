from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Job_Additional_Info
from oauth2 import get_current_user
from schemas import Login_Form, Job_Additional_Info_Form
router = APIRouter(
    prefix='/job_additional_info',
    tags=['Job_Additional_Info']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Job_Additional_Info).all()
    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Additional_Info).filter(
        Job_Additional_Info.job_post_id == id).first()
    return data


@router.post('/')
async def create(req: Job_Additional_Info_Form, db: Session = Depends(get_db)):
    column = Job_Additional_Info(
        job_type_name=req.job_type_name,
        job_specialization_name=req.job_specialization_name,
        job_qualification=req.job_qualification,
        career_level=req.career_level,
        job_post_id=req.job_post_id
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'Job Additional info created.',
        'data': {
            'job_type_name': column.job_type_name,
            'job_specialization_name': column.job_specialization_name,
            'job_qualification': column.job_qualification,
            'career_level': column.career_level,
            'job_post_id': column.job_post_id
        }
    }


@router.put('/{id}')
async def update(id: int, req: Job_Additional_Info_Form, db: Session = Depends(get_db)):
    column = db.query(Job_Additional_Info).filter(
        Job_Additional_Info.job_post_id == id).first()

    if column:
        column.job_type_name = req.job_type_name,
        column.job_specialization_name = req.job_specialization_name,
        column.job_qualification = req.job_qualification,
        column.career_level = req.career_level,
        column.job_post_id = req.job_post_id
        db.commit()

        return {
            'msg': 'Job Additional info updated.',
            'data': {
                'job_type_name': column.job_type_name,
                'job_specialization_name': column.job_specialization_name,
                'job_qualification': column.job_qualification,
                'career_level': column.career_level,
                'job_post_id': column.job_post_id
            }
        }
    return {
        'msg': 'Job Additional Info cannot be found.'
    }
