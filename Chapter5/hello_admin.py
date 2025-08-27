users = []

if users:
    for name in users:
        if name == "admin":
            print("whad up big dawg!")
        else:
            print(f"hello {name.title()}")
else:
    print("we need users")