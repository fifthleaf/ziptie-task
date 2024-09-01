from typing import Annotated

from fastapi import Body, FastAPI, HTTPException, Path, Query
from sqlalchemy.sql import select

from . import db, schema, utils

db.Base.metadata.create_all(bind=db.engine)

app = FastAPI()


@app.post("/create/teacher")
async def create_teacher(
    teacher_data: Annotated[schema.TeacherRequest, Body()]
) -> schema.TeacherResponse:
    """
    Creates a new teacher in the database.

        Args:
            teacher_data: The teacher data to be created.

        Returns:
            Success message and the created teacher data.
    """
    try:
        teacher = db.Teacher(**teacher_data.model_dump())
        with db.local_session() as session:
            utils.insert_data(session, teacher)
        return schema.TeacherResponse(
            message="Teacher created successfully",
            data=schema.TeacherResponseData.from_orm(teacher),
        )
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail="Something went wrong"
        ) from exc


@app.post("/create/student")
async def create_student(
    student_data: Annotated[schema.StudentRequest, Body()]
) -> schema.StudentResponse:
    """
    Creates a new student in the database.

        Args:
            student_data: The student data to be created.

        Returns:
            Success message and the created student data.
    """
    try:
        student = db.Student(**student_data.model_dump())
        with db.local_session() as session:
            utils.insert_data(session, student)
        return schema.StudentResponse(
            message="Student created successfully",
            data=schema.StudentResponseData.from_orm(student),
        )
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail="Something went wrong"
        ) from exc


@app.get("/yearbook/{teacher_id}")
async def get_yearbook(
    teacher_id: Annotated[int, Path(ge=1)],
    page_size: Annotated[int, Query(ge=1)] = 10,
    page: Annotated[int, Query(ge=0)] = 0,
) -> schema.YearbookResponse:
    """
    Retrieves the yearbook for a specific teacher.

        Args:
            teacher_id: The ID of the teacher.
            page_size: The number of students to return per page.
            page: The page number to return.

        Returns:
            Success message and the yearbook data.
    """
    try:
        query = (
            select(
                db.Student.fullname.label("student"),
                db.Student.major,
                db.Teacher.fullname.label("teacher"),
                db.Teacher.classroom,
            )
            .join(db.Teacher.students)
            .where(db.Teacher.id == teacher_id)
            .limit(page_size)
            .offset(page)
        )
        with db.local_session() as session:
            yearbook = utils.get_data(session, query)
        return schema.YearbookResponse(
            message=f"Class of a teacher: {teacher_id}",
            data=yearbook,
        )
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail="Something went wrong"
        ) from exc
