import random, time, sys
from tabulate import tabulate
from os import system, name
from pyfiglet import Figlet

class Player_loc():
    def __init__(self, player_loc_vert, player_loc_hori, player_location, tower_key, magic_sword):
        self.player_loc_vert = player_loc_vert
        self.player_loc_hori = player_loc_hori
        self.player_location = player_location
        self.tower_key = tower_key
        self.magic_sword = magic_sword

class Player:
    def __init__(self, name, health, weapon, damage, defense, armor_pierce):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.damage = damage
        self.defense = defense
        self.armor_pierce = armor_pierce

class Monster:
    def __init__(self, name, health, defense, weapon, damage, armor_pierce):
        self.name = name
        self.health = health
        self.defense = defense
        self.weapon = weapon
        self.damage = damage
        self.armor_pierce = armor_pierce


def main():

    f = Figlet(font='epic')

    print_fast(f.renderText('Warlock Quest!'))
    to_continue()

    print_fast(help())
    to_continue()

    while True:
        char_name = str(input("\nChoose the name of your character here: ")) # Ask for character name
        clear()
        if char_name != '': #accept any name, even numbers, just not an empty string.
            break
        else:
            print("Please type a name.")

    player = get_player(char_name) # get character stats
    clear()
    print_slow(f"Your name is {player.name} and you wield the {player.weapon}. You have {player.health} HP, and {player.defense} DEF.\n") #display your character.

    while True:
        try:
            player_loc = get_start_loc(input("Where would you like to begin your adventure? Choose between 'town' or 'beach': ").lower())  #Get starting location on map for player.
            break
        except UnboundLocalError:
            print("Invalid input, please try again.")
            pass
    input("\nPress enter to begin: ")
    clear()

    game_on = True # GAME ON

    #-------------- Main adventure loop -----------#

    while game_on == True:
        clear()
        check_combat = True
        find_loc(player_loc.player_location, player, check_combat) # check if current map pos has enemies and if they attack or not.
        clear()
        print(f"Terrain of current area: {find_loc(player_loc.player_location, None)}")
        print()
        print(show_paths(player_loc.player_location)) # show surrounding areas and their terrain.
        player_loc = action_options(input("\nWhat would you like to do? ").lower(), player_loc.player_loc_vert, player_loc.player_loc_hori, player_loc.player_location, player, player_loc.tower_key, player_loc.magic_sword) #Default options in an area. search & travel to another area. # conditional actions: Fight, run,

def combat(player, enemy): # for any combat, start of combat. player_loc.player_loc_vert, player_loc.player_loc_hori

    monster_list = {
    '1' : {'name' : 'goblin', 'health' : 5, 'defense' : 1, 'weapon' : 'dagger', 'damage' : 4, 'armor_pierce': 10},
    '2' : {'name' : 'orc', 'health' : 12, 'defense' : 2, 'weapon' : 'sword', 'damage' : 8, 'armor_pierce': 10},
    '3' : {'name' : 'ogre', 'health' : 25, 'defense' : 0, 'weapon' : 'club', 'damage' : 10, 'armor_pierce': 5},
    '4' : {'name' : 'bandit', 'health' : 10, 'defense' : 2, 'weapon' : 'spear', 'damage' : 6, 'armor_pierce': 15},
    '5' : {'name' : 'giant spider', 'health' : 15, 'defense' : 2, 'weapon' : 'fangs', 'damage' : 6, 'armor_pierce': 15},
    '6' : {'name' : 'drake', 'health' : 50, 'defense' : 3, 'weapon' : 'claws', 'damage' : 8, 'armor_pierce': 20},

                    }

    monster = get_monster(monster_list, enemy) #generate monster stats.


    print_slow(f"\nAn evil {monster.name} appears before you! It wields: {monster.weapon}. It has {monster.health} HP, and {monster.defense} DEF.\n")

    action = input("Would you like to try and escape? type 'e'. If you would stand and fight! press enter.")
    if action == 'e':
        if run_away() == True:
            in_combat = False
        else:
            in_combat = True
    else:
        in_combat = True

    while in_combat == True: #Combat loop, where player and monster deal damage and attack each other until one is dead.
        dmg = get_wep_dmg(player.damage, player.armor_pierce, monster.defense) #calculate damage vs monsters defense. (player always goes first, no initiative.)
        monster.health -= dmg # monster is damaged.
        print_slow(f"\nYou attack with the {player.weapon} and deal {dmg} damage to the {monster.name}!")
        print_slow(f"\n{monster.name} has {monster.health} HP left.")

        if monster.health <= 0: #checks if monster or player is dead and ending combat if that is true
            print_slow("\nThe enemy is dead!")
            in_combat = False
            to_continue()
            break


        dmg = get_wep_dmg(monster.damage, monster.armor_pierce, player.defense) # calculate monster damage
        print_slow(f"\nThe {monster.name} attacks! It deals {dmg} damage to you.")
        player.health -= dmg #player is damaged
        print_slow(f"\nYou have {player.health} HP left")

        if player.health <= 0:
            sys.exit("\nYou are beaten, rest in pieces.\nBetter luck next time!")


        action = input("\nWould you like to keep fighting? 'y' or 'n': ")
        clear()
        if action == 'y':
            continue
        else:
            if run_away() == True:
                in_combat = False
                break
            else:
                continue



