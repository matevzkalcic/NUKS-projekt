import sqlite3
from pathlib import Path

DB_PATH = Path("app/tasks.db")

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
        """)
        conn.commit()

def add_task(title: str):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()

def get_tasks():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT id, title, completed FROM tasks").fetchall()

def complete_task(task_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()

def get_stats():
    with sqlite3.connect(DB_PATH) as conn:
        total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        done = conn.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1").fetchone()[0]
        return {"total_tasks": total, "completed": done, "completion_rate": (done / total * 100) if total else 0}

def delete_task(task_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        # Dovoli brisanje le, če je naloga že označena kot končana
        completed = conn.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if completed and completed[0]:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()