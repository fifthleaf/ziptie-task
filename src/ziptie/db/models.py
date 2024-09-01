from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import SmallInteger, String

from ziptie.db import Base


class Teacher(Base):
    """
    Represents a teacher entity.

        Attributes:
            id: The unique identifier of the teacher.
            fullname: The full name of the teacher.
            classroom: The classroom number of the teacher.
            subject: The subject taught by the teacher.
            principal: Whether the teacher is a principal or not
    """

    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(30))
    classroom: Mapped[int] = mapped_column(SmallInteger)
    subject: Mapped[str] = mapped_column(String(30))
    principal: Mapped[Optional[bool]]
