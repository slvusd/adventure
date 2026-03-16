from rooms import goon, basement, space, armory, mgr, dungeon, juvie, office, island

inventory = []
celbrity = ''

def main():
    current_room = "juvie"
    
    rooms = {
        "goon": goon.run,
        "basement": basement.run,
        "space": space.run,
        "armory": armory.run,
        "mgr": mgr.run,
        "dungeon": dungeon.run,
        "juvie": juvie.run,
        "office": office.run,
        "island": island.run,
    }

    while current_room in rooms:
        current_room = rooms[current_room]()

main()

