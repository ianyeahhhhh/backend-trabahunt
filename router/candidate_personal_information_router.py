from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Personal_Information
from oauth2 import get_current_user
from schemas import Login_Form, Candidate_Personal_Information_Form

router = APIRouter(
    prefix='/candidate_personal_information',
    tags=['Candidate_Personal_Information']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Personal_Information).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Personal_Information).filter(
        Candidate_Personal_Information.user_account_id == id).first()
    return data


# post or create Candidate Personal Info
@router.post('/')
async def create(req: Candidate_Personal_Information_Form, db: Session = Depends(get_db)):
    column = Candidate_Personal_Information(
        candidate_type=req.candidate_type,
        first_name=req.first_name,
        middle_name=req.middle_name,
        last_name=req.last_name,
        suffix_name=req.suffix_name,
        email=req.email,
        birth_date=req.birth_date,
        sex=req.sex,
        block_number=req.block_number,
        lot_number=req.lot_number,
        street=req.street,
        barangay=req.barangay,
        city=req.city,
        zip_code=req.zip_code,
        region=req.region,
        country=req.country,
        nationality=req.nationality,
        civil_status=req.civil_status,
        review_status=req.review_status,
        candidate_image=req.candidate_image,
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
        'msg': 'Candidate Personal Info created.',
        'data': {
            'candidate_type': column.candidate_type,
            'first_name': column.first_name,
            'middle_name': column.middle_name,
            'last_name': column.last_name,
            'suffix_name': column.suffix_name,
            'email': column.email,
            'birth_date': column.birth_date,
            'sex': column.sex,
            'block_number': column.block_number,
            'lot_number': column.lot_number,
            'street': column.street,
            'barangay': column.barangay,
            'city': column.city,
            'zip_code': column.zip_code,
            'region': column.region,
            'country': column.country,
            'nationality': column.nationality,
            'civil_status': column.civil_status,
            'review_status': column.review_status,
            'candidate_image': column.candidate_image,
            'user_account_id': column.user_account_id,
            'created_by': column.created_by,
            'created_at': column.created_at,
            'updated_by': column.updated_by,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Personal_Information_Form, db: Session = Depends(get_db)):
    column = db.query(Candidate_Personal_Information).filter(
        Candidate_Personal_Information.user_account_id == id).first()

    if column:
        column.candidate_type = req.candidate_type
        column.first_name = req.first_name
        column.middle_name = req.middle_name
        column.last_name = req.last_name
        column.suffix_name = req.suffix_name
        column.email = req.email
        column.birth_date = req.birth_date
        column.sex = req.sex
        column.block_number = req.block_number
        column.lot_number = req.lot_number
        column.street = req.street
        column.barangay = req.barangay
        column.city = req.city
        column.zip_code = req.zip_code
        column.region = req.region
        column.country = req.country
        column.nationality = req.nationality
        column.civil_status = req.civil_status
        column.review_status = req.review_status
        column.candidate_image = req.candidate_image
        column.user_account_id = req.user_account_id
        db.commit()

        column.created_by = column.user_account_id
        column.updated_by = column.user_account_id
        column.created_at = datetime.now()
        column.updated_at = datetime.now()
        db.commit()

        return {
            'msg': 'Candidate Personal Info updated.',
            'data': {
                'candidate_type': column.candidate_type,
                'first_name': column.first_name,
                'middle_name': column.middle_name,
                'last_name': column.last_name,
                'suffix_name': column.suffix_name,
                'email': column.email,
                'birth_date': column.birth_date,
                'sex': column.sex,
                'block_number': column.block_number,
                'lot_number': column.lot_number,
                'street': column.street,
                'barangay': column.barangay,
                'city': column.city,
                'zip_code': column.zip_code,
                'region': column.region,
                'country': column.country,
                'nationality': column.nationality,
                'civil_status': column.civil_status,
                'review_status': column.review_status,
                'candidate_image': column.candidate_image,
                'user_account_id': column.user_account_id,
                'created_by': column.created_by,
                'created_at': column.created_at,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at,
            }
        }
    return {
        'msg': 'User Account cannot be found.'
    }


@router.delete('/{id}')
async def deactivate(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Personal_Information).filter(
        Candidate_Personal_Information.user_account_id == id).first()

    if column:
        if column.review_status == 'Active':
            column.review_status = 'Inactive'

            db.commit()
            return {
                'msg': 'Candidate Account deactivated.',
                'email': column.email
            }
        return {
            'msg': 'Candidate Account is already deactivated.'
        }
    return {
        'msg': 'Candidate Account cannot be found.'
    }


@router.put('/grantaccess/{id}')
async def grantAccess(id: int, db: Session = Depends(get_db)):
    column = db.query(Candidate_Personal_Information).filter(
        Candidate_Personal_Information.user_account_id == id).first()

    if column:
        column.review_status = 'Active'
        db.commit()
        return {
            'msg': 'Candidate Granted Access'
        }
    return {
        'msg': 'candidate not found'
    }