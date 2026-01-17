# materials.py

materials = {

    # ---------------- ORGANIC ----------------
    "organic": {
        "bin": "Green Bin",
        "base_difficulty": 1,
        "hazard": False,
        "recyclable": True
    },

    # ---------------- PAPER ----------------
    "paper_clean": {
        "bin": "Blue Bin",
        "base_difficulty": 2,
        "hazard": False,
        "recyclable": True
    },
    "paper_dirty": {
        "bin": "Red Bin",
        "base_difficulty": 4,
        "hazard": False,
        "recyclable": False
    },

    # ---------------- PLASTIC ----------------
    "plastic_recyclable": {
        "bin": "Blue Bin",
        "base_difficulty": 3,
        "hazard": False,
        "recyclable": True
    },
    "plastic_non_recyclable": {
        "bin": "Red Bin",
        "base_difficulty": 6,
        "hazard": False,
        "recyclable": False
    },

    # ---------------- METAL ----------------
    "metal": {
        "bin": "Blue Bin",
        "base_difficulty": 3,
        "hazard": False,
        "recyclable": True
    },

    # ---------------- GLASS ----------------
    "glass": {
        "bin": "Blue Bin",
        "base_difficulty": 4,
        "hazard": True,
        "recyclable": True
    },

    # ---------------- E-WASTE ----------------
    "e_waste": {
        "bin": "E-Waste Collection Center",
        "base_difficulty": 7,
        "hazard": True,
        "recyclable": True
    },

    # ---------------- SANITARY ----------------
    "sanitary": {
        "bin": "Wrapped & Red Bin",
        "base_difficulty": 9,
        "hazard": True,
        "recyclable": False
    },

    # ---------------- CONSTRUCTION ----------------
"construction": {
    "bin": "C&D Waste Facility",
    "base_difficulty": 6,
    "hazard": False,
    "recyclable": False
},


    # ---------------- TEXTILE ----------------
    "textile_reusable": {
        "bin": "Donation / Textile Recycling",
        "base_difficulty": 3,
        "hazard": False,
        "recyclable": True
    },
    "textile_waste": {
        "bin": "Red Bin",
        "base_difficulty": 5,
        "hazard": False,
        "recyclable": False
    },

    # ---------------- HAZARDOUS ----------------
    "hazardous": {
        "bin": "Hazardous Waste Collection",
        "base_difficulty": 10,
        "hazard": True,
        "recyclable": False
    },

    # ---------------- BIOMEDICAL ----------------
    "biomedical": {
        "bin": "Yellow Biomedical Bin",
        "base_difficulty": 10,
        "hazard": True,
        "recyclable": False
    },

    # ---------------- RUBBER ----------------
    "rubber": {
        "bin": "Special Rubber Recycling",
        "base_difficulty": 5,
        "hazard": False,
        "recyclable": True
    },

    # ---------------- WOOD ----------------
    "wood": {
        "bin": "Wood Recycling / Compost",
        "base_difficulty": 4,
        "hazard": False,
        "recyclable": True
    }
}
