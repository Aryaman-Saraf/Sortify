import pickle
import sys

with open("waste_db.pkl", "rb") as f:
    WASTE_DB = pickle.load(f)

print("♻️ Sortify CLI ready (type 'exit' to quit)\n")


user_input = input("Enter waste item: ").lower()
if user_input == "exit":
    sys.exit(0)

match = next((k for k in WASTE_DB if user_input in k), None)

if match:
        category, difficulty = WASTE_DB[match]
        print(f"🗑️ Category: {category}\n\n")
        #print(f"🎯 Difficulty: {difficulty}")
        #print(f"⭐ Points: {difficulty * 10}\n")
else:
        print("❌ Item not found\n")