def get_weapon(player_name): # Displays weapon options to choose from and returns weapon stats to player.

    wep_list = [['sword', 8, 1, 25],['spear', 6, 2, 15],['axe', 10, 0, 35],['mace', 4, 3, 5]] #Weapons list
    print(f"Greetings, {player_name}. Choose your weapon.")

    print(tabulate(wep_list, headers=["Weapon", "Damage", "Defense", "AP %"], tablefmt="simple_grid"))
    print("'Damage' means that, for example, the sword deals between 1 and 8 damage everytime you attack. \n'Defense' lowers your enemies' damage against you.\n'AP' stands for Armor piercing. The percent chance to pierce their defenses. ")
    while True:
        weapon = input("choice: ").lower() # choose weapon

        for i in range(0, 4): #compare player input against weapons list.
            if weapon in wep_list[i][0]:
                current_weapon = wep_list[i]
                break
        if weapon == current_weapon[0]:
            break
        else:
            print("Your input does not match any of the weapons in the list, please try again.")
    return current_weapon #returns list of weapon stats.

def get_player(player_name): # Player character stats getter can make these setters and getters? in class methods.
    name = player_name
    health = 15
    weapon_stats = get_weapon(player_name)
    weapon = weapon_stats[0]
    defense = 1 + weapon_stats[2] #default defense + weapon defense
    damage = weapon_stats[1]
    armor_pierce = weapon_stats[3]
    return Player(name, health, weapon, damage, defense, armor_pierce)

def get_monster(monsters, monster_select): # monster stats getter in future monster stats will be gotten from a list/dict of monsters.
    for k, v in monsters.items(): # Loops thru dict
        if monster_select == v['name']: # checks for what monster is encountered
            monster = v # gets all stats
    name = monster['name']
    health = monster['health']
    defense = monster['defense']
    weapon = monster['weapon']
    damage = monster['damage']
    armor_pierce = monster['armor_pierce']
    return Monster(name, health, defense, weapon, damage, armor_pierce)


def get_wep_dmg(max_dmg, AP_chance, defense): # takes the damage stat of a weapon and returns an int between 1 and the damage stat. e.g. for sword its 1 to 8.
    ap = False
    if random.randint(1, 100) <= AP_chance: # if random is less than AP_Chance e.g. for Axe is 35. defense is ignored.
        ap = True
        print("\nThe attack pierces armor!") #Move this somehow??
    return dmg_calc(random.randint(1, max_dmg), ap, defense)

def dmg_calc(damage, ap, defense): #calcualte weapon damage versus defense and check armor piercing 'ap'.

    if ap == True:
        return damage
    else:
        if damage - defense < 0: # set damage to 0 so health does not go over maximum. e.g. minus minus.
            return 0
        else:
            return damage - defense

