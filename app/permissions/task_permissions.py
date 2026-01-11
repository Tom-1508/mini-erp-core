from enum import Enum
from app.models.role import Role
from app.models.task import TaskStatus

class TaskAction(Enum):
    CREATE = "create"
    SUBMIT = "submit"
    APPROVE = "approve"
    CLOSE = "close"
    VIEW = "view"


class TaskPermission:
    """
    Centralized permission rules for Task actions.
    """

    _permissions = {
        TaskAction.CREATE: {Role.USER, Role.MANAGER, Role.ADMIN},
        TaskAction.SUBMIT: {Role.USER},
        TaskAction.APPROVE: {Role.MANAGER, Role.ADMIN},
        TaskAction.CLOSE: {Role.ADMIN},
        TaskAction.VIEW: {Role.USER, Role.MANAGER, Role.ADMIN},
    }

    @classmethod
    def can_perform(cls, role: Role, action: TaskAction) -> bool:
        allowed_roles = cls._permissions.get(action, set())
        return role in allowed_roles
