favorite_fruits = ["raspberry", "lemon", "pineapple"]
if "raspberry" in favorite_fruits:
    print("You really like raspberries!")
if "lemon" in favorite_fruits:
    print("You really like  lemons!")
if "pineapple" in favorite_fruits:
    print("You really like pineapples!")
if "kiwi" in favorite_fruits:
    print("You really like kiwi!")
else:
    print("Kiwi is not your fave.")
if "strawberry" in favorite_fruits:
    print("You really like strawberries!")
else:
    print("Strawberries are not your fave.")

fruits_to_check = ["raspberry", "lemon", "pineapple", "kiwi", "strawberry"]
for fruit in fruits_to_check:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}s!")
    else:
        print(f"{fruit.title()} is not your fave.")