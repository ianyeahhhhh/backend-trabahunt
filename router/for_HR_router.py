from datetime import date, datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Profile
from oauth2 import get_current_user
from schemas import Candidate_Profile_Form

router = APIRouter(
    prefix='/for_HR',
    tags=['for_HR']
)

@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Profile).filter(Candidate_Profile.candidate_type == 'Agency').filter(Candidate_Profile.review_status == 'Active').all()

    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Profile).filter(
        Candidate_Profile.candidate_type == 'Agency'
        ).filter(
            Candidate_Profile.review_status == 'Active'
            ).filter(
                Candidate_Profile.user_account_id == id
            ).first()
    
    return data
