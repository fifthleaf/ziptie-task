from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import Numeric, SmallInteger, String

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

        Relationships:
            students: The list of students taught by the teacher.
    """

    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(30))
    classroom: Mapped[int] = mapped_column(SmallInteger)
    subject: Mapped[str] = mapped_column(String(30))
    principal: Mapped[Optional[bool]]

    students: Mapped[list["Student"]] = relationship(back_populates="teacher")


class Student(Base):
    """
    Represents a student entity.

        Attributes:
            id: The unique identifier of the student.
            fullname: The full name of the student.
            major: The major of the student.
            gpa: The grade point average of the student.
            teacher_id: The ID of teacher who teaches the student.

        Relationships:
            teacher: The teacher who teaches the student.
    """

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(30))
    major: Mapped[str] = mapped_column(String(30))
    gpa: Mapped[float] = mapped_column(Numeric(4, 2))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))

    teacher: Mapped["Teacher"] = relationship(back_populates="students")
