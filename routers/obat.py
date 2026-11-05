from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/obat',
    tags=['Obat'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponeObat)
def create_obat(request: schemas.CreateObat, db: Session = Depends(get_db)):
    new_obat = models.Obat(**request.dict())

    db.add(new_obat)
    db.commit()
    db.refresh(new_obat)

    return new_obat

@router.get('/', response_model=List[schemas.ResponeObat])
def get_all_obat(db: Session = Depends(get_db)):
    obat = db.query(models.Obat).all()

    return obat

@router.get('/{id}', response_model=schemas.ResponeObat, status_code=status.HTTP_200_OK)
def get_id_obat(id: str, db: Session = Depends(get_db)):
    obat = db.query(models.Obat).filter(models.Obat.id_obat == id).first()

    if obat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Obat Tidak Ditemukan.'
        )

    return obat

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_obat(id: str, db: Session = Depends(get_db)):
    obat = db.query(models.Obat).filter(models.Obat.id_obat == id)

    if obat.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Obat Tidak Ditemukan.'
        )

    obat.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponeObat)
def upd_obat(id: str, data: schemas.CreateObat, db: Session = Depends(get_db)):
    obat = db.query(models.Obat).filter(models.Obat.id_obat == id)

    if obat.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Obat Tidak Ditemukan.'
        )

    obat.update(data.dict(), synchronize_session=False)
    db.commit()

    return obat.first()