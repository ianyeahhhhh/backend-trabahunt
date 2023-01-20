from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

from models import Company_Legal_Document
from schemas import Company_Legal_Document_Form, Login_Form
from oauth2 import get_current_user


router = APIRouter(
    prefix='/company_legal_document',
    tags=['Company_Legal_Document']
)


# get all
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Company_Legal_Document).all()
    return data


# get one
@router.get('/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Company_Legal_Document).filter(Company_Legal_Document.user_account_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Company_Legal_Document_Form, db: Session = Depends(get_db)):
    column = Company_Legal_Document(
        user_account_id=req.user_account_id,
        legal_document=req.legal_document
    )
    db.add(column)
    db.commit()

    column.created_by = column.company_legal_document_id
    column.updated_by = column.company_legal_document_id
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Company Legal Document created.',
        'data': {
            'user_account_id': column.user_account_id,
            'legal_document': column.legal_document,
            'created_by': column.created_by,
            'updated_by': column.updated_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }


# update
@router.put('/{id}')
async def update(id: int, req: Company_Legal_Document_Form, db: Session = Depends(get_db)
                # , current_user: Login_Form = Depends(get_current_user)
                ):
    column = db.query(Company_Legal_Document).filter(
        Company_Legal_Document.user_account_id == id).first()

    if column:
        column.user_account_id = req.user_account_id
        column.legal_document = req.legal_document
        column.updated_at = datetime.now()

        db.commit()
        return {
            'msg': 'Company Legal Document updated.',
            'data': {
                'user_account_id': column.user_account_id,
                'legal_document': column.legal_document,
                'updated_by': column.updated_by,
                'updated_at': column.updated_at
            }
        }
    return {
        'msg': 'Company Legal Document ID does not exist.'
    }
