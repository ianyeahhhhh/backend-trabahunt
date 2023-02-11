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


# All Requests of a specific Employer
@router.get('/all_requests/{id}')
async def get_all_requests(id: int, db: Session = Depends(get_db)):
    data = db.query(Request_Form).filter(
        Request_Form.user_account_id == id).all()
    return data


@router.post('/')
async def create(req: Request_Form_Form, db: Session = Depends(get_db)):
    column = Request_Form(
        company_name=req.company_name,
        specialization=req.specialization,
        department=req.department,
        position=req.position,
        employment_type=req.employment_type,
        salary_range=req.salary_range,
        zip_code=req.zip_code,
        city=req.city,
        region=req.region,
        country=req.country,
        status=req.status,
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
        'msg': 'Request Form info created.',
        'data': {
            'company_name': column.company_name,
            'request_id': column.request_id,
            'specialization': column.specialization,
            'department': column.department,
            'position': column.position,
            'employment_type': column.employment_type,
            'salary_range': column.salary_range,
            'zip_code': column.zip_code,
            'city': column.city,
            'region': column.region,
            'country': column.country,
            'status': column.status,
            'user_account_id': column.user_account_id
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


@router.put('/to_pending/{id}')
async def cancel(id: int, db: Session = Depends(get_db)):
    column = db.query(Request_Form).filter(
        Request_Form.request_id == id).first()

    if column:
        column.status = 'Pending'
        db.commit()

        return {
            'msg': 'Request Sent to HR.'
        }
    return {
        'msg': 'Request Error.'
    }


@router.put('/approve_request/{id}')
async def cancel(id: int, db: Session = Depends(get_db)):
    column = db.query(Request_Form).filter(
        Request_Form.request_id == id).first()

    if column:
        column.status = 'Approved'
        db.commit()

        return {
            'msg': 'Request Approved.'
        }
    return {
        'msg': 'Request Error.'
    }


@router.put('/disapprove_request/{id}')
async def cancel(id: int, db: Session = Depends(get_db)):
    column = db.query(Request_Form).filter(
        Request_Form.request_id == id).first()

    if column:
        column.status = 'Disapproved'
        db.commit()

        return {
            'msg': 'Request Disapproved.'
        }
    return {
        'msg': 'Request Error.'
    }


@router.get('/for_HR/')
async def cancel(db: Session = Depends(get_db)):
    column = db.query(Request_Form).filter(Request_Form.status != 'To be Reviewed').all()

    return column

