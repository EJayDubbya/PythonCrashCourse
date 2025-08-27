current_users = ["Dingus", "boog", "bub", "marco polo", "mommie", "nahnie"]
new_users = ["dingus", "dell", "KK", "bub", "tades"]
current_case = [name.lower() for name in current_users]

for name in new_users:
    if name in current_case:
        print(f"{name.title()} is not available please choose a different name")
    else:
        print(f"{name.title()} is available")


