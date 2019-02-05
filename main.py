from classes.game import Person, bcolours
from classes.magic import Spell


'''Black magic'''
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

'''White Magic'''
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460,65,60,34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200,65,45,25, [])

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



