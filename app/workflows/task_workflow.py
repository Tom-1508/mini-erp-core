from app.models.task import TaskStatus, Task


class InvalidWorkflowTransition(Exception):
    """Raised when an invalid task status transition is attempted."""
    pass


class TaskWorkflow:
    """
    Centralized workflow engine for Task status transitions.
    """

    _allowed_transitions = {
        TaskStatus.DRAFT: {TaskStatus.SUBMITTED},
        TaskStatus.SUBMITTED: {TaskStatus.APPROVED},
        TaskStatus.APPROVED: {TaskStatus.CLOSED},
        TaskStatus.CLOSED: set(),  # terminal state
    }

    @classmethod
    def can_transition(cls, from_status: TaskStatus, to_status: TaskStatus) -> bool:
        return to_status in cls._allowed_transitions.get(from_status, set())

    @classmethod
    def transition(cls, task: Task, new_status: TaskStatus) -> None:
        if not cls.can_transition(task.status, new_status):
            raise InvalidWorkflowTransition(
                f"Cannot transition task from {task.status.value} to {new_status.value}"
            )

        task.status = new_status
