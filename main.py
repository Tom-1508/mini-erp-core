# from app.models.user import User
# from app.models.role import Role

# user = User(id=1, username="tamal", role=Role.ADMIN)
# print(user)
# print(user.is_admin())


# from app.models.user import User
# from app.models.role import Role
# from app.models.task import Task, TaskStatus

# admin = User(id=1, username="admin", role=Role.ADMIN)
# user = User(id=2, username="user1", role=Role.USER)

# task = Task(
#     id=1,
#     title="Submit expense report",
#     description="Travel reimbursement",
#     created_by=user,
#     assigned_to=admin
# )

# print(task)
# print(task.status)


# from app.models.user import User
# from app.models.role import Role
# from app.models.task import Task, TaskStatus
# from app.workflows.task_workflow import TaskWorkflow, InvalidWorkflowTransition

# user = User(id=1, username="user1", role=Role.USER)

# task = Task(
#     id=1,
#     title="Submit expense",
#     description="Travel reimbursement",
#     created_by=user,
#     assigned_to=None
# )

# print(task.status)

# TaskWorkflow.transition(task, TaskStatus.SUBMITTED)
# print(task.status)

# try:
#     TaskWorkflow.transition(task, TaskStatus.CLOSED)
# except InvalidWorkflowTransition as e:
#     print(e)




from app.models.user import User
from app.models.role import Role
from app.models.task import Task, TaskStatus
from app.permissions.task_permissions import TaskPermission, TaskAction
from app.workflows.task_workflow import TaskWorkflow, InvalidWorkflowTransition

user = User(id=1, username="user1", role=Role.USER)
manager = User(id=2, username="manager1", role=Role.MANAGER)

task = Task(
    id=1,
    title="Purchase laptop",
    description="New developer machine",
    created_by=user,
    assigned_to=manager
)

# USER submits task
if TaskPermission.can_perform(user.role, TaskAction.SUBMIT):
    TaskWorkflow.transition(task, TaskStatus.SUBMITTED)

print(task.status)

# USER tries to approve (should fail permission)
if TaskPermission.can_perform(user.role, TaskAction.APPROVE):
    TaskWorkflow.transition(task, TaskStatus.APPROVED)
else:
    print("User not allowed to approve")

# MANAGER approves
if TaskPermission.can_perform(manager.role, TaskAction.APPROVE):
    TaskWorkflow.transition(task, TaskStatus.APPROVED)

print(task.status)
