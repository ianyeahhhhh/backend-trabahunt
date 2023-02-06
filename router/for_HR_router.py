from datetime import date, datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Personal_Information
from oauth2 import get_current_user
from schemas import Candidate_Personal_Information_Form

router = APIRouter(
    prefix='/for_HR',
    tags=['for_HR']
)

@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Candidate_Personal_Information).filter(Candidate_Personal_Information.candidate_type == 'Agency').filter(Candidate_Personal_Information.review_status == 'Active').all()

    return data


@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Personal_Information).filter(
        Candidate_Personal_Information.candidate_type == 'Agency'
        ).filter(
            Candidate_Personal_Information.review_status == 'Active'
            ).filter(
                Candidate_Personal_Information.user_account_id == id
            ).first()
    
    return data
