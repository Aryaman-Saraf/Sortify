from itertools import product

# ---------- BASE DATA ----------
BASE_ITEMS = [
    ("banana_peel", "organic - Green Dustbin", 1),
    ("apple_core", "organic - Green Dustbin", 1),
    ("mango_peel", "organic - Green Dustbin", 1),
    ("orange_peel", "organic - Green Dustbin", 1),
    ("plastic_bottle", "plastic_recyclable - Blue Dustbin", 2),
    ("plastic_wrapper", "plastic_non_recyclable - Black or Grey Dustbin", 3),
    ("paper_cup", "paper - Blue Dustbin", 2),
    ("cardboard_box", "paper - Blue Dustbin", 2),
    ("glass_bottle", "glass - Blue or Green Dustbin", 4),
    ("broken_glass", "glass - Blue or Green Dustbin", 5),
    ("used_battery", "e_waste - Green, Yellow, or Grey Dustbin", 6),
    ("mobile_charger", "e_waste - Green, Yellow, or Grey Dustbin", 5),
    ("sanitary_pad", "sanitary - yellow, black/tiger-striped, white, or blue dustbin", 7),
    ("diaper", "sanitary - yellow, black/tiger-striped, white, or blue dustbin", 7),
    ("cloth_piece", "cloth - Green Dustbin", 3),
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
