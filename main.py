from typing import List

from classes.game import Person, bcolours
from classes.magic import Spell
from classes.inventory import Item
import random


"""Create some Items"""
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member.", 99999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party HP/MP", 99999)
grenade = Item("Grenade", "attack", "Deals 500 damage.", 1000)


'''Black magic'''
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

'''White Magic'''
cure = Spell("Cure", 12, 300, "white")
cura = Spell("Cura", 18, 600, "white")

magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, cura]
player_items = [{"item" : potion, "quantity" : 5}, {"item" : hipotion, "quantity" : 5}, {"item" : superpotion, "quantity" : 3},
                {"item": elixer, "quantity": 15,},{"item" : hielixer, "quantity" : 5}, {"item" : grenade, "quantity" : 5}]

player1 = Person("Riku  ", 3460,132,60,34, magic, player_items)
player2 = Person("Sora  ", 1460,188,60,34, magic, player_items)
player3 = Person("Roxas ", 2460,174,60,34, magic, player_items)

enemy2 = Person("Imp        ", 1200, 130, 560, 325, enemy_spells,[])
enemy1 = Person("Xehanort ",18000,400,400,25, enemy_spells, [])
enemy3 = Person("Imp        ", 1200, 130, 560, 325, enemy_spells,[])

players = [player1,player2,player3]
enemies: List[Person] = [enemy1,enemy2,enemy3]

running = True

print(bcolours.FAIL + bcolours.BOLD + "An Enemy Attacks!" + bcolours.ENDC)

while running:
    print("===============================================")

    print("\n\n")
    print("NAME          HP                                         MP")

    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_Damage()

            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)

            print("\n" + "You attacked: " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been defeated!")
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose Magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()




            if spell.cost > current_mp:
                print(bcolours.FAIL + "\nYou do not have enough MP!\n" + bcolours.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolours.OKBLUE, "\n" + spell.name, "Heals for:", str(magic_dmg), "HP.", bcolours.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print(bcolours.OKBLUE + "\nSpell: " + spell.name + " deals " + str(magic_dmg) + " damage to " + enemies[enemy].name.replace(" ","") +  bcolours.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated!")
                    del enemies[enemy]

        elif index == 2:
                player.choose_items()
                item_choice = int(input("    Choose Item:")) - 1

                if item_choice == -1:
                    continue


                item = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] == 0:
                    print(bcolours.FAIL + "\n", "None left..."+ bcolours.ENDC)
                    continue

                player.items[item_choice]["quantity"] -= 1

                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolours.OKGREEN + "\n" + item.name + " heals for", str(item.prop) + "HP"+ bcolours.ENDC)
                elif item.type == "elixer":

                    if item.name == "MegaElixer":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolours.OKGREEN + "\n" + item.name + " Fully restores HP and MP!" + bcolours.ENDC)
                elif item.type == "attack":
                    enemy = player.choose_target(enemies)

                    enemies[enemy].take_damage(item.prop)

                    print(bcolours.FAIL + "\n" + item.name + " Deals: " + str(item.prop) + " of damage to: " + enemies[enemy].name + bcolours.ENDC)

                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has been defeated!")
                        del enemies[enemy]

    """Checks if battle is over"""
    defeated_enemies = 0
    defeated_players = 0

    """Check if enemy won"""
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    """Check if player won"""
    for player in players:
        if player.get_hp() == 0:
            defeated_players ++ 1

    if defeated_enemies == 2:
        print(bcolours.OKGREEN + "You win!" + bcolours.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolours.FAIL + "You died!" + bcolours.ENDC)
        running = False

    for enemy in enemies:
        enemy_choice = random.randrange(0,2)
        if enemy_choice == 0:

            target = random.randrange(0,3)
            enemy_dmg = enemy.generate_Damage()
            players[target].take_damage(enemy_dmg)
            print( "\n" + bcolours.FAIL + enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg, "damage." + bcolours.ENDC)

        elif enemy_choice == 1:
           spell, magic_dmg = enemy.choose_enemy_spell()
           enemy.reduce_mp(spell.cost)

           if spell.type == "white":
               enemy.heal(magic_dmg)
               print(bcolours.OKBLUE, "\n" + spell.name, "heals " + enemy.name.replace(" ", "") + " for:", str(magic_dmg), "HP.", bcolours.ENDC)
           elif spell.type == "black":
               target = random.randrange(0, 3)

               players[target].take_damage(magic_dmg)

               print(bcolours.FAIL + "\nSpell: " + spell.name + " deals " + str(magic_dmg) + " to " + players[target].name + bcolours.ENDC)

               if players[target].get_hp() == 0:
                   print(players[target].name.replace(" ", "") + " has been defeated!")
                   del players[player]








