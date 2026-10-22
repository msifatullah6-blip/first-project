from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/dokter',
    tags=['Dokter'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponeDokter)
def create_dokter(request: schemas.CreateDokter, db: Session = Depends(get_db)):
    new_dokter = models.Dokter(**request.dict())

    db.add(new_dokter)
    db.commit()
    db.refresh(new_dokter)

    return new_dokter

@router.get('/', response_model=List[schemas.ResponeDokter])
def get_all_dokter(db: Session = Depends(get_db)):
    dokter = db.query(models.Dokter).all()

    return dokter

@router.get('/{id}', response_model=schemas.ResponeDokter, status_code=status.HTTP_200_OK)
def get_id_dokter(id: str, db: Session = Depends(get_db)):
    dokter = db.query(models.Dokter).filter(models.Dokter.id_dokter == id).first()

    if dokter is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Dokter Tidak Ditemukan.'
        )

    return dokter

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_dokter(id: str, db: Session = Depends(get_db)):
    dokter = db.query(models.Dokter).filter(models.Dokter.id_dokter == id)

    if dokter.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Dokter Tidak Ditemukan.'
        )

    dokter.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponeDokter)
def upd_dokter(id: str, data: schemas.CreateDokter, db: Session = Depends(get_db)):
    dokter = db.query(models.Dokter).filter(models.Dokter.id_dokter == id)

    if dokter.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Dokter Tidak Ditemukan.'
        )

    dokter.update(data.dict(), synchronize_session=False)
    db.commit()

    return dokter.first()