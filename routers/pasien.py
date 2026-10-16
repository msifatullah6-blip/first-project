from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db

router = APIRouter(
    prefix='/pasien',
    tags=['Pasien']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponePasien)
def create_pasien(request: schemas.CreatePasien, db: Session = Depends(get_db)):
    new_pasien = models.Pasien(**request.dict())

    db.add(new_pasien)
    db.commit()
    db.refresh(new_pasien)

    return new_pasien

@router.get('/', response_model=List[schemas.ResponePasien])
def get_all_pasien(db: Session = Depends(get_db)):
    pasien = db.query(models.Pasien).all()

    return pasien

@router.get('/{id}', response_model=schemas.ResponePasien, status_code=status.HTTP_200_OK)
def get_id_pasien(id: str, db: Session = Depends(get_db)):
    pasien = db.query(models.Pasien).filter(models.Pasien.id_pasien == id).first()

    if pasien is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pasien Tidak Ditemukan.'
        )

    return pasien

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_pasien(id: str, db: Session = Depends(get_db)):
    pasien = db.query(models.Pasien).filter(models.Pasien.id_pasien == id)

    if pasien.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pasien Tidak Ditemukan.'
        )

    pasien.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponePasien)
def upd_pasien(id: str, data: schemas.CreatePasien, db: Session = Depends(get_db)):
    pasien = db.query(models.Pasien).filter(models.Pasien.id_pasien == id)

    if pasien.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pasien Tidak Ditemukan.'
        )

    pasien.update(data.dict(), synchronize_session=False)
    db.commit()

    return pasien.first()