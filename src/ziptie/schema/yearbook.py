from pydantic import BaseModel, Field


class YearbookResponseData(BaseModel):
    """
    Represents a single entry in the yearbook data.

        Attributes:
            student: The full name of the student.
            major: The major of the student.
            teacher: The full name of the teacher.
            classroom: The classroom number of the teacher.
    """

    student: str = Field(max_length=30)
    major: str = Field(max_length=30)
    teacher: str = Field(max_length=30)
    classroom: int = Field(ge=1, le=20)

    class Config:
        """
        Configuration class for Pydantic model.

            Attributes:
                from_attributes: Whether to create the object from attributes.
        """

        from_attributes = True


class YearbookResponse(BaseModel):
    """
    Represents a response to a yearbook-related request.

        Attributes:
            message: A message describing the outcome of the request.
            data: The yearbook data returned in the response.
    """

    message: str = Field(max_length=100)
    data: list[YearbookResponseData]
