from datetime import date, datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Interview_Info
from oauth2 import get_current_user
from schemas import Login_Form, Interview_Info_Form
router = APIRouter(
    prefix='/interview_info',
    tags=['Interview_Info']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Interview_Info).all()
    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Interview_Info).filter(
        Interview_Info.interview_info_id == id).first()
    return data


@router.post('/')
async def create(req: Interview_Info_Form, db: Session = Depends(get_db)):
    column = Interview_Info(
        candidate_profile_id=req.candidate_profile_id,
        interview_date=req.interview_date,
        interview_time=req.interview_time,
        interview_location=req.interview_location,
        interview_additional_info=req.interview_additional_info,
        interview_status=req.interview_status,
        interview_remarks=req.interview_remarks,
        created_by=req.created_by,
        updated_by=req.updated_by
    )
    db.add(column)
    db.commit()

    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Job Application info added.',
        'data': {
            'interview_info_id': column.interview_info_id,
            'candidate_profile_id': column.candidate_profile_id,
            'interview_date': column.interview_date,
            'interview_time': column.interview_time,
            'interview_location': column.interview_location,
            'interview_additional_info': column.interview_additional_info,
            'interview_status': column.interview_status,
            'interview_remarks': column.interview_remarks
        }
    }


@router.put('/{id}')
async def create(id: int, req: Interview_Info_Form, db: Session = Depends(get_db)):
    column = db.query(Interview_Info).filter(
        Interview_Info.interview_info_id == id).first()

    if column:
        column.candidate_profile_id = req.candidate_profile_id,
        column.interview_date = req.interview_date,
        column.interview_time = req.interview_time,
        column.interview_location = req.interview_location,
        column.interview_additional_info = req.interview_additional_info,
        column.interview_remarks = req.interview_remarks,
        column.interview_status = req.interview_status,
        column.created_by=req.created_by,
        column.updated_by=req.updated_by
        db.commit()

        return {
            'msg': 'Interview info updated.',
            'data': {
                'candidate_profile_id': column.candidate_profile_id,
                'interview_date': column.interview_date,
                'interview_time': column.interview_time,
                'interview_location': column.interview_location,
                'interview_additional_info': column.interview_additional_info,
                'interview_status': column.interview_status,
                'interview_remarks': column.interview_remarks,
            }
        }

    return {
        'msg': 'Interview Info cannot be found'
    }


@router.put('/accept/{id}')
async def create(id: int, db: Session = Depends(get_db)):
    column = db.query(Interview_Info).filter(
        Interview_Info.interview_info_id == id).first()

    if column:
        column.interview_status = 'Accepted'
        db.commit()

        return {
            'msg': 'Candidate Hired.',
            'data': {
                'job_application_id': column.interview_info_id,
                'candidate_profile_id': column.candidate_profile_id
            }
        }

    return {
        'msg': 'Interview Info cannot be found'
    }


@router.put('/reject/{id}')
async def create(id: int, db: Session = Depends(get_db)):
    column = db.query(Interview_Info).filter(
        Interview_Info.interview_info_id == id).first()

    if column:
        column.interview_status = 'Rejected'
        db.commit()

        return {
            'msg': 'Candidate Rejected.',
            'data': {
                'job_application_id': column.interview_info_id,
                'candidate_profile_id': column.candidate_profile_id
            }
        }

    return {
        'msg': 'Interview Info cannot be found'
    }


@router.put('/cancel/{id}')
async def create(id: int, db: Session = Depends(get_db)):
    column = db.query(Interview_Info).filter(
        Interview_Info.interview_info_id == id).first()

    if column:
        column.interview_status = 'Cancelled'
        db.commit()

        return {
            'msg': 'Interview Cancelled.',
            'data': {
                'job_application_id': column.interview_info_id,
                'candidate_profile_id': column.candidate_profile_id
            }
        }

    return {
        'msg': 'Interview Info cannot be found'
    }