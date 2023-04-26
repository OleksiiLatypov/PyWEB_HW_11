from faker import Faker
from sqlalchemy.orm import Session
from src.database.db import SessionLocal
from src.database.models import Contact
from src.schemas import ContactModel

fake = Faker()

database = SessionLocal()


def create_contact(contact: ContactModel, db: Session = SessionLocal):
    contact = Contact(name=contact.name, lastname=contact.lastname, email=contact.email, phone=contact.phone,
                      birthday=contact.birthday, additional_info=contact.additional_info)
    print(contact, db)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


if __name__ == '__main__':
    for i in range(10):
        new_contact = Contact(
            name=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(),
            phone=fake.msisdn(),
            birthday=fake.date(),
            additional_info=fake.paragraph()
        )
        create_contact(contact=new_contact, db=database)
