from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Job_Location
from oauth2 import get_current_user
from schemas import Login_Form, Job_Location_Form
router = APIRouter(
    prefix='/job_location',
    tags=['Job_Location']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Job_Location).all()
    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Job_Location).filter(
        Job_Location.job_post_id == id).first()
    return data


@router.post('/')
async def create(req: Job_Location_Form, db: Session = Depends(get_db)):
    column = Job_Location(
        city=req.city,
        region=req.region,
        country=req.country,
        zip_code=req.zip_code,
        job_post_id=req.job_post_id
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'Job Location info created.',
        'data': {
            'job_location_id': column.job_location_id,
            'city': column.city,
            'region': column.region,
            'country': column.country,
            'zip_code': column.zip_code,
            'job_post_id': column.job_post_id
        }
    }


@router.put('/{id}')
async def update(id: int, req: Job_Location_Form, db: Session = Depends(get_db)):
    column = db.query(Job_Location).filter(
        Job_Location.job_location_id == id).first()

    if column:
        column.city = req.city
        column.region = req.region
        column.country = req.country
        column.zip_code = req.zip_code
        column.job_post_id = req.job_post_id
        db.commit()

        return {
            'msg': 'Job Location info updated.',
            'data': {
                'job_location_id': column.job_location_id,
                'city': column.city,
                'region': column.region,
                'country': column.country,
                'zip_code': column.zip_code,
                'job_post_id': column.job_post_id
            }
        }
    return {
        'msg': 'Job Location Info cannot be found.'
    }
