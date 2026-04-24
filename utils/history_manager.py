import json
import os
from datetime import datetime

HISTORY_FILE = "qa_execution_history.json"


def save_execution_history(total, passed, failed, broken, skipped, pass_rate):
    history_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total": total,
        "passed": passed,
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "pass_rate": pass_rate
    }

    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []

    history.append(history_entry)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)