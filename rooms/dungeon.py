# rooms/dungeon.py
# dungeon.py © 2026 by Razvan Gogosanu is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

def run():
    print("\n === evil dungeon ===")
    print("get ready for a fun time")

    while True:
        choice = input("Where do you want to go?? > ").strip().lower()
        if choice == "space":
            print("join mason in space! why not visit mgr after?? :)")
            continue

        return choice
