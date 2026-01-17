import pickle
from generator import generate_library

print("Starting waste database generation...")

library = generate_library(limit=500_000)

with open("waste_db.pkl", "wb") as f:
    pickle.dump(library, f)

print("Database created successfully: waste_db.pkl")
