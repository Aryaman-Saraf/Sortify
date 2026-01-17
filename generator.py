# generator.py

from materials import materials
from scoring import compute_difficulty, compute_points, compute_priority

# --------------------------------------------------
# 200+ BASE ITEMS (CORE ONTOLOGY)
# --------------------------------------------------

base_items = {

    # ---------- ORGANIC (40) ----------
    "banana peel": "organic",
    "apple core": "organic",
    "orange peel": "organic",
    "mango peel": "organic",
    "vegetable peels": "organic",
    "potato peels": "organic",
    "onion skins": "organic",
    "tomato waste": "organic",
    "cooked rice": "organic",
    "cooked dal": "organic",
    "leftover curry": "organic",
    "bread waste": "organic",
    "egg shells": "organic",
    "fish bones": "organic",
    "chicken bones": "organic",
    "tea leaves": "organic",
    "coffee grounds": "organic",
    "fruit pulp": "organic",
    "spoiled fruits": "organic",
    "spoiled vegetables": "organic",
    "flower waste": "organic",
    "garden leaves": "organic",
    "grass clippings": "organic",
    "food scraps": "organic",
    "expired food": "organic",
    "curd waste": "organic",
    "milk residue": "organic",
    "butter paper food waste": "organic",
    "oil soaked food waste": "organic",
    "raw meat waste": "organic",
    "seafood waste": "organic",
    "coconut shell": "organic",
    "areca nut shell": "organic",
    "peanut shells": "organic",
    "sugarcane waste": "organic",
    "corn cobs": "organic",
    "bread crumbs": "organic",
    "rice husk": "organic",
    "food compost residue": "organic",
    "kitchen waste mix": "organic",

    # ---------- PAPER (40) ----------
    "newspaper": "paper_clean",
    "magazine": "paper_clean",
    "office paper": "paper_clean",
    "notebook paper": "paper_clean",
    "exam answer sheets": "paper_clean",
    "cardboard box": "paper_clean",
    "paper bag": "paper_clean",
    "paper envelope": "paper_clean",
    "paper file": "paper_clean",
    "printed paper": "paper_clean",
    "wrapping paper": "paper_clean",
    "paper carton": "paper_clean",
    "corrugated cardboard": "paper_clean",
    "paper cup": "paper_dirty",
    "paper plate": "paper_dirty",
    "pizza box": "paper_dirty",
    "burger box": "paper_dirty",
    "oil soaked paper": "paper_dirty",
    "used tissue paper": "paper_dirty",
    "napkins": "paper_dirty",
    "paper towel": "paper_dirty",
    "toilet paper roll": "paper_dirty",
    "paper straw": "paper_dirty",
    "milk carton paper": "paper_dirty",
    "juice carton paper": "paper_dirty",
    "receipt paper": "paper_dirty",
    "carbon paper": "paper_dirty",
    "thermal paper": "paper_dirty",
    "wall poster paper": "paper_dirty",
    "paper cup lid": "paper_dirty",
    "shredded paper": "paper_clean",
    "old books": "paper_clean",
    "newspaper bundle": "paper_clean",
    "exam hall paper": "paper_clean",
    "art paper waste": "paper_clean",
    "drawing sheets": "paper_clean",
    "chart paper": "paper_clean",
    "paper calendar": "paper_clean",
    "paper diary": "paper_clean",
    "newspaper with staples": "paper_clean",

    # ---------- PLASTIC (50) ----------
    "plastic bottle": "plastic_recyclable",
    "pet bottle": "plastic_recyclable",
    "plastic container": "plastic_recyclable",
    "plastic jar": "plastic_recyclable",
    "plastic bucket": "plastic_recyclable",
    "plastic mug": "plastic_recyclable",
    "plastic tray": "plastic_recyclable",
    "plastic box": "plastic_recyclable",
    "plastic lunch box": "plastic_recyclable",
    "plastic shampoo bottle": "plastic_recyclable",
    "plastic oil bottle": "plastic_recyclable",
    "plastic detergent bottle": "plastic_recyclable",
    "plastic milk pouch": "plastic_non_recyclable",
    "chips packet": "plastic_non_recyclable",
    "chocolate wrapper": "plastic_non_recyclable",
    "plastic carry bag": "plastic_non_recyclable",
    "plastic cling wrap": "plastic_non_recyclable",
    "plastic sachet": "plastic_non_recyclable",
    "plastic pouch": "plastic_non_recyclable",
    "multi-layered plastic": "plastic_non_recyclable",
    "plastic straw": "plastic_non_recyclable",
    "plastic spoon": "plastic_non_recyclable",
    "plastic fork": "plastic_non_recyclable",
    "plastic plate": "plastic_non_recyclable",
    "plastic cup": "plastic_non_recyclable",
    "plastic toys": "plastic_recyclable",
    "plastic furniture": "plastic_recyclable",
    "plastic chair": "plastic_recyclable",
    "plastic table": "plastic_recyclable",
    "plastic pipe": "plastic_recyclable",
    "plastic cable cover": "plastic_recyclable",
    "plastic tape": "plastic_non_recyclable",
    "plastic rope": "plastic_non_recyclable",
    "bubble wrap": "plastic_non_recyclable",
    "plastic foam": "plastic_non_recyclable",
    "thermocol": "plastic_non_recyclable",
    "plastic packaging waste": "plastic_non_recyclable",
    "plastic grocery bag": "plastic_non_recyclable",
    "plastic bottle cap": "plastic_recyclable",
    "plastic toothbrush": "plastic_non_recyclable",
    "plastic pen": "plastic_non_recyclable",
    "plastic marker": "plastic_non_recyclable",
    "plastic razor": "plastic_non_recyclable",
    "plastic gloves": "plastic_non_recyclable",
    "plastic helmet": "plastic_recyclable",
    "plastic keyboard cover": "plastic_recyclable",
    "plastic mouse cover": "plastic_recyclable",
    "plastic remote cover": "plastic_recyclable",

    # ---------- METAL (30) ----------
    "aluminium can": "metal",
    "steel bottle": "metal",
    "steel spoon": "metal",
    "steel plate": "metal",
    "tin can": "metal",
    "metal foil": "metal",
    "iron rod": "metal",
    "metal wire": "metal",
    "metal nails": "metal",
    "metal screws": "metal",
    "metal scrap": "metal",
    "copper wire": "metal",
    "brass items": "metal",
    "metal utensils": "metal",
    "broken lock": "metal",
    "keys": "metal",
    "metal hanger": "metal",
    "metal bottle cap": "metal",
    "metal lid": "metal",
    "metal box": "metal",
    "metal furniture": "metal",
    "metal shelf": "metal",
    "metal rack": "metal",
    "metal tools": "metal",
    "metal blade": "metal",
    "metal scissors": "metal",
    "metal nail cutter": "metal",
    "metal watch strap": "metal",
    "metal bangles": "metal",
    "metal jewellery scrap": "metal",
}

