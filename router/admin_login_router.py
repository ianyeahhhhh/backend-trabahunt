from fastapi import APIRouter, Depends
import database, models, main
from sqlalchemy.orm import Session
from hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/admin_login',
    tags=['Admin_Login']
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Admin_Profile).filter(
        models.Admin_Profile.email == request.username).first()
    if user:
        if user.admin_status == 'Active':
            if Hash.verify(user.password, request.password):
                access_token = main.create_access_token(
                    data={"sub": user.email})
                return {
                    "access_token": access_token,
                    "token_type": "bearer",
                    "data": user
                }   
            return {'msg': 'Invalid Password.'}
        return {'msg': 'Admin is Inactive.'}
    return {'msg': 'Invalid Email.'}