def run_away(): #  % chance to flee.
    x = random.randint(1, 100)
    if x >= 40:
        print("You escaped safely..")
        time.sleep(2)
        return True
    else:
        print_slow("The enemy blocks your way!\n")

def character_sheet(player): #call to display character in a fancy table. Will be an option to view character and collected items in adventure mode.
    char_sheet = [["HP", player.health], ["DEF", player.defense], ["Weapon", player.weapon,], ["Damage", player.damage], ["Items", " "]]
    headers = [player.name, "lvl 1 Warrior"] # make a variable at player class for levels. Then base stats on that variable. Perhaps even experience.
    print(tabulate(char_sheet, headers, tablefmt='fancy_grid'))


def action_options(action, player_loc_vert, player_loc_hori, player_loc, player, tower_key, magic_sword): # Display the current options depending on what is in current area. try except this or above where its called.

    if action == "north" or action == 'n' and player_loc_vert != 6: # future proof this sometime for larger maps with
        player_loc_vert += 1
    elif action == "south" or action == 's' and player_loc_vert != 1:
        player_loc_vert -= 1
    elif action == "west" or action == 'w' and player_loc_hori != 1:
        player_loc_hori -= 1
    elif action == "east" or action == 'e' and player_loc_hori != 6:
        player_loc_hori += 1
    elif action == "search":
        if player_loc == (3, 1):
            tower_key = show_special(player_loc, tower_key, magic_sword) # search for special place in current location
        elif player_loc == (2, 2):
            magic_sword = show_special(player_loc, tower_key, magic_sword)
        else:
            show_special(player_loc, tower_key, magic_sword)
    elif action =="rest":
        player.health = 15
        print(f"You rest, hoping for a calm evening...\nYour HP is now at {player.health}.")
        to_continue()
    elif action == "help":
        print_fast(help())
        to_continue()
    else:
        print("Nothing happens")
    player_location = (player_loc_vert, player_loc_hori)

    return Player_loc(player_loc_vert, player_loc_hori, player_location, tower_key, magic_sword)


def show_special(player_coordinates, tower_key, magic_sword): # Display points of interest in current area
    clear()
    print("You search the local area...")
    search = True
    special = find_loc(player_coordinates, None, search, tower_key, magic_sword)
    to_continue()
    return special

def get_start_loc(start_choice):
    clear()
    if start_choice == "town":
        player_loc_vert = 1
        player_loc_hori = 4
        print_fast("After a long and dangerous journey through the volcanic wasteland, you arrive in the southern part of Ios. A modest town, populated mostly by humans, is the local landmark. The town is rugged, but nothing you haven't seen before.")
    elif start_choice == "beach":
        player_loc_vert = 1
        player_loc_hori = 6
        print_fast("The last thing you remember was.. a storm. Your ship.. it was smashed to pieces against the jagged rocks.. As you open your eyes you realize you've washed ashore on a beatiful golden beach.\nYou slowly stand up ,legs trembling from the effort, and try to remember why you were on the ship..\nYou were headed for... Irnor the Imperial city of Irnor, the city of dice.")
    tower_key = False
    magic_sword = False
    player_location = (player_loc_vert, player_loc_hori)

    return Player_loc(player_loc_vert, player_loc_hori, player_location, tower_key, magic_sword)


def monster_check():
    x = random.randint(1, 100)
    if x >= 30:
        return None
    else:
        monsters = ["goblin", "bandit", "orc", "giant spider", "ogre", "drake" ]
        weights = [0.40, 0.20, 0.15, 0.10, 0.10, 0.05 ]
        x = random.choices(monsters, weights, k=1)
        return x[0]

def to_continue():
    input("\nPress enter to continue")
    clear()

def help():
    return "HOW TO PLAY: To travel to a nearby area you simply type: 'north' or 'n', 'south' or 's', 'east' or 'e' or 'west' or 'w'.\nWhen you want to investigate the local area, or interact with the local settlement, you do this by typing 'search'.\nIf you encounter an enemy, you may choose to fight or run.\nTo rest and recover your health type: 'rest'.\nYou can also type in 'help' to read this message again."