# --------------------------------------------------
# EXPANDED GENERATORS (MORE AXES)
# --------------------------------------------------

conditions = ["clean", "used", "dirty", "wet", "dry"]
sizes = ["tiny", "small", "medium", "large", "extra large"]
sources = [
    "household", "office", "school", "college", "restaurant",
    "hospital", "street", "mall", "factory", "construction site"
]
packaging = ["unwrapped", "wrapped", "mixed", "contaminated"]
age = ["fresh", "old"]
time_of_day = ["morning", "afternoon", "evening", "night"]

# NEW AXES (for scale + realism)
moisture = ["dry", "slightly wet", "soaked"]
damage = ["intact", "broken", "shredded"]
season = ["summer", "monsoon", "winter"]
handling = ["handled with care", "careless disposal"]
recyclability_state = ["easily recyclable", "hard to recycle"]
# ---------------- ADDITIONAL GENERATOR AXES ----------------

odor_level = ["odorless", "mild smell", "strong smell"]
toxicity = ["non-toxic", "low toxicity", "toxic"]
storage_time = ["immediate disposal", "stored overnight", "stored for days"]
user_awareness = ["easy to identify", "confusing", "commonly misclassified"]
collection_method = [
    "door-to-door pickup",
    "community bin",
    "drop-off center"
]
legal_status = [
    "allowed for disposal",
    "restricted disposal",
    "requires special handling"
]

# --------------------------------------------------
# GENERATOR ENGINE
# --------------------------------------------------

def generate_waste_library():
    waste_library = {}

    for item_name, material_key in base_items.items():
        material = materials[material_key]

        for condition in conditions:
            for size in sizes:
                for source in sources:
                    for pack in packaging:
                        for state in age:
                            for time in time_of_day:
                                for wetness in moisture:
                                    for breakage in damage:
                                        for seasonality in season:
                                            for recycle_state in recyclability_state:
                                                for smell in odor_level:
                                                    for tox in toxicity:
                                                        for storage in storage_time:
                                                            for awareness in user_awareness:
                                                                for collection in collection_method:
                                                                    for legal in legal_status:

                                                                        difficulty = compute_difficulty(
                                                                            material["base_difficulty"],
                                                                            condition,
                                                                            pack
                                                                        )

                                                                        points = compute_points(difficulty)
                                                                        priority = compute_priority(difficulty)

                                                                        key = (
    f"{condition} {state} {size} {item_name} "
    f"{wetness} {breakage} {smell} "
    f"from {source} during {seasonality} "
    f"{time} ({pack}, {recycle_state}, "
    f"{tox}, {storage}, {awareness}, "
    f"{collection}, {legal})"
)

                                                                        

                                                                        waste_library[key] = {
    "category": material_key,
    "bin": material["bin"],
    "difficulty": difficulty,
    "points": points,
    "priority": priority,
    "hazard": material["hazard"],
    "recyclable": material["recyclable"],
    "legal_status": legal,
    "collection_method": collection
}


    return waste_library


    return waste_library

