from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Candidate_Personal_Information, Candidate_Character_References, Candidate_Education
from models import Candidate_Emergency_Contact, Candidate_Family_Background, Candidate_Job_History
from models import Candidate_Experience_Detail, Candidate_Resume

router = APIRouter(
    prefix='/fetch_candidate',
    tags=['Fetch_Candidate']
)


# get all
@router.get('/{id}')
async def get_all(id: int, db: Session = Depends(get_db)):
    data = db.query(Candidate_Personal_Information).filter(Candidate_Personal_Information.user_account_id == id).first()
    data1 = db.query(Candidate_Job_History).filter(Candidate_Job_History.user_account_id == id).first()
    data2 = db.query(Candidate_Education).filter(Candidate_Education.user_account_id == id).first()
    data3 = db.query(Candidate_Family_Background).filter(Candidate_Family_Background.user_account_id == id).first()
    data4 = db.query(Candidate_Experience_Detail).filter(Candidate_Experience_Detail.user_account_id == id).first()
    data5 = db.query(Candidate_Character_References).filter(Candidate_Character_References.user_account_id == id).first()
    data6 = db.query(Candidate_Emergency_Contact).filter(Candidate_Emergency_Contact.user_account_id == id).first()
    data7 = db.query(Candidate_Resume).filter(Candidate_Resume.user_account_id == id).first()

    return data, data1, data2, data3, data4, data5, data6, data7