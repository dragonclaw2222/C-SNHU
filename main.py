game_inventory = ['radio', 'helmet', 'health drink', 'armor', 'flashlight', 'metal pipe']
inventory = []


def tutorial():
    print('The goal of this game is to find all the items in the dungeon and escape')
    print('Use the search command to find items in each room to try to get back home')
    print('You can navigate the dungeon by inputting north , south , east , or west')
    print('You can check your inventory at any time by inputting inventory')
    bedroom()


def bedroom():
    print('You find yourself in a bedroom theres is a single door to the west')
    player_input = input().lower()
    if player_input == 'search':
        if 'radio' in inventory:
            print('You find nothing else of use in this room')
            bedroom()
        else:
            add_inventory('radio')
            print('You find a beat up old radio and pocket it')
            bedroom()
    if player_input == 'inventory':
        print(inventory)
        bedroom()
    if player_input == 'west':
        ladder_room()
    if player_input in ['search', 'inventory', 'west']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        bedroom()


def ladder_room():
    print('You find yourself in a room full of ladders there is a door to the east and west')
    player_input = input().lower()
    if player_input == 'search':
        print('You find nothing of use in this room')
        ladder_room()
    if player_input == 'inventory':
        print(inventory)
        ladder_room()
    if player_input == 'east':
        bedroom()
    if player_input == 'west':
        blood_pool()
    if player_input in ['search', 'inventory', 'west', 'east']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        ladder_room()


def blood_pool():
    print('A massive pool of blood fills the center of this room. There is a door to the north and west')
    player_input = input().lower()
    if player_input == 'search':
        if 'helmet' in inventory:
            print('You find nothing else of use in this room')
            blood_pool()
        else:
            add_inventory('helmet')
            print('You find a helmet floating in the pool')
            blood_pool()
    if player_input == 'inventory':
        print(inventory)
        blood_pool()
    if player_input == 'east':
        ladder_room()
    if player_input == 'north':
        dining_room()
    if player_input in ['search', 'inventory', 'north', 'east']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        blood_pool()


def dining_room():
    print('You stand in a dining room with rotting food covering the numerous tables. There are doors leading north, east, south, and west')
    player_input = input().lower()
    if player_input == 'search':
        if 'health drink' in inventory:
            print('You find nothing else of use in this room')
            dining_room()
        else:
            add_inventory('health drink')
            print('You sort through the rotting food and find some health drinks')
            dining_room()
    if player_input == 'inventory':
        print(inventory)
        dining_room()
    if player_input == 'south':
        blood_pool()
    if player_input == 'north':
        pitch()
    if player_input == 'west':
        freezer()
    if player_input == 'east':
        iron()
    if player_input in ['search', 'inventory', 'north', 'east', 'south', 'west']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        dining_room()


def freezer():
    print('You are in a large freezer with meat hanging from hooks. There is a door to the east back the way you came')
    player_input = input().lower()
    if player_input == 'search':
        if 'armor' in inventory:
            print('You find nothing else of use in this room')
            freezer()
        else:
            add_inventory('armor')
            print('You take a bulletproof vest that was hanging from one of the hooks')
            freezer()
    if player_input == 'inventory':
        print(inventory)
        freezer()
    if player_input == 'east':
        dining_room()
    if player_input in ['search', 'inventory', 'east']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        freezer()


def pitch():
    print('The room you are in is completely dark except a light source on the ground in the distance. The is a door to the south back the way you came')
    player_input = input().lower()
    if player_input == 'search':
        if 'flashlight' in inventory:
            print('You find nothing else of use in this room')
            pitch()
        else:
            add_inventory('flashlight')
            print('You head towards the light and find it to be a working flashlight')
            pitch()
    if player_input == 'inventory':
        print(inventory)
        pitch()
    if player_input == 'south':
        dining_room()
    if player_input in ['search', 'inventory', 'south']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        pitch()


def iron():
    print('You find yourself in a large rusted iron tunnel. There is a door to the east and north')
    player_input = input().lower()
    if player_input == 'search':
        if 'metal pipe' in inventory:
            print('You find nothing else of use in this room')
            iron()
        else:
            add_inventory('metal pipe')
            print('You pull a sturdy looking pipe off of one of the walls to use as a weapon')
            iron()
    if player_input == 'inventory':
        print(inventory)
        iron()
    if player_input == 'west':
        dining_room()
    if player_input == 'north':
        intermission()
    if player_input in ['search', 'inventory', 'north', 'west']:
        pass
    else:
        print('Choose a direction by inputting north, south, east, or west')
        print('Check your bag with inventory or search the room with search')
        iron()


def intermission():
    print('You feel a looming presence emanating from the room ahead')
    print('Make sure you are completely prepared with all six items before you continue.')
    print('You can check your inventory by inputting the inventory command')
    print('Input continue if you are ready or back if you need more time to prepare')
    player_input = input().lower()
    if player_input == 'inventory':
        print(inventory)
        intermission()
    if player_input == 'continue':
        boss_fight()
    if player_input == 'back':
        iron()
    if player_input in ['inventory', 'continue', 'back']:
        pass
    else:
        print('Choose to continue if you are ready or fall back if you need more items.')
        print('Check your bag with inventory.')
        intermission()


def boss_fight():
    if all(i in inventory for i in game_inventory):
        print('The radio you picked up begins to emit a loud static noise. \n'
              'Pointing the flashlight to the path ahead you see a massive creature emerge from the darkness. \n'
              'The beast slashes at you with its claws but the helmet and armor you found protects you. \n'
              'You wildly lash out with the pipe you found until the monster relents for the briefest of moments. \n'
              'You take this crucial opportunity to run past and up the stairs to freedom. \n'
              'Congratulations You Escaped And Won!!!')
    else:
        print('A monster leaps from the dark. \n'
              'Being under prepared it catches you off guard ending in your demise. \n'
              'You Lose. \n'
              'Try to find all the items before confronting the last room. \n'
              'The game will now restart')
        tutorial()


def add_inventory(item):
    game_inventory.remove(item)
    inventory.append(item)


tutorial()
