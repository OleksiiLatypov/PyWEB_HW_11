from datetime import date, timedelta, datetime
from pprint import pprint
from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactModel
from src.database.db import SessionLocal
import asyncio

database = SessionLocal()


async def get_contacts(db: Session):
    contacts = db.query(Contact).all()
    return contacts


async def get_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def create_contact(body: ContactModel, db: Session):
    new_contact = Contact(name=body.name, lastname=body.lastname, email=body.email, phone=body.phone,
                          birthday=body.birthday, additional_info=body.additional_info)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


async def update_contact(body: ContactModel, contact_id, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.name = body.name
        contact.lastname = body.lastname
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.additional_info = body.additional_info
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_birthday(db: Session):
    current_day = date.today()
    next_week = [(current_day + timedelta(i)).strftime('%B %d') for i in range(7)]
    list_of_contacts = [contact for contact in await get_contacts(db) if
                        contact.birthday.date().strftime('%B %d') in next_week]
    return list_of_contacts


async def search_contact(search_word: str, db: Session):
    result = []
    all_contacts = db.query(Contact).all()
    for contact in all_contacts:
        if search_word in contact.name:
            result.append(contact)
        if search_word in contact.lastname:
            result.append(contact)
        if search_word in contact.email:
            result.append(contact)
    return result

# if __name__ == '__main__':
# pprint(asyncio.run(get_contacts(database)))
# pprint(asyncio.run(get_contact(4, database)))
# pprint(asyncio.run(create_contact(
#     Contact(name='Draco', lastname='Malfoy', email='draco.malfoy@gmail.com', phone='+380670901111',
#             birthday=date(2000, 4, 26),
#             additional_info='my sister'), database)))
# pprint(asyncio.run(
#     update_contact(Contact(name='Ron', lastname='Wisley', email='ron.wisley@gmail.com', phone='+380630002233',
#                            birthday=date(1990, 2, 20),
#                            additional_info='Simple info'), 8, database)))
# pprint((asyncio.run(remove_contact(4, database))))
# pprint(asyncio.run(get_birthday(database)))
# pprint(asyncio.run(search_contact('latypov.oleksii.la@gmail.com', database)))
