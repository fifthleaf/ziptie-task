from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

from ziptie.db import Student, Teacher
from ziptie.schema import YearbookResponseData


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


def get_data(session: Session, query: Select) -> list[YearbookResponseData]:
    """
    Executes a database query and returns the yearbook results.

        Args:
            session: The database session to use for the query.
            query: The SQL query to execute.

        Returns:
            A yearbook rows representing the query results.
    """
    try:
        result = session.execute(query).mappings().all()
        if not result:
            raise HTTPException(status_code=404, detail="Not found")
        return [YearbookResponseData.from_orm(row) for row in result]
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=500, detail="Database error") from exc
