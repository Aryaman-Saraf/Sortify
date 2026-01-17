# classifier.py

def interpret_user_input(user_input, waste_library):
    tokens = user_input.lower().split()
    best_match = None
    best_score = 0

    for item in waste_library:
        score = sum(token in item for token in tokens)
        if score > best_score:
            best_score = score
            best_match = item

    return best_match


def classify_waste(user_input, waste_library):
    item = interpret_user_input(user_input, waste_library)

    if not item:
        return {"error": "Item not recognized"}

    data = waste_library[item]

    return {
        "item": item,
        "bin": data["bin"],
        "category": data["category"],
        "difficulty": data["difficulty"],
        "priority": data["priority"],
        "points": data["points"]
    }
