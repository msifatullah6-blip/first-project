from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/kunjung',
    tags=['Kunjung'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponeKunjung)
def create_kunjung(request: schemas.CreateKunjung, db: Session = Depends(get_db)):
    new_kunjung = models.Kunjung(**request.dict())

    db.add(new_kunjung)
    db.commit()
    db.refresh(new_kunjung)

    return new_kunjung

@router.get('/', response_model=List[schemas.ResponeKunjung])
def get_all_kunjung(db: Session = Depends(get_db)):
    kunjung = db.query(models.Kunjung).all()

    return kunjung

@router.get('/{id}', response_model=schemas.ResponeKunjung, status_code=status.HTTP_200_OK)
def get_id_kunjung(id: str, db: Session = Depends(get_db)):
    kunjung = db.query(models.Kunjung).filter(models.Kunjung.id_kunjung == id).first()

    if kunjung is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Kunjung Tidak Ditemukan.'
        )

    return kunjung

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_kunjung(id: str, db: Session = Depends(get_db)):
    kunjung = db.query(models.Kunjung).filter(models.Kunjung.id_kunjung == id)

    if kunjung.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Kunjung Tidak Ditemukan.'
        )

    kunjung.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponeKunjung)
def upd_kunjung(id: str, data: schemas.CreateKunjung, db: Session = Depends(get_db)):
    kunjung = db.query(models.Kunjung).filter(models.Kunjung.id_kunjung == id)

    if kunjung.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Kunjung Tidak Ditemukan.'
        )

    kunjung.update(data.dict(), synchronize_session=False)
    db.commit()

    return kunjung.first()