def show_paths(player_loc):

    return f"North: {find_loc((player_loc[0] + 1, player_loc[1]), None)}\nSouth: {find_loc((player_loc[0] - 1, player_loc[1]), None)}\nWest: {find_loc((player_loc[0], player_loc[1] - 1), None)}\nEast: {find_loc((player_loc[0], player_loc[1] + 1), None)}\nYou take a look around and notice {find_loc((player_loc[0], player_loc[1]), None, True, False, False, True)}."

def find_loc(coordinates, player, search = False, tower_key = False, magic_sword = False, show_spec = False): # General find stuff in map function. May take an optional function if player is searching local area, may reveal special items or locations.

    current_area = []
    map_grid = [

        ['loc1', (1, 1), 'volcanic desert', 'nothing special', 'enemy'], ['loc2', (1, 2), 'forest', 'nothing special', 'enemy'], ['loc3', (1, 3), 'forest', 'nothing special', 'enemy'],
        ['loc4', (1, 4), 'plains', 'a Human Town', ''], ['loc5', (1, 5), 'plains', 'nothing special', 'enemy'], ['loc6', (1, 6), 'beach', 'a Shipwreck', ''],
        ['loc7', (2, 1), 'desert', 'nothing special', 'enemy'], ['loc8', (2, 2), 'mountains', 'some Dwarven ruins', 'enemy'], ['loc9', (2, 3), 'forest', 'nothing special', 'enemy'],
        ['loc10', (2, 4), 'forest', 'nothing special', 'enemy'], ['loc11', (2, 5), 'plains', 'nothing special', 'enemy'], ['loc12', (2, 6), 'plains', 'nothing special', 'enemy'],
        ['loc13', (3, 1), 'desert', 'some Old ruins', 'enemy'], ['loc14', (3, 2), 'mountains', 'nothing special', 'enemy'], ['loc15', (3, 3), 'mountains', 'nothing special', 'enemy'],
        ['loc16', (3, 4), 'forest', 'nothing special', 'enemy'], ['loc17', (3, 5), 'plains', 'nothing special', 'enemy'], ['loc18', (3, 6), 'plains', 'The Imperial City', ''],
        ['loc19', (4, 1), 'oasis', 'a Nomad Camp', ''], ['loc20', (4, 2), 'desert', 'nothing special', 'enemy'], ['loc21', (4, 3), 'hills', 'nothing special', 'enemy'],
        ['loc22', (4, 4), 'forest', 'an Elven tree village', ''], ['loc23', (4, 5), 'forest', 'nothing special', 'enemy'], ['loc24', (4, 6), 'plains', 'nothing special', 'enemy'],
        ['loc25', (5, 1), 'desert', 'nothing special', 'enemy'], ['loc26', (5, 2), 'desert', 'nothing special', 'enemy'], ['loc27', (5, 3), 'plains', 'nothing special', 'enemy'],
        ['loc28', (5, 4), 'plains', 'nothing special', 'enemy'], ['loc29', (5, 5), 'marshes', 'nothing special', 'enemy'], ['loc30', (5, 6), 'marshes', 'nothing special', 'enemy'],
        ['loc31', (6, 1), 'mountains', 'nothing special', 'enemy'], ['loc32', (6, 2), 'mountains', 'a Dwarven Hold', ''], ['loc33', (6, 3), 'hills', 'nothing special', 'enemy'],
        ['loc34', (6, 4), 'hills', 'nothing special', 'enemy'], ['loc35', (6, 5), 'hills', 'nothing special', 'enemy'], ['loc36', (6, 6), 'marshes', 'A tall Tower', '']

                ] # The map is static, it will be rebuilt on every function call. Maybe design a function that contains the map grid and saves it to a new variable everytime its called and can be updated?

    try:
        for i in range(len(map_grid)):
            if coordinates == map_grid[i][1]: #check if the location is in the map_grid and return it. Can be used to check surrounding grids or current location of player.
                current_area.append(map_grid[i][2]) #0Terrain
                current_area.append(map_grid[i][3]) #1Landmark
                current_area.append(map_grid[i][4]) #2Enemy?
                if search == True and show_spec == True:
                    return map_grid[i][3]
                if coordinates == (6, 6) and tower_key == True:
                    print("The key from the desert ruins seem to fit perfectly. A loud *click* is heard and the wall shimmers with a purple glow to reveal an ordinary doorway. A set of stars going up is all you can see.")
                    to_continue()
                    print_slow("Walking up the stairs seems to take forever, and after a few minutes you come into a grand throne room.\nThe room seems too large to fit inside the narrow tower.\nYou look around, and at first seeing no sign of life. You clance behind you, expecting an ambush...\nSuddenly, A loud harrowing laughter echoes from the gilded throne.\nTurning around, you see a man clothed in purple robes that shimmer faintly sat upon it.")
                    print_slow("-'You are not welcome here... Not one of my enemies has survived my arcane powers, and you will NOT be the first. So.. MY home.. will be YOUR.. tomb!! *cackling laughter*")
                    if magic_sword == True:
                        print_slow("You draw the magical sword from the dwarven ruins and swing it against the evil warlock. He screams and recoils in terror as he realizes what blade you wield.")
                        sys.exit(print_slow("Your sword cleaves him in two and a loud *pop* is heard as the warlock erupts in blinding light... You look around, and it seems not even a speck of dust remains of the warlock.\nCongratulations, you have claimed victory against the evil warlock!"))
                    else:
                        print("Your weapon is not working against his enchanted robe!! He takes his time, and mutters some arcane words under his breath.\nA large fireball explodes outwards from his hand and engulfs you in flames..")
                        sys.exit(print_slow("You are dead.. Perhaps a special weapon will help you next time!"))

                if current_area[2] == 'enemy' and player != None:
                    enemy = monster_check()
                    if enemy == None:
                        return map_grid[i][2]
                    else:
                        combat(player, enemy)

                else:
                    if current_area[1] != '' and search == True and show_spec == False:
                        if coordinates == (3, 1): # Desert ruins
                            print("As you search the desert ruins, you find a glass orb. It is lying on a pedestal inside what used to be a tall tower.\nYou reach for the orb, but at the slightest touch, it shatters in a blinding light.\nWhen you regain your sight all that is left is a simple iron key with the initials 'A.W' inscribed.")
                            tower_key = True
                            return tower_key

                        if coordinates == (6, 6): # Wizard Tower
                            print("As you investigate the base of the tower you realize that it is missing an entrance. Looking closer, in the stone wall, there is a small key hole.")
                        if coordinates == (1, 4): #Human town
                            print("You look around town and see the sign of the 'Hooded badger', A local watering hole.\nThe inside of the tavern mirrors the mood of the town, rugged but calm.\nThe barkeep eyes you discerningly and pour you an ale.\nThe barkeep is suprisingly loose-lipped. He speaks to you about the local area and that the town was not always this somber.\nThe warlock Amarask Welt built his tower in the marshes to the north-east 30 years ago, and since then it all went downhill.\nHe offers little more except vague directions to a few settlements and places of interest.")
                            print("-'I hear to the north, an elven village lies hidden in the forest. And to the far north-west the dwarves have made their home in their mountain halls for many years.\nI also heard that the imperial city 'Irnor' in the east has closed its gates for the last months. If you're headed west you could find shelter in the desert at the Nomad's camp in the oasis.\nSome of the other adventurers have spoken of old ruins containing secrets not too far.\nSpecifically, the desert ruins south of the oasis, the nomads dare not go near it. Old magic guards that place they say.")
                            print("You thank the barkeep for his tales and flick him a silver coin which he snatches deftly from the air and bites it.\n'One ale was enough' you think to yourself, Time to get a move on...")
                        if coordinates == (4, 1): #Nomad Camp
                            print("The nomads welcome you warily and you are surprised they offer up water for free. They speak of the ruins to the south that is guarded by old magic.\nAlso, in the camp is a dwarven merchant. She tells you of her home to the north-north east.\nAfter a few ales with her she reveals that their ancestral home was destroyed.\nIt lies in the mountains between the desert and the forest, east of here.\nAfter a few more ales you leave the camp and go to sleep, waking up early to set off again..")
                        if coordinates == (4, 4): #Elven village
                            print("The elven village is small but seems safe enough to shelter. They allow you to spend the night in a small cottage on the outskirts.\nThe elves rarely speak but you overhear some songs that are sung in the common tongue.\nYou make out the lyrics, they tell of a magic elven sword that was stolen by the dwarves long ago.\nThe sword was the only weapon the elves had against their enemy: Witch queen Aniris.\nThe brave elven warrior fought and managed to strike the witch down, thus saving the village.")
                        if coordinates == (6, 2):# Dwarven hold
                            print("Spending some time with the dwarves in their home is fraught with ale in heaps. So many different tales are shared with you it is hard to keep track.\nOnce, you almost mentioned elvish wine and was near a beating, but all in all, a pleasant time.\nThe one story that was memorable was an old dwarven ancestral rhyme.\nIt mentions how the dwarves regard the earth as their mother and their brother wrought from 'the earth mother' is iron.\nYour stay at the dwarves was too short, but you are still impatient and leave early in the morning...")
                        if coordinates == (3, 6):#Imperial City, under lock down.
                            print("Approaching the city walls you see that the gate is closed and outside a large camp of people are living.\nIt seems that they are refugees from a village to the north near the marshes.\nThey speak in muted voices about the event that destroyed their village.\nHellfire from a clear sky suddenly started raining down upon them, bringing total destruction to the town.\nShortly thereafter the city gates were closed and has yet to open for several weeks..\nYou spend the night in the camp but find it hard to sleep, thoughts of fiery demons haunt your dreams.\nThe next day you leave.. hoping for a better future for the camp dwellers.")
                        if coordinates == (2, 2):# Dwarven ruins
                            print("You come upon the ruins of the dwarven ancestral home. Venturing deeper you see a small flicker of lights in the depths.\nClimbing is difficult, but with a few well placed ropes you manage to approach the light.\nThe light emits from a small hole in the rubble of a cave in. Crawling inside you come upon a grand room.\nThere you find a square translucent rock with a rusty sword plunged deep into it.\nAs you grab the sword a soothing voice inside your head speaks to you.")
                            guesses_left = 3
                            while True:
                                x = input("Taken from my mother's womb, Beaten and burned, I become a blood thirsty killer, what am I? ").lower()
                                if x == 'iron' or x == 'iron ore':
                                    print("You figured out the riddle and the sword comes out cleanly. After a second, it starts to shake and you struggle to hold on.\nThe shaking grows more intense and it seems to shake off the rust. What remains afterwards is a shining blade of white light.")
                                    magic_sword = True
                                    return magic_sword
                                else:
                                    guesses_left -= 1
                                    print("You guessed wrong, A light rumble is heard around you but nothing happens.")
                                    if guesses_left == 0:
                                        sys.exit(print_slow("\nThe rumble returns stronger this time. The cave structure starts to collaps and you are buried beneath the mountain forever...\nYou have died.."))

                        if coordinates == (1, 6): #shipwreck
                            print("Nothing of value is found in the shipwreck. Only some dead bodies floating in the water..")
                    return map_grid[i][2]
                return map_grid[i][2]

        if coordinates[0] > 6: # Avoid hard numbers, if the map is expanded this will break. Try to future proof? tie logic to map_grid coordinates? Max function?
            print("The Nyross mountains blocks your path to the north.")
            return "passage blocked"
        if coordinates[0] < 1:
            print("A volcanic area blocks your path to the south.")
            return "passage blocked"
        if coordinates[1] > 6:
            print("The Karnic Ocean blocks your path to the east.")
            return "passage blocked"
        if coordinates[1] < 1:
            print("The white desert of Harulra blocks your western path.")
            return "passage blocked"
    except NameError:
        pass


def clear(): #Taken from https://www.geeksforgeeks.org/clear-screen-python/

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_slow(str): #thematic text print
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

def print_fast(str): #thematic text print
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


if __name__ == "__main__":
    main()