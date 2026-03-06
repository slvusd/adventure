# main2.py
import importlib
import inspect
import pkgutil
import rooms


def discover_rooms():
    """Find all valid room modules in the rooms/ package and return a dict of name -> run function."""
    room_map = {}
    for finder, name, ispkg in pkgutil.iter_modules(rooms.__path__):
        try:
            module = importlib.import_module(f"rooms.{name}")
            if hasattr(module, 'run'):
                room_map[name] = module.run
            else:
                print(f"[warning] rooms/{name}.py has no run() function — skipping")
        except Exception as e:
            print(f"[warning] Could not load rooms/{name}.py: {e} — skipping")
    return room_map


def call_room(room_fn, inventory, state):
    """Call a room function with however many arguments it is ready to accept."""
    num_params = len(inspect.signature(room_fn).parameters)
    if num_params == 0:
        return room_fn()
    elif num_params == 1:
        return room_fn(inventory)
    else:
        return room_fn(inventory, state)


def main():
    room_map = discover_rooms()

    if not room_map:
        print("No rooms found. Add some .py files to the rooms/ folder.")
        return

    print(f"Loaded rooms: {list(room_map.keys())}\n")

    inventory = []
    state = {
        "visited": [],
    }

    current_room = "forest" if "forest" in room_map else next(iter(room_map))

    while current_room in room_map:
        state["visited"].append(current_room)
        next_room = call_room(room_map[current_room], inventory, state)

        if next_room is None:
            print("\n[Room returned None — did you forget a return statement?]")
            break
        elif next_room not in room_map:
            print(f"\n['{next_room}' doesn't exist yet — coming soon!]")
            break

        current_room = next_room

    print("\nThanks for playing.")


main()

