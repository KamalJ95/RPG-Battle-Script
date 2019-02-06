from classes.game import Person, bcolours
from classes.magic import Spell
from classes.inventory import Item

"""Create some Items"""
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member.", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores party HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage.", 500)


'''Black magic'''
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

'''White Magic'''
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item" : potion, "quantity" : 5}, {"item" : hipotion, "quantity" : 5}, {"item" : superpotion, "quantity" : 3},
                {"item": elixer, "quantity": 15,},{"item" : hielixer, "quantity" : 5}, {"item" : grenade, "quantity" : 5}]

player = Person(460,65,60,34, magic, player_items)
enemy = Person(1200,65,45,25, [], [])

running = True

print(bcolours.FAIL + bcolours.BOLD + "An Enemy Attacks!" + bcolours.ENDC)

while running:
    print("===============================================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_Damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, " points of damage. Enemy hp: ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

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
            enemy.take_damage(magic_dmg)
            print(bcolours.OKBLUE + "\nSpell: " + spell.name + " deals " + str(magic_dmg) + " points of damage!" + bcolours.ENDC)

    elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose Item:")) - 1

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
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolours.OKGREEN + "\n" + item.name + " Fully restores HP and MP!" + bcolours.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolours.FAIL + "\n" + item.name + " Deals: " + str(item.prop) + " of damage!" + bcolours.ENDC)



    enemy_choice = 1

    enemy_dmg = enemy.generate_Damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for:", enemy_dmg)


    print('--------------------------------------')
    print("Enemy HP: " + bcolours.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolours.ENDC + "\n")
    print("Your HP: " + bcolours.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolours.ENDC + "\n")
    print("Your MP: " + bcolours.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolours.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolours.OKGREEN + "You win!" + bcolours.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolours.FAIL + "You died!" + bcolours.ENDC)
        running = False



