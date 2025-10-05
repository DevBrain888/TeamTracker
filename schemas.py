from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, ConfigDict


class Status(str, Enum):
    new = "new"
    doing = "doing"
    done = "done"


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    status: Status = Status.new
    # update_at: datetime
    # priority: Optional[int] = None # low or high priority
    # due_data: Optional[datetime]

class STask(STaskAdd):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class STaskId(BaseModel):
    ok: bool = True
    task_id: int
