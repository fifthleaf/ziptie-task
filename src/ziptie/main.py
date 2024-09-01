from typing import Annotated

from fastapi import Body, FastAPI, HTTPException

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
