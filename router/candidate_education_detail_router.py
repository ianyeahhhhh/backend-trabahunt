from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

from models import Candidate_Education_Detail
from schemas import Candidate_Education_Detail_Form, Login_Form
from oauth2 import get_current_user

router = APIRouter(
    prefix='/candidate_education_detail',
    tags=['Candidate_Education_Detail']
)


# get all rows
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Education_Detail).all()

    return data


# get one info
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Education_Detail).filter(
        Candidate_Education_Detail.user_account_id == id).first()
    return data


# get one hired candidate info
@router.get('/hired/{id}')
async def get_one_when_hired(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Education_Detail).filter(
        Candidate_Education_Detail.candidate_education_detail_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Education_Detail_Form, db: Session = Depends(get_db)):
    column = Candidate_Education_Detail(
        user_account_id=req.user_account_id,
        institute_university_name=req.institute_university_name,
        highest_education_attainment=req.highest_education_attainment,
        institute_university_location=req.institute_university_location,
        field_of_study=req.field_of_study,
        major=req.major,
        graduation_date=req.graduation_date
    )

    db.add(column)
    db.commit()

    column.created_by = column.candidate_education_detail_id
    column.updated_by = column.candidate_education_detail_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Candidate_Education_Detail info created.',
        'data': {
            'institute_university_name': column.institute_university_name,
            'highest_education_attainment': column.highest_education_attainment,
            'institute_university_location': column.institute_university_location,
            'field_of_study': column.field_of_study,
            'major': column.major,
            'graduation_date': column.graduation_date,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


# update an info
@router.put('/{id}')
async def update(id: int, req: Candidate_Education_Detail_Form, db: Session = Depends(get_db)
                 # , current_user: Login_Form = Depends(get_current_user)
                 ):
    column = db.query(Candidate_Education_Detail).filter(
        Candidate_Education_Detail.user_account_id == id).first()

    if column:
        column.institute_university_name = req.institute_university_name
        column.highest_education_attainment = req.highest_education_attainment
        column.institute_university_location = req.institute_university_location
        column.field_of_study = req.field_of_study
        column.major = req.major
        column.graduation_date = req.graduation_date
        column.updated_at = datetime.now()

        db.commit()
        return {
            'msg': 'Candidate_Education_Detail info updated.',
            'data': {
                'candidate_education_detail_id': column.candidate_education_detail_id,
                'institute_university_name': column.institute_university_name,
                'highest_education_attainment': column.highest_education_attainment,
                'institute_university_location': column.institute_university_location,
                'field_of_study': column.field_of_study,
                'major': column.major,
                'graduation_date': column.graduation_date,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'Candidate Education Detail not found.'
    }
