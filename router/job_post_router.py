from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Job_Post
from oauth2 import get_current_user
from schemas import Login_Form, Job_Post_Form
router = APIRouter(
    prefix='/job_post',
    tags=['Job_Post']
)


# FOR ONE JOB AD (FOR VIEWING)
@router.get('/get_one/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.job_post_id == id).first()
    return data


# FOR ALL JOB ADS (FOR ADMIN)
@router.get('/all')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Job_Post).all()
    return data


# FOR ALL PENDING JOB ADS (FOR ADMIN)
@router.get('/all/pending')
async def get_all_pending(db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(
        Job_Post.job_post_status == 'Pending').all()
    return data


# FOR ALL NON-PENDING JOB ADS (FOR ADMIN)
@router.get('/all/except_pending')
async def get_all_with_user(db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(
        Job_Post.job_post_status != 'Pending').all()
    return data


# FOR ALL NON-PENDING OR INACTIVE JOB ADS (FOR CANDIDATE)
@router.get('/all/except_pending_for_candidate')
async def get_all_with_user(db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.job_post_status !=
                                     'Pending' and Job_Post.job_post_status != 'Inactive').all()
    return data


# FOR ALL JOB ADS OF USER_ID (FOR EMPLOYER)
@router.get('/all/{id}')
async def get_all_with_user(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(
        Job_Post.user_account_id == id).all()
    return data


# FOR ALL JOB ADS OF USER_ID (FOR EMPLOYER)
@router.get('/all/except_pending/{id}')
async def get_all_with_user(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.user_account_id == id).filter(
        Job_Post.job_post_status != 'Pending').all()
    return data


# FOR ALL ACCEPTED JOB ADS OF USER_ID (FOR EMPLOYER)
@router.get('/all/accepted/{id}')
async def get_all_accepted_with_user(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.user_account_id == id).filter(
        Job_Post.job_post_status == 'Accepted').all()
    return data


# FOR ALL REJECTED JOB ADS OF USER_ID (FOR EMPLOYER)
@router.get('/all/rejected/{id}')
async def get_all_accepted_with_user(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.user_account_id == id).filter(
        Job_Post.job_post_status == 'Rejected').all()
    return data


# FOR PENDING JOB ADS OF USER_ID (FOR EMPLOYER)
@router.get('/all/pending/{id}')
async def get_all_pending_with_user(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Post).filter(Job_Post.user_account_id == id).filter(
        Job_Post.job_post_status == 'Pending').all()
    return data


@router.post('/')
async def create(req: Job_Post_Form, db: Session = Depends(get_db)):
    column = Job_Post(
        job_description=req.job_description,
        job_post_status=req.job_post_status,
        job_title=req.job_title,
        job_position_level=req.job_position_level,
        salary=req.salary,
        user_account_id=req.user_account_id,
        job_location_id=req.job_location_id,
        company_id=req.company_id
    )
    db.add(column)
    db.commit()

    column.created_by = column.user_account_id
    column.updated_by = column.user_account_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Job Post info created.',
        'data': {
            'job_post_id': column.job_post_id,
            'job_description': column.job_description,
            'job_post_status': column.job_post_status,
            'job_title': column.job_title,
            'job_position_level': column.job_position_level,
            'salary': column.salary,
            'user_account_id': column.user_account_id,
            'job_location_id': column.job_location_id,
            'company_id': column.company_id
        }
    }


@router.put('/accept_job_ad/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Post).filter(
        Job_Post.job_post_id == id).first()

    if column:
        column.job_post_status = 'Accepted'
        db.commit()

        return {
            'msg': 'Job Post Accepted.',
            'data': {
                'job_description': column.job_description,
                'job_post_status': column.job_post_status,
                'job_title': column.job_title,
                'job_position_level': column.job_position_level,
                'salary': column.salary,
                'user_account_id': column.user_account_id,
                'job_location_id': column.job_location_id,
                'company_id': column.company_id
            }
        }
    return {
        'msg': 'Job Post cannot be found.'
    }


@router.put('/reject_job_ad/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Post).filter(
        Job_Post.job_post_id == id).first()

    if column:
        column.job_post_status = 'Rejected'
        db.commit()

        return {
            'msg': 'Job Post Rejected.',
            'data': {
                'job_description': column.job_description,
                'job_post_status': column.job_post_status,
                'job_title': column.job_title,
                'job_position_level': column.job_position_level,
                'salary': column.salary,
                'user_account_id': column.user_account_id,
                'job_location_id': column.job_location_id,
                'company_id': column.company_id
            }
        }
    return {
        'msg': 'Job Post cannot be found.'
    }


@router.put('/{id}')
async def update(id: int, req: Job_Post_Form, db: Session = Depends(get_db)):
    column = db.query(Job_Post).filter(
        Job_Post.job_post_id == id).first()

    if column:
        column.job_description = req.job_description,
        column.job_post_status = req.job_post_status,
        column.job_title = req.job_title,
        column.job_position_level = req.job_position_level,
        column.salary = req.salary,
        column.user_account_id = req.user_account_id,
        column.job_location_id = req.job_location_id,
        column.company_id = req.company_id
        db.commit()

        return {
            'msg': 'Job Post info updated.',
            'data': {
                'job_description': column.job_description,
                'job_post_status': column.job_post_status,
                'job_title': column.job_title,
                'job_position_level': column.job_position_level,
                'salary': column.salary,
                'user_account_id': column.user_account_id,
                'job_location_id': column.job_location_id,
                'company_id': column.company_id
            }
        }
    return {
        'msg': 'Job Post cannot be found.'
    }


@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    column = db.query(Job_Post).filter(
        Job_Post.job_post_id == id).first()

    if column:
        column.job_post_status = 'Inactive'
        db.commit()

        return {
            'msg': 'Job Post info deleted.',
            'data': {
                'job_post_id': column.job_post_id,
            }
        }
    return {
        'msg': 'Job Post cannot be found.'
    }
