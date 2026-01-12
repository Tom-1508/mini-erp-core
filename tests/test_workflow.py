import pytest
from app.models.task import Task, TaskStatus
from app.models.user import User
from app.models.role import Role
from app.workflows.task_workflow import TaskWorkflow, InvalidWorkflowTransition


def create_task():
    user = User(id=1, username="user", role=Role.USER)
    return Task(
        id=1,
        title="Test Task",
        description="Test",
        created_by=user,
        assigned_to=None
    )


def test_valid_transition():
    task = create_task()
    TaskWorkflow.transition(task, TaskStatus.SUBMITTED)
    assert task.status == TaskStatus.SUBMITTED


def test_invalid_transition_raises_error():
    task = create_task()
    TaskWorkflow.transition(task, TaskStatus.SUBMITTED)

    with pytest.raises(InvalidWorkflowTransition):
        TaskWorkflow.transition(task, TaskStatus.CLOSED)
