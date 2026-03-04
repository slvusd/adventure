# rooms/juvie.py

def run():
    print("\n === Juvie Hall ===")
    print("You were very bad!")

    while True:
        choice = input("Where do you go? > ").strip().lower()
        if choice != "sky":
          print("You are trapped in Juvie hall!!!")
          continue

        return choice

