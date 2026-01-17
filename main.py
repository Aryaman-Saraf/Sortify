'''This is main.py'''
# main.py

from generator import generate_waste_library
from classifier import classify_waste

def run_sortify():
    print("♻️ SORTIFY — 1,000,000+ Waste Items Assistant ♻️")
    print("Generating waste library (this may take some time)...")

    waste_library = generate_waste_library()
    print(f"Library loaded with {len(waste_library)} items")

    while True:
        user_input = input("\nEnter waste item (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Thank you for using Sortify 🌱")
            break

        result = classify_waste(user_input, waste_library)

        if "error" in result:
            print("Item not recognized. Try again.")
        else:
            print("\nMatched Item:", result["item"])
            print("Bin:", result["bin"])
            print("Category:", result["category"])
            print("Difficulty:", result["difficulty"])
            print("Priority:", result["priority"])
            print("Points:", result["points"])


if __name__ == "__main__":
    run_sortify()
