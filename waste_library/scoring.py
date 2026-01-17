MODIFIERS = {
    "tiny": 1,
    "small": 1,
    "medium": 2,
    "large": 3,
    "dirty": 1,
    "broken": 2,
    "mixed": 3,
    "contaminated": 4,
    "street": 2,
    "hospital": 4,
    "industrial": 4
}

def calculate_points(base_points: int, text: str) -> int:
    points = base_points
    text = text.lower()

    for key, value in MODIFIERS.items():
        if key in text:
            points += value

    return max(points, 1)
