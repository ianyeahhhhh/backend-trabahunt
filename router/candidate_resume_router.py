from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Resume
from oauth2 import get_current_user
from schemas import Candidate_Resume_Form, Login_Form


router = APIRouter(
    prefix='/candidate_resume',
    tags=['Candidate_Resume']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Resume).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = data = db.query(Candidate_Resume).filter(
        Candidate_Resume.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Candidate_Resume_Form, db: Session = Depends(get_db)):
    column = Candidate_Resume(
        user_account_id=req.user_account_id,
        resume=req.resume
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'Resume Added.',
        'data': {
            'user_account_id': column.user_account_id,
            'resume': column.resume
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Candidate_Resume_Form, db: Session = Depends(get_db)
                 # , current_user: Login_Form = Depends(get_current_user)
                 ):
    data = db.query(Candidate_Resume).filter(
        Candidate_Resume.user_account_id == id).first()

    if data:
        data.user_account_id = req.user_account_id
        data.resume = req.resume
        db.commit()

        return {
            'msg': 'Resume Updated',
            'data': {
                'user_account_id': data.user_account_id,
                'resume': data.resume
            }
        }
    return {
        'msg': 'User Account Not Found.'
    }
