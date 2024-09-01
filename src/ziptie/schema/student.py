from pydantic import BaseModel, Field


class StudentRequest(BaseModel):
    """
    Represents a request to create or update a student.

        Attributes:
            fullname: The full name of the student.
            major: The major of the student.
            gpa: The grade point average of the student.
            teacher_id: The ID of the teacher who teaches the student.
    """

    fullname: str = Field(max_length=30)
    major: str = Field(max_length=30)
    gpa: float = Field(ge=1, le=5)
    teacher_id: int = Field(ge=1)


class StudentResponseData(StudentRequest):
    """
    Represents the data returned in a student response.

        Attributes:
            id: The unique identifier of the student.
            fullname: The full name of the student.
            major: The major of the student.
            gpa: The grade point average of the student.
            teacher_id: The ID of the teacher who teaches the student.
    """

    id: int = Field(ge=1)

    class Config:
        """
        Configuration class for Pydantic model.

            Attributes:
                from_attributes: Whether to create the object from attributes.
        """

        from_attributes = True


class StudentResponse(BaseModel):
    """
    Represents a response to a student-related request.

        Attributes:
            message: A message describing the outcome of the request.
            data: The student data returned in the response.
    """

    message: str = Field(max_length=100)
    data: StudentResponseData
