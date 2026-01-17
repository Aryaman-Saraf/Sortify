from waste_library.resolver import resolve_waste

print("=== Sortify Waste Classifier ===")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Enter waste item: ")

    if user_input.lower() == "exit":
        break

    result = resolve_waste(user_input)
    print(result)
