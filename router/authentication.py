from fastapi import APIRouter, Depends
import database, models, main
from sqlalchemy.orm import Session
from hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/login',
    tags=['User_Login']
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User_Account).filter(
        models.User_Account.email == request.username).first()
    if user:
        if user.account_status == 'Active':
            if Hash.verify(user.password, request.password):
                access_token = main.create_access_token(
                    data={"sub": user.email})
                return {
                    "access_token": access_token,
                    "token_type": "bearer",
                    "data": user
                }   
            return {'msg': 'Invalid Password.'}
        return {'msg': 'User is Inactive.'}
    return {'msg': 'Invalid Email.'}
