from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

from models import Candidate_Profile
from schemas import Candidate_Profile_Form, Login_Form
from oauth2 import get_current_user

router = APIRouter(
    prefix='/candidate_profile',
    tags=['Candidate_Profile']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Profile).all()

    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Profile_Form, db: Session = Depends(get_db)):
    column = Candidate_Profile(
        user_account_id=req.user_account_id,
        candidate_type=req.candidate_type,
        first_name=req.first_name,
        middle_name=req.middle_name,
        last_name=req.last_name,
        suffix_name=req.suffix_name,
        full_name=req.first_name + " " + req.middle_name + " " + req.last_name,
        age=req.age,
        gender=req.gender,
        birth_date=req.birth_date,
        zip_code=req.zip_code,
        city=req.city,
        region=req. region,
        country=req.country,
        nationality=req.nationality,
        review_status=req.review_status,
        candidate_image=req.candidate_image
    )

    db.add(column)
    db.commit()

    column.created_by = column.candidate_profile_id
    column.updated_by = column.candidate_profile_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Candidate_Profile info created.',
        'data': {
            'candidate_profile_id': column.candidate_profile_id,
            'candidate_type': column.candidate_type,
            'first_name': column.first_name,
            'middle_name': column.middle_name,
            'last_name': column.last_name,
            'suffix_name': column.suffix_name,
            'age': column.age,
            'gender': column.gender,
            'birth_date': column.birth_date,
            'zip_code': column.zip_code,
            'city': column.city,
            'region': column. region,
            'country': column.country,
            'nationality': column.nationality,
            'candidate_image': column.candidate_image,
            'review_status': column.review_status,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Profile_Form, db: Session = Depends(get_db)
                 # , current_user: Login_Form = Depends(get_current_user)
                 ):
    column = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()

    if column:
        column.candidate_type = req.candidate_type
        column.first_name = req.first_name
        column.middle_name = req.middle_name
        column.last_name = req.last_name
        column.suffix_name = req.suffix_name
        column.full_name = req.first_name + " " + req.middle_name + " " + req.last_name
        column.age = req.age
        column.gender = req.gender
        column.birth_date = req.birth_date
        column.zip_code = req.zip_code
        column.city = req.city
        column.region = req. region
        column.country = req.country
        column.nationality = req.nationality
        column.candidate_image = req.candidate_image
        column.review_status = req.review_status
        column.updated_at = datetime.now()

        db.commit()
        return {
            'msg': 'Candidate_Profile info updated.',
            'data': {
                'candidate_type': column.candidate_type,
                'first_name': column.first_name,
                'middle_name': column.middle_name,
                'last_name': column.last_name,
                'suffix_name': column.suffix_name,
                'age': column.age,
                'gender': column.gender,
                'birth_date': column.birth_date,
                'zip_code': column.zip_code,
                'city': column.city,
                'region': column. region,
                'country': column.country,
                'nationality': column.nationality,
                'candidate_image': column.candidate_image,
                'review_status': column.review_status,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'Candidate does not exist.'
    }


@router.put('/transfer/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()

    if column:
        column.review_status = 'Transferred'
        db.commit()
        return {
            'msg': 'Candidate Transferred'
        }


@router.put('/todirecthire/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()

    if column:
        column.candidate_type = 'Direct Hire'
        db.commit()
        return {
            'msg': 'Candidate set to Direct Hire'
        }


@router.put('/toagency/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()

    if column:
        column.candidate_type = 'Agency'
        db.commit()
        return {
            'msg': 'Candidate set to Agency'
        }


@router.put('/grantaccess/{id}')
async def update(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Profile).filter(
        Candidate_Profile.user_account_id == id).first()

    if column:
        column.review_status = 'Active'
        db.commit()
        return {
            'msg': 'Candidate Activated'
        }
