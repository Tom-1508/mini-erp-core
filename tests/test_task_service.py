import pytest
from app.models.user import User
from app.models.role import Role
from app.models.task import Task, TaskStatus
from app.services.task_service import TaskService, PermissionDenied


def setup_users():
    return (
        User(id=1, username="user", role=Role.USER),
        User(id=2, username="manager", role=Role.MANAGER),
        User(id=3, username="admin", role=Role.ADMIN),
    )


def create_task(user):
    return Task(
        id=1,
        title="Service Test",
        description="Testing service layer",
        created_by=user,
        assigned_to=None
    )


def test_happy_path_flow():
    user, manager, admin = setup_users()
    task = create_task(user)

    TaskService.submit_task(task, user)
    assert task.status == TaskStatus.SUBMITTED

    TaskService.approve_task(task, manager)
    assert task.status == TaskStatus.APPROVED

    TaskService.close_task(task, admin)
    assert task.status == TaskStatus.CLOSED


def test_permission_denied():
    user, _, _ = setup_users()
    task = create_task(user)

    with pytest.raises(PermissionDenied):
        TaskService.approve_task(task, user)
