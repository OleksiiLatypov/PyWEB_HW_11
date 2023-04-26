from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import crud
from src.schemas import ResponseContact, ContactModel

router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get('/all', response_model=List[ResponseContact])
async def get_contacts(db: Session = Depends(get_db)):
    contacts = await crud.get_contacts(db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contacts


@router.get('/{contact_id}', response_model=ResponseContact)
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await crud.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact with this id not found')
    return contact


@router.post('/create', response_model=ResponseContact)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    new_contact = await crud.create_contact(body, db)
    return new_contact


@router.put('/update/{contact_id}', response_model=ResponseContact)
async def update_contact(body: ContactModel, contact_id: int, db: Session = Depends(get_db)):
    contact = await crud.update_contact(body, contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.delete('/delete/{contact_id}', response_model=ResponseContact)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await crud.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.get("/birthday", response_model=List[ResponseContact])
async def birthday_list(db: Session = Depends(get_db)):
    contacts = await crud.get_birthday(db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts


@router.get("/search/{part_to_search}", response_model=List[ResponseContact])
async def searcher(part_to_search: str = Path(min_length=2, max_length=15), db: Session = Depends(get_db)):
    contacts = await crud.search_contact(part_to_search, db)
    if len(contacts) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts
