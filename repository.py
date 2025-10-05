from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> STask:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            # refresh to load server defaults like created_at
            await session.refresh(task)
            await session.commit()
            return STask.model_validate(task)

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return tasks_schemas