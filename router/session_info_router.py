from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Session_Info
from oauth2 import get_current_user
from schemas import Session_Info_Form


router = APIRouter(
    prefix='/session_info',
    tags=['Session_Info']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Session_Info).all()
    return data


@router.post('/')
async def create(req: Session_Info_Form, db: Session = Depends(get_db)):
    column = Session_Info(
        user_account_id=req.user_account_id,
        time_of_login=req.time_of_login,
        time_of_logout=req.time_of_logout
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'Session Info Added.',
        'data': {
            'session_info_id': column.session_info_id,
            'user_account_id': column.user_account_id,
            'time_of_login': column.time_of_login,
            'time_of_logout': column.time_of_logout
        }
    }


@router.put('/{id}')
async def update(id: int, req: Session_Info_Form, db: Session = Depends(get_db)):
    data = db.query(Session_Info).filter(
        Session_Info.session_info_id == id).first()

    if data:
        data.user_account_id = req.user_account_id,
        data.time_of_login = req.time_of_login,
        data.time_of_logout = req.time_of_logout
        db.commit()

        return {
            'msg': 'Session Info Updated',
            'data': {
                'session_info_id': data.session_info_id,
                'user_account_id': data.user_account_id,
                'time_of_login': data.time_of_login,
                'time_of_logout': data.time_of_logout
            }
        }
    return {
        'msg': 'Session Info does not exist.'
    }

