from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/poli',
    tags=['Poli'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponePoli)
def create_poli(request: schemas.CreatePoli, db: Session = Depends(get_db)):
    new_poli = models.Poli(**request.dict())

    db.add(new_poli)
    db.commit()
    db.refresh(new_poli)

    return new_poli

@router.get('/', response_model=List[schemas.ResponePoli])
def get_all_poli(db: Session = Depends(get_db)):
    poli = db.query(models.Poli).all()

    return poli

@router.get('/{id}', response_model=schemas.ResponePoli, status_code=status.HTTP_200_OK)
def get_id_poli(id: str, db: Session = Depends(get_db)):
    poli = db.query(models.Poli).filter(models.Poli.id_poli == id).first()

    if poli is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Poli Tidak Ditemukan.'
        )

    return poli

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_poli(id: str, db: Session = Depends(get_db)):
    poli = db.query(models.Poli).filter(models.Poli.id_poli == id)

    if poli.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Poli Tidak Ditemukan.'
        )

    poli.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponePoli)
def upd_poli(id: str, data: schemas.CreatePoli, db: Session = Depends(get_db)):
    poli = db.query(models.Poli).filter(models.Poli.id_poli == id)

    if poli.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Poli Tidak Ditemukan.'
        )

    poli.update(data.dict(), synchronize_session=False)
    db.commit()

    return poli.first()