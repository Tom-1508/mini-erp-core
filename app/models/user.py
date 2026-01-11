from dataclasses import dataclass
from datetime import datetime
from app.models.role import Role


@dataclass
class User:
    id: int
    username: str
    role: Role
    created_at: datetime = datetime.utcnow()

    def is_admin(self) -> bool:
        return self.role == Role.ADMIN

    def is_manager(self) -> bool:
        return self.role == Role.MANAGER

    def is_user(self) -> bool:
        return self.role == Role.USER
