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


class TeacherResponseData(TeacherRequest):
    """
    Represents the data returned in a teacher response.

        Attributes:
            id: The unique identifier of the teacher.
            fullname: The full name of the teacher.
            classroom: The classroom number of the teacher.
            subject: The subject taught by the teacher.
            principal: Whether the teacher is a principal or not.
    """

    id: int = Field(ge=1)

    class Config:
        """
        Configuration class for Pydantic model.

            Attributes:
                from_attributes: Whether to create the object from attributes.
        """

        from_attributes = True


class TeacherResponse(BaseModel):
    """
    Represents a response to a teacher-related request.

        Attributes:
            message: A message describing the outcome of the request.
            data: The teacher data returned in the response.
    """

    message: str = Field(max_length=100)
    data: TeacherResponseData
