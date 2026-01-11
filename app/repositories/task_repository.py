import sqlite3
from typing import Optional

from app.models.task import Task, TaskStatus
from app.models.user import User


class TaskRepository:
    """
    Handles persistence of Task entities.
    """

    def __init__(self, db_path: str = "tasks.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    created_by INTEGER NOT NULL,
                    assigned_to INTEGER,
                    created_at TEXT,
                    updated_at TEXT
                )
                """
            )
            conn.commit()


    def save(self, task: Task) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO tasks
                (id, title, description, status, created_by, assigned_to, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task.id,
                    task.title,
                    task.description,
                    task.status.value,
                    task.created_by.id,
                    task.assigned_to.id if task.assigned_to else None,
                    task.created_at.isoformat(),
                    task.updated_at.isoformat(),
                ),
            )
            conn.commit()


    def get_by_id(self, task_id: int, users: dict[int, User]) -> Optional[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()

        if not row:
            return None

        return Task(
            id=row[0],
            title=row[1],
            description=row[2],
            status=TaskStatus(row[3]),
            created_by=users[row[4]],
            assigned_to=users.get(row[5]),
            created_at=row[6],
            updated_at=row[7],
        )


