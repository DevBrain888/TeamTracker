from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("", response_model=STask)
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STask:
    created_task = await TaskRepository.add_one(task)
    return created_task

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks