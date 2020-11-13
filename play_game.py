import json

import time

def main():
    # TODO: allow them to choose from multiple JSON files?
    with open('2spooky_mansion.json') as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


    
def add_items(items):
    stuff = []
    for i in items:
        stuff.append(items)
        
def drop_items(stuff):
    item == input("What item would you like to drop?")
    stuff = []
    for item in stuff:
        stuff.remove(item)

def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']
    visited = set()

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        print("Time:", time.perf_counter(), "seconds")

        # TODO: print any available items in the room...
        # e.g., There is a Mansion Key.
        
        #Keep track of player's location; print out message if revisitng room.
        if current_place in visited:
            print("...You've been in this room before.")
        visited.add(current_place)


        # Is this a game-over?
        if here.get("ends_game", False):
            break
        

        # Allow the user to choose an exit:
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))
            
        #List items to take as an option. 
        stuff = list_stuff(here)
        for i, items in enumerate(stuff):
            print ("  {}. {}".format(i+1, exit['description']))
            

        # See what they typed:
        action = input("> ").lower().strip()

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        #If the player asks for help, reprint the instructions
        #First task complete
        if action == "help":
            print_instructions()
            continue


#         # TODO: if they type "stuff", print any items they have (check the stuff list!)
        if action == "stuff":
            items = []
            if items:
                print(items)
            if not items:
                print("You have nothing.")
            continue
        
        # TODO: if they type "take", grab any items in the room.
#             if action == "take":
                add_items(items)
                continue
        
        #TODO: if they type "drop", drop the item from stuff.
            if action == "drop":
                items = []
                if items:
                    drop_item(stuff)
                if not items:
                    print("You have nothing.")   
                continue

            usable_exits = find_usable_exits(here, stuff)
            hidden_exits = find_hidden_exits(here)
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
            if action in ["search", "find"]:
                here = rooms[current_place]
                # Print the description.
                print(here["description"])
                hidden_exits = find_hidden_exits(here)
        # Print out numbers for them to choose:
                for i, exit in enumerate(hidden_exits):
                    print("  {}. {}".format(i+1, exit['description']))
                continue
#                 
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    print("=== GAME OVER ===")
    print("Time:", time.perf_counter(), "seconds")

def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        if "required_key" in exit:
            if exit["required_key"] in stuff:
                usable.append(exit)
            continue
        usable.append(exit)
    return usable

#For items in a room, list them as 'usable'. 
def list_stuff(room):
    usable = []
    for items in room ['items']:
        usable.append(items)
    return usable 

#Search for hidden exits.
def find_hidden_exits(room):
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", True):
            usable.append(exit)
            continue
    return usable


def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print("=== Instructions ===")
    print("")
    


if __name__ == '__main__':
    main()
