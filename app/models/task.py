from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from app.models.user import User


class TaskStatus(Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    CLOSED = "closed"
    


@dataclass
class Task:
    id: int
    title: str
    description: str
    created_by: User
    assigned_to: User | None
    status: TaskStatus = TaskStatus.DRAFT
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

