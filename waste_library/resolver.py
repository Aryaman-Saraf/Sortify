from .materials import MATERIALS
from .keywords import KEYWORDS
from .scoring import calculate_points

def resolve_waste(user_input: str):
    text = user_input.lower()
    selected_material = None
    highest_priority = -1

    for material, data in KEYWORDS.items():
        if any(word in text for word in data["words"]):
            if data["priority"] > highest_priority:
                highest_priority = data["priority"]
                selected_material = material

    if selected_material is None:
        return {
            "error": "Unknown waste item"
        }

    base = MATERIALS[selected_material]
    points = calculate_points(base["base_points"], text)

    return {
        "object": user_input,
        "material": selected_material,
        "bin": base["bin"],
        "points": points
    }
