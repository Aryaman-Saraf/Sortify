# scoring.py

def compute_difficulty(base, condition, packaging):
    difficulty = base
    if condition in ["dirty", "wet"]:
        difficulty += 1
    if packaging in ["mixed", "contaminated"]:
        difficulty += 2
    return min(difficulty, 10)


def compute_points(difficulty):
    return difficulty * 2


def compute_priority(difficulty):
    if difficulty <= 3:
        return "Low"
    elif difficulty <= 6:
        return "Medium"
    else:
        return "High"
