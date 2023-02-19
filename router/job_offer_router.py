from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Job_Offer
from schemas import Job_Offer_Form


router = APIRouter(
    prefix='/job_offer',
    tags=['Job_Offer']
)


@router.get('/for_employer/{id}')
async def get_one_for_employer(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Offer).filter(Job_Offer.job_offer_id == id).first()
    return data


# logged in: candidate. // all job offered to a specific candidate
@router.get('/all_for_candidate/{id}')
async def get_all_for_candidate(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Offer).filter(Job_Offer.offered_to == id).all()
    return data


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Job_Offer).all()
    return data


@router.get('/all_for_an_employer/{id}')
async def get_all_for_an_employer(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Offer).filter(Job_Offer.created_by == id).all()
    return data


@router.post('/')
async def create(req: Job_Offer_Form, db: Session = Depends(get_db)):
    column = Job_Offer(
        offered_to=req.offered_to,
        job_title=req.job_title,
        job_position=req.job_position,
        salary=req.salary,
        city=req.city,
        region=req.region,
        zip_code=req.zip_code,
        country=req.country,
        job_offer_description=req.job_offer_description,
        job_offer_status=req.job_offer_status,
        interview_info_id=req.interview_info_id,
        company_id=req.company_id,
        created_by=req.created_by,
        updated_by=req.updated_by
    )
    db.add(column)
    db.commit()

    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Job Offer Created',
        'data': {
            'offered_to': column.offered_to,
            'job_title': column.job_title,
            'job_position': column.job_position,
            'salary': column.salary,
            'city': column.city,
            'region': column.region,
            'zip_code': column.zip_code,
            'country': column.country,
            'job_offer_description': column.job_offer_description,
            'job_offer_status': column.job_offer_status,
            'interview_info_id': column.interview_info_id,
            'company_id': column.company_id
        }
    }


@router.put('/{id}')
async def update(id: int, req: Job_Offer_Form, db: Session = Depends(get_db)):

    column = db.query(Job_Offer).filter(Job_Offer.job_offer_id == id).first()

    if column:
        column.offered_to=req.offered_to,
        column.job_title=req.job_title,
        column.job_position=req.job_position,
        column.salary=req.salary,
        column.city=req.city,
        column.region=req.region,
        column.zip_code=req.zip_code,
        column.country=req.country,
        column.job_offer_description=req.job_offer_description,
        column.job_offer_status=req.job_offer_status,
        column.interview_info_id=req.interview_info_id,
        column.company_id=req.company_id,
        column.created_by=req.created_by,
        column.updated_by=req.updated_by,
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Job Offer Updated',
            'data': {
                'offered_to': column.offered_to,
                'job_title': column.job_title,
                'job_position': column.job_position,
                'salary': column.salary,
                'city': column.city,
                'region': column.region,
                'zip_code': column.zip_code,
                'country': column.country,
                'job_offer_description': column.job_offer_description,
                'job_offer_status': column.job_offer_status,
                'interview_info_id': column.interview_info_id,
                'company_id': column.company_id
            }
        }


@router.put('/cancel/{id}')
async def cancel(id: int, db: Session = Depends(get_db)):

    column = db.query(Job_Offer).filter(Job_Offer.job_offer_id == id).first()

    if column:
        column.job_offer_status = 'Cancelled'
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Job Offer Canceled',
            'data': {
                'offered_to': column.offered_to,
                'job_title': column.job_title,
                'job_position': column.job_position,
                'salary': column.salary,
                'city': column.city,
                'region': column.region,
                'zip_code': column.zip_code,
                'country': column.country,
                'job_offer_description': column.job_offer_description,
                'job_offer_status': column.job_offer_status,
                'interview_info_id': column.interview_info_id,
                'company_id': column.company_id
            }
        }


@router.put('/accept/{id}')
async def accept(id: int, db: Session = Depends(get_db)):

    column = db.query(Job_Offer).filter(Job_Offer.job_offer_id == id).first()

    if column:
        column.job_offer_status = 'Accepted'
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Job Offer Canceled',
            'data': {
                'offered_to': column.offered_to,
                'job_title': column.job_title,
                'job_position': column.job_position,
                'salary': column.salary,
                'city': column.city,
                'region': column.region,
                'zip_code': column.zip_code,
                'country': column.country,
                'job_offer_description': column.job_offer_description,
                'job_offer_status': column.job_offer_status,
                'interview_info_id': column.interview_info_id,
                'company_id': column.company_id
            }
        }


@router.put('/reject/{id}')
async def reject(id: int, db: Session = Depends(get_db)):

    column = db.query(Job_Offer).filter(Job_Offer.job_offer_id == id).first()

    if column:
        column.job_offer_status = 'Rejected'
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Job Offer Canceled',
            'data': {
                'offered_to': column.offered_to,
                'job_title': column.job_title,
                'job_position': column.job_position,
                'salary': column.salary,
                'city': column.city,
                'region': column.region,
                'zip_code': column.zip_code,
                'country': column.country,
                'job_offer_description': column.job_offer_description,
                'job_offer_status': column.job_offer_status,
                'interview_info_id': column.interview_info_id,
                'company_id': column.company_id
            }
        }


@router.get('/most_recent/{id}')
async def get_all(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Offer).filter(
        Job_Offer.offered_to == id).filter(Job_Offer.job_offer_status == 'Pending').order_by(Job_Offer.created_at.desc()).first()
    return data