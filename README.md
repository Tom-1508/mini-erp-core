# Mini ERP Core (Python)

A minimal, backend-focused ERP-style system built in Python to demonstrate
enterprise-grade architecture, workflow-driven business logic, and role-based
authorization.

This project is intentionally framework-agnostic and focuses on **clean system
design, separation of concerns, and explainability**, rather than UI or APIs.

---

## 🎯 Why This Project Exists

This project was built to demonstrate:

- Strong Python fundamentals
- Enterprise-style backend architecture
- Workflow-based lifecycle management
- Role-Based Access Control (RBAC)
- Clean separation of domain, logic, and persistence layers
- Open-source–friendly and reviewable code structure

The design closely mirrors how real ERP systems and frameworks
(such as Frappe/ERPNext) are structured internally.

---

## 🧠 High-Level Architecture

The system follows a layered architecture where each layer has
**one clear responsibility**:

```

Models        → Domain entities (User, Task)
Workflows     → Valid state transitions
Permissions   → Role-based authorization rules
Services      → Business logic orchestration
Repositories  → Persistence (SQLite)

```

Each layer is independent and can evolve without tightly coupling
to other layers.

---

## 🔁 Task Lifecycle (Workflow Engine)

The task lifecycle is enforced via a centralized workflow engine:


DRAFT → SUBMITTED → APPROVED → CLOSED


- Invalid transitions are explicitly blocked
- Terminal states are enforced
- Workflow logic is isolated from models and services

---

## 🔐 Permission Model (RBAC)

Permissions are defined declaratively using role-to-action mappings:

- **Users** can create and submit tasks
- **Managers** can approve tasks
- **Admins** can close tasks

Authorization is checked **before** any workflow transition is applied.
Permissions and workflows are intentionally kept separate.

---

## 🧩 Service Layer (Business Orchestration)

All business operations are performed through a service layer:

- Services coordinate permission checks and workflow transitions
- Domain models remain clean and rule-free
- UI / API layers (future) would interact only with services

Example usage:

```python
TaskService.submit_task(task, user)
TaskService.approve_task(task, manager)
TaskService.close_task(task, admin)
````

---

## 🗄️ Persistence Strategy

* SQLite is used for simplicity
* A repository layer isolates all database logic
* Domain models remain storage-agnostic
* Easy to migrate to an ORM or different database later

---

## 🧪 Demo Execution

The project includes a simple `main.py` script that demonstrates:

* Task creation
* Workflow transitions
* Permission enforcement
* Persistence and retrieval

This script is intentionally kept minimal to showcase core logic.

---

## 🚀 Future Improvements

* REST API layer (Flask / FastAPI)
* ORM integration
* Configurable workflows
* Automated unit tests
* Role hierarchy support
* Audit log persistence

---

## 📌 Key Takeaway

This project prioritizes **clarity, maintainability, and explainability**—
the same qualities required in open-source and enterprise engineering teams.

It demonstrates how complex business rules can be modeled cleanly
without relying on heavy frameworks.