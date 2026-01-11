from app.models.task import Task, TaskStatus
from app.models.user import User
from app.permissions.task_permissions import TaskPermission, TaskAction
from app.workflows.task_workflow import TaskWorkflow, InvalidWorkflowTransition


class PermissionDenied(Exception):
    """Raised when a user is not allowed to perform an action."""
    pass


class TaskService:
    """
    Orchestrates task-related business operations.
    """

    @staticmethod
    def submit_task(task: Task, user: User) -> None:
        if not TaskPermission.can_perform(user.role, TaskAction.SUBMIT):
            raise PermissionDenied("User not allowed to submit task")

        TaskWorkflow.transition(task, TaskStatus.SUBMITTED)

    @staticmethod
    def approve_task(task: Task, user: User) -> None:
        if not TaskPermission.can_perform(user.role, TaskAction.APPROVE):
            raise PermissionDenied("User not allowed to approve task")

        TaskWorkflow.transition(task, TaskStatus.APPROVED)

    @staticmethod
    def close_task(task: Task, user: User) -> None:
        if not TaskPermission.can_perform(user.role, TaskAction.CLOSE):
            raise PermissionDenied("User not allowed to close task")

        TaskWorkflow.transition(task, TaskStatus.CLOSED)
