from datetime import datetime
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash

from models import Employee_Info
from oauth2 import get_current_user
from schemas import Login_Form, Employee_Info_Form
router = APIRouter(
    prefix='/employee_info',
    tags=['Employee_Info']
)


# GET ALL EMPLOYEE INFO
@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    data = db.query(Employee_Info).all()
    return data


# GET ALL EMPLOYEE INFO FOR A SPECIFIC COMPANY FOR DATATABLE
@router.get('/{id}')
async def get_all(id:int, db: Session = Depends(get_db)):
    data = db.query(Employee_Info).filter(Employee_Info.hired_by == id).all()
    return data


# GET ALL EMPLOYEE INFO FOR A SPECIFIC COMPANY FOR VIEWING
@router.get('/get_one/{id}')
async def get_all(id:int, db: Session = Depends(get_db)):
    data = db.query(Employee_Info).filter(Employee_Info.employee_id == id).first()
    return data


# GET SPECIFIC EMPLOYEE INFO
@router.get('/get_one/{id}')
async def get_one(id: int, db: Session = Depends(get_db)):
    data = db.query(Employee_Info).filter(
        Employee_Info.employee_id == id).first()
    return data


# post or create
@router.post('/')
async def create(req: Employee_Info_Form, db: Session = Depends(get_db)):
    column = Employee_Info(
        full_name=req.full_name,
        position=req.position,
        hired_by=req.hired_by,
        candidate_personal_info_id=req.candidate_personal_info_id
    )
    db.add(column)
    db.commit()

    column.created_by = column.hired_by
    column.updated_by = column.hired_by
    column.hired_by = column.hired_by
    column.created_at = datetime.now()
    column.updated_at = datetime.now()
    db.commit()

    return {
        'msg': 'Employee Hired ',
        'data': {
            'candidate_personal_info_id': column.candidate_personal_info_id,
            'employee_id': column.employee_id,
            'full_name': column.full_name,
            'position': column.position,
            'hired_by': column.hired_by,
            'created_by': column.hired_by,
            'updated_by': column.hired_by,
            'hired_by': column.hired_by,
            'created_at': column.created_at,
            'updated_at': column.updated_at
        }
    }
