#### Video Demo:  https://youtu.be/TBYffmlmo5g
## Description: This is a text-based adventure game with light combat mechanics.

As described before. This is an old-school adventure game with minor combat encounters. The name 'Warlock Quest' is a semi-parody at 80's naming conventions on fantasy themed products.

### Classes:
I was sure I wanted to use classes since they allow me to control variables associated with an explicit monster or the player easier. And later on a new a new class was developed, Player location.
It handles player location vertically and horizontally as two seperate but also player location as a tuple based on them. I wanted to handle them seperately because I can increase or decrease them easier if they are seperate to move or show specific locations on the map.
Besides the current location on the map, this class also handles if the Tower key and magic sword are found yet or not. You need the key to access the tower. But also need the sword to defeat the Warlock.

### Main:
Using figlet for the intro title was a late addition but an easy implementation, and it makes the game feel more like a game. And I discovered, quite late, that the Print_fast function makes it look even cooler!

In main there is the 'preparations' and the 'main adventure loop'. The prep is showing how the game works, the title, asking the player to select a name for the character, and calling get_player. To get the stats for the character. I elected to go with static stats and not base them on a level system. I needed to cut some corners sometimes to save time since I had a deadline for myself.

The adventure loop is quite short but calls find_loc and checks of there will be combat in the new location. It asks you for your actions on the adventuring map. Action_options has a few different actions which the player can take.

#### Combat:
Later is the combat function with the combat loop inside. A loop here is ideal to check after every attack and or 'turn' in combat if the player or the enemy is defeated.
This monster list I wanted to put in its on file but seemed to have some trouble with it and simply put it in the combat function for ease of access, since we must use the get_monster function early on to generate the monster stats.

#### Info display:
I use clear() a lot since I don't want any information from previous combat rounds or even previous locations blobbing up in terminal. A clean terminal makes it easier to play the game.
I also use a small to_continue function which I find nifty if I want to make sure there is information that don't disappear too fast from the terminal. A fine balance between clear() and to_continue() is needed.


#### Weapon Choice, Damage, and Combat continued:
I have a whole function for the player to choose his weapon and tabulate displays the weapons and their different stats very nicely. It is actually called in the 'prep' phase in main. by get_player. I wanted it there since you setup your character usually at the start of the game and a weapon is not very important but somewhat.

I have a function for telling the damage calculation function what stats the weapon has. Which I think is thinking forward if I ever wanted to add more weapons I simply have to make the stats for them and not put them in manually in all these damage calc functions. Just the initial weapon_choice function.

A little run away function that is called in combat loop if you think you are outmatched in combat. Based on a % chance. choosing 1, 100 seems to make it easy for a human to understand.


The character sheet which is mostly aesthetics. Displays your character in tabulate nicely with all your stats. Level is included here because I might still expand on this project.

#### Actions_options:
The action_options functions is not future proofed. I was thinking of having a randomized map. These hard numbers from the tuple grid (1, 6) must be changed. But it works for my 'static' map.
This is the main decider. What the player chooses comes through this function and it decides depending on what input the player has done.

Show_special calls find_loc for the special locations. Like the wizard tower and ruins and the settlements. Points of interest.

get_start_loc is called in 'prep' phase and lets you choose between town and beach. At first I did not see the need to include a second start location but I think it makes the game slightly dynamic. A different 'origin' story one could say, albeit simplified.

#### Monsters:
And, monster_check(). % chance for en encounter with a random monster. I like the weights here but I could see myself making them variables that depend on location in the map.
In fact, at first I had the monsters manually set out in the grid map. e.g at (1, 6) there would only be goblin. But I found it easier to simply make a few areas have no enemies and then make most of them have a % chance to encounter them for a bit of variation.

#### Locations & Map:
find_loc is the map. it recreates the map just everytime it is called. Not ideal I would say. I wanted it to be changeable at first. But for time limitations sake I made it static. If there is a function I would change the most it is perhaps this one. It takes a number of arguments and most of them are optional. It really only needs coordinates to function at its base.
A lot of If operators here. I am more versed in using If than match case and I think it suits me better here.

At the end there are the Thematic print functions for the text to seem like someone is typing it, two different speeds. Another one of those things that makes the game feel more like a game.
