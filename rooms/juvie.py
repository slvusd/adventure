# rooms/juvie.py

def run(inventory):
    print("\n === Juvie Hall ===")
    print(f"You currently have: {inventory}")
    print("You were very bad!")

    inventory += ["ball"]

    if "knife" in inventory:
        pass
    else:
        inventory += ["knife"]

    while True:
        choice = input("Where do you go? > ").strip().lower()
        if choice != "mgr":
          print("You are trapped in Juvie hall!!!")
          print("But I'll let you go!")

        return choice

