from classes.game import Person, bcolours

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460,65,60,34, magic)
enemy = Person(1200,65,45,25, magic)

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolours.FAIL + "\nYou do not have enough MP!\n" + bcolours.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolours.OKBLUE + "\n Spell: " + spell + " deals" + str(magic_dmg) + " points of damage!" + bcolours.ENDC)




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



