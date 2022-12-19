from datetime import datetime
from fastapi import APIRouter, Depends

from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Files
from oauth2 import get_current_user
from schemas import Files_Form

router = APIRouter(
    prefix='/files',
    tags=['Files']
)


@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Files).all()
    return data

@router.post('/')
async def create(req: str, db: Session = Depends(get_db)):
    column = Files(
        # file_name=req
    )
    db.add(column)
    db.commit()

    return {
        'msg': 'File info created',
        'data': {
            'file_name': column.file_name
        }
    }