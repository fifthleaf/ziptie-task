from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ziptie.db import Student, Teacher


def insert_data(session: Session, item: Teacher | Student):
    """
    Inserts a teacher or student into the database.

        Args:
            session: The database session to use for the insertion.
            item: The teacher or student to insert.
    """
    try:
        session.add(item)
        session.commit()
        session.refresh(item)
    except SQLAlchemyError as exc:
        session.rollback()
        raise HTTPException(status_code=500, detail="Database error") from exc
