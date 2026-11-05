from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/periksa',
    tags=['Periksa'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponePeriksa)
def create_periksa(request: schemas.CreatePeriksa, db: Session = Depends(get_db)):
    new_periksa = models.Periksa(**request.dict())

    db.add(new_periksa)
    db.commit()
    db.refresh(new_periksa)

    return new_periksa

@router.get('/', response_model=List[schemas.ResponePeriksa])
def get_all_periksa(db: Session = Depends(get_db)):
    periksa = db.query(models.Periksa).all()

    return periksa

@router.get('/{id}', response_model=schemas.ResponePeriksa, status_code=status.HTTP_200_OK)
def get_id_periksa(id: str, db: Session = Depends(get_db)):
    periksa = db.query(models.Periksa).filter(models.Periksa.id_periksa == id).first()

    if periksa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Periksa Tidak Ditemukan.'
        )

    return periksa

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_periksa(id: str, db: Session = Depends(get_db)):
    periksa = db.query(models.Periksa).filter(models.Periksa.id_periksa == id)

    if periksa.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Periksa Tidak Ditemukan.'
        )

    periksa.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponePeriksa)
def upd_periksa(id: str, data: schemas.CreatePeriksa, db: Session = Depends(get_db)):
    periksa = db.query(models.Periksa).filter(models.Periksa.id_periksa == id)

    if periksa.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Periksa Tidak Ditemukan.'
        )

    periksa.update(data.dict(), synchronize_session=False)
    db.commit()

    return periksa.first()