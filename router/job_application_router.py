from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Job_Application
from oauth2 import get_current_user
from schemas import Login_Form, Job_Application_Form
router = APIRouter(
    prefix='/job_application',
    tags=['Job_Application']
)


# GET ONE JOB APP
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(
        Job_Application.job_application_id == id).first()
    return data


# GET ALL
@router.get('/all')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Job_Application).all()
    return data


# GET ALL APPLICATIONS FOR SPECIFIC COMPANY
@router.get('/all/{id}')
async def get_all_for_an_employer(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(
        Job_Application.employer_id == id).all()
    return data


# GET ALL HIRED FOR A SPECIFIC COMPANY
@router.get('/all/hired/{id}')
async def get_all_hired_for_an_employer(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(
        Job_Application.employer_id == id).filter(Job_Application.job_application_status == 'Accepted').all()
    return data


# GET ALL PENDING JOB APPS FOR A SPECIFIC COMPANY
@router.get('/all/except_enlisted/{id}')
async def get_all_pending(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.employer_id == id).filter(
        Job_Application.job_application_status != 'For Interview').all()
    return data


# GET ALL PENDING JOB APPS FOR A SPECIFIC COMPANY AND JOB POST
@router.get('/all/except_enlisted/{id}/{id1}')
async def get_all_pending(id: int, id1: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.employer_id == id).filter(Job_Application.job_post_id == id1).filter(
        Job_Application.job_application_status != 'For Interview').all()
    return data


# GET ALL ENLISTED/FOR INTERVIEW JOB APPS FOR A SPECIFIC COMPANY
@router.get('/all/enlisted/{id}')
async def get_all_pending(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.employer_id == id).filter(
        Job_Application.job_application_status == 'For Interview').all()
    return data


# GET ALL PENDING JOB APPS FOR A SPECIFIC CANDIDATE
@router.get('/all/pending_candidate/{id}')
async def get_all_pending_candidate(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.candidate_personal_information_id == id).filter(
        Job_Application.job_application_status == 'Pending').all()
    return data


# GET ALL ACCEPTED JOB APPS FOR A SPECIFIC CANDIDATE
@router.get('/all/accepted_candidate/{id}')
async def get_all_accepted_candidate(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.candidate_personal_information_id == id).filter(
        Job_Application.job_application_status == 'Accepted').all()
    return data


# GET ALL REJECTED JOB APPS FOR A SPECIFIC CANDIDATE
@router.get('/all/rejected_candidate/{id}')
async def get_all_rejected_candidate(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.candidate_personal_information_id == id).filter(
        Job_Application.job_application_status == 'Rejected').all()
    return data


# GET ALL NON-PENDING JOB APPS FOR A SPECIFIC COMPANY
@router.get('/all/except_pending/{id}')
async def get_all_except_pending(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.employer_id == id).filter(
        Job_Application.job_application_status != 'Pending').all()
    return data


# GET ALL NON-PENDING JOB APPS FOR A SPECIFIC COMPANY
@router.get('/all/except_pending_candidate/{id}')
async def get_all_except_pending_candidate(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(Job_Application.candidate_personal_information_id == id).filter(
        Job_Application.job_application_status != 'Pending').all()
    return data


# CREATE/ADD A JOB APPLICATION
@router.post('/')
async def create(req: Job_Application_Form, db: Session = Depends(get_db)):
    column = Job_Application(
        full_name=req.full_name,
        email=req.email,
        contact_number=req.contact_number,
        candidate_personal_information_id=req.candidate_personal_information_id,
        interview_info_id=req.interview_info_id,
        employer_id=req.employer_id,
        job_post_id=req.job_post_id,
        created_at=datetime.now()
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'Job Application info created.',
        'data': {
            'full_name': column.full_name,
            'email': column.email,
            'contact_number': column.contact_number,
            'candidate_personal_information_id': column.candidate_personal_information_id,
            'employer_id': column.employer_id,
            'interview_info_id': column.interview_info_id,
            'job_application_id': column.job_application_id,
            'job_post_id': column.job_post_id
        }
    }


# UPDATE A JOB APPLICATION
@router.put('/{id}')
async def update(id: int, req: Job_Application_Form, db: Session = Depends(get_db)):
    column = db.query(Job_Application).filter(
        Job_Application.job_application_id == id).first()

    if column:
        column.full_name = req.full_name
        column.email = req.email
        column.contact_number = req.contact_number
        column.job_application_status = req.job_application_status
        db.commit()

        return {
            'msg': 'Job Application info updated.',
            'data': {
                'full_name': column.full_name,
                'email': column.email,
                'contact_number': column.contact_number,
                'candidate_personal_information_id': column.candidate_personal_information_id,
                'employer_id': column.employer_id,
                'job_application_id': column.job_application_id,
                'job_application_status': column.job_application_status
            }
        }
    return {
        'msg': 'Job Application Info cannot be found.'
    }


# FOR INTERVIEW / ENLIST
@router.put('/enlist/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Application).filter(
        Job_Application.job_application_id == id).first()

    if column:
        column.job_application_status = 'For Interview'
        db.commit()

        return {
            'msg': 'Job Application Accepted.',
            'data': {
                'full_name': column.full_name,
                'email': column.email,
                'contact_number': column.contact_number,
                'candidate_personal_information_id': column.candidate_personal_information_id,
                'employer_id': column.employer_id,
                'interview_info_id': column.interview_info_id,
                'job_application_id': column.job_application_id,
                'job_application_status': column.job_application_status
            }
        }
    return {
        'msg': 'Job Application Info cannot be found.'
    }


# ACCEPT A JOB APPLICATION
@router.put('/accept/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Application).filter(
        Job_Application.job_application_id == id).first()

    if column:
        column.job_application_status = 'Accepted'
        db.commit()

        return {
            'msg': 'Job Application Accepted.',
            'data': {
                'full_name': column.full_name,
                'email': column.email,
                'contact_number': column.contact_number,
                'candidate_personal_information_id': column.candidate_personal_information_id,
                'employer_id': column.employer_id,
                'interview_info_id': column.interview_info_id,
                'job_application_id': column.job_application_id,
                'job_application_status': column.job_application_status
            }
        }
    return {
        'msg': 'Job Application Info cannot be found.'
    }


# REJECT A JOB APPLICATION
@router.put('/reject/{id}')
async def remove(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Application).filter(
        Job_Application.job_application_id == id).first()

    if column:
        column.job_application_status = 'Rejected'
        db.commit()

        return {
            'msg': 'Job Application Rejected.',
            'data': {
                'full_name': column.full_name,
                'email': column.email,
                'contact_number': column.contact_number,
                'candidate_personal_information_id': column.candidate_personal_information_id,
                'job_application_id': column.job_application_id,
                'interview_info_id': column.interview_info_id,
            }
        }

    return {
        'msg': 'Job Application cannot be found'
    }

#MOST RECENT JOB APP order_by(User_Account.created_at.desc())
@router.get('/most_recent/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Application).filter(
        Job_Application.employer_id == id).filter(Job_Application.job_application_status == 'For Interview').order_by(Job_Application.created_at.desc()).first()
    return data