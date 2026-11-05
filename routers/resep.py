from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db
from security import get_current_user

router = APIRouter(
    prefix='/resep',
    tags=['Resep'],
    dependencies=[Depends(get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponeResep)
def create_resep(request: schemas.CreateResep, db: Session = Depends(get_db)):
    new_resep = models.Resep(**request.dict())

    db.add(new_resep)
    db.commit()
    db.refresh(new_resep)

    return new_resep

@router.get('/', response_model=List[schemas.ResponeResep])
def get_all_resep(db: Session = Depends(get_db)):
    resep = db.query(models.Resep).all()

    return resep

@router.get('/{id}', response_model=schemas.ResponeResep, status_code=status.HTTP_200_OK)
def get_id_resep(id: str, db: Session = Depends(get_db)):
    resep = db.query(models.Resep).filter(models.Resep.id_resep == id).first()

    if resep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Resep Tidak Ditemukan.'
        )

    return resep

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_resep(id: str, db: Session = Depends(get_db)):
    resep = db.query(models.Resep).filter(models.Resep.id_resep == id)

    if resep.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Resep Tidak Ditemukan.'
        )

    resep.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', response_model=schemas.ResponeResep)
def upd_resep(id: str, data: schemas.CreateResep, db: Session = Depends(get_db)):
    resep = db.query(models.Resep).filter(models.Resep.id_resep == id)

    if resep.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Resep Tidak Ditemukan.'
        )

    resep.update(data.dict(), synchronize_session=False)
    db.commit()

    return resep.first()