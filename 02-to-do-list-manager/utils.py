def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def normalize_status(status):
    status = status.strip().lower()
    if status in ("pending", "done"):
        return status
    return None

def normalize_priority(value):
    try:
        value = int(value)
        if value in (1, 2, 3):
            return value
        return None
    except ValueError:
        return None
    