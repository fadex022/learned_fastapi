from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas, models
from ..utils import Hasher
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('/create_users', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):

    payload.password = Hasher(payload.password)
    new_user = models.User(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    
    return user