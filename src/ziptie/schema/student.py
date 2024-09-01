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
