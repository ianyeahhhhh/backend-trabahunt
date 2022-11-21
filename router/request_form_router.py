from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Request_Form
from oauth2 import get_current_user
from schemas import Login_Form, Request_Form_Form

router = APIRouter(
    prefix='/request_form',
    tags=['Request_Form']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Request_Form).all()
    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Request_Form).filter(
        Request_Form.request_id == id).first()
    return data


@router.get('/all_requests/{id}')
async def get_all_requests(id: int, db: Session = Depends(get_db)):
    data = db.query(Request_Form).filter(
        Request_Form.user_account_id == id).all()
    return data


@router.post('/')
async def create(req: Request_Form_Form, db: Session = Depends(get_db)):
    column = Request_Form(
        user_account_id=req.user_account_id,
        job_position=req.job_position,
        job_specialization_name=req.job_specialization_name,
        zip_code=req.zip_code,
        city=req.city,
        region=req.region,
        country=req.country,
        salary_range=req.salary_range,
        job_type_name=req.job_type_name,
        status=req.status
    )
    db.add(column)
    db.commit()

    column.created_by = column.user_account_id
    column.updated_by = column.user_account_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Request Form info created.',
        'data': {
            'request_id':column.request_id,
            'user_account_id':column.user_account_id,
            'job_position':column.job_position,
            'job_specialization_name':column.job_specialization_name,
            'zip_code':column.zip_code,
            'city':column.city,
            'region':column.region,
            'country':column.country,
            'salary_range':column.salary_range,
            'job_type_name':column.job_type_name,
            'status':column.status,
            'created_by':column.created_by,
            'created_at':column.created_at,
            'updated_by':column.updated_by,
            'updated_at':column.updated_at
        }
    }


@router.put('/cancel_request/{id}')
async def cancel(id: int, db: Session = Depends(get_db)):
    column = db.query(Request_Form).filter(
        Request_Form.request_id == id).first()

    if column:
        column.status = 'Cancelled'
        db.commit()

        return {
            'msg': 'Request Cancelled.'
        }
    return {
        'msg': 'Request Cancellation error.'
    }
