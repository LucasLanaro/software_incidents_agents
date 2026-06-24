import json
from pathlib import Path


MEMORY_DIR = Path("memory")


def load_logs() -> str:
    with open(MEMORY_DIR / "logs.txt", "r", encoding="utf-8") as f:
        return f.read()


def load_metrics() -> str:
    with open(MEMORY_DIR / "metrics.txt", "r", encoding="utf-8") as f:
        return f.read()


def load_runbooks() -> str:
    with open(MEMORY_DIR / "runbooks.md", "r", encoding="utf-8") as f:
        return f.read()


def load_system_knowledge() -> str:
    with open(MEMORY_DIR / "system_knowledge.md", "r", encoding="utf-8") as f:
        return f.read()


def load_previous_incidents() -> list:
    with open(MEMORY_DIR / "previous_incidents.json", "r", encoding="utf-8") as f:
        return json.load(f)