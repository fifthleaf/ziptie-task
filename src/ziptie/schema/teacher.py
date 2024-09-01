from typing import Optional

from pydantic import BaseModel, Field


class TeacherRequest(BaseModel):
    """
    Represents a request to create or update a teacher.

        Attributes:
            fullname: The full name of the teacher.
            classroom: The classroom number of the teacher.
            subject: The subject taught by the teacher.
            principal: Whether the teacher is a principal or not.
    """

    fullname: str = Field(max_length=30)
    classroom: int = Field(ge=1, le=20)
    subject: str = Field(max_length=30)
    principal: Optional[bool] = Field(default=None)
