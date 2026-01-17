from itertools import product

# ---------- BASE DATA ----------
BASE_ITEMS = [
    ("banana_peel", "organic", 1),
    ("apple_core", "organic", 1),
    ("mango_peel", "organic", 1),
    ("orange_peel", "organic", 1),
    ("plastic_bottle", "plastic_recyclable", 2),
    ("plastic_wrapper", "plastic_non_recyclable", 3),
    ("paper_cup", "paper", 2),
    ("cardboard_box", "paper", 2),
    ("glass_bottle", "glass", 4),
    ("broken_glass", "glass", 5),
    ("used_battery", "e_waste", 6),
    ("mobile_charger", "e_waste", 5),
    ("sanitary_pad", "sanitary", 7),
    ("diaper", "sanitary", 7),
    ("cloth_piece", "cloth", 3),
] * 9  # 15 × 9 = 135 base items

CONDITIONS = {
    "clean": 0,
    "wet": 1,
    "dirty": 2,
    "broken": 1
}

CONTEXTS = {
    "home": 0,
    "restaurant": 1,
    "street": 1,
    "hospital": 2
}

SIZES = {
    "s": 0,
    "m": 1,
    "l": 2
}

CONTAMINATION = {
    "pure": 0,
    "mixed": 2
}

VARIANTS = range(40)  # synthetic expansion


# ---------- GENERATOR ----------
def generate_library(limit=500_000, progress_step=10_000):
    library = {}
    count = 0

    for (name, category, base_diff), cond, ctx, size, cont, var in product(
        BASE_ITEMS,
        CONDITIONS,
        CONTEXTS,
        SIZES,
        CONTAMINATION,
        VARIANTS
    ):
        key = f"{name}|{cond}|{ctx}|{size}|{cont}|v{var}"

        difficulty = (
            base_diff
            + CONDITIONS[cond]
            + CONTEXTS[ctx]
            + SIZES[size]
            + CONTAMINATION[cont]
        )

        library[key] = (category, difficulty)

        count += 1
        if count % progress_step == 0:
            print(f"Generated {count} items...")

        if count >= limit:
            break

    print(f"Finished generating {count} items.")
    return library
