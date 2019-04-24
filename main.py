from classes.game import Person,Colors
from classes.magic import Magic
import random
#from termcolor import colored

lightning = Magic('Lightning', 15, 150,"destroy")
fire = Magic('Fire', 12, 120,"destroy")
quake = Magic('Quake', 13, 130,"destroy")
metal = Magic('Metal', 14, 140,"destroy")
 
healer = Magic("Healer", 12, 120, "medical")
cura = Magic("Cura", 18, 180, "medical")

magic = [lightning, fire, quake, metal, healer, cura]

player = Person(460, 65, 50, 30, magic)
enemy = Person(1500, 65, 40, 40, [])

print(Colors.BOLD + Colors.FAIL + "Enemy Attacks!!!", Colors.ENDC)

while True:
    print(Colors.OKBLUE + "================ACTIONS==========================" + Colors.ENDC)

    player.choose_action()
    choice = int(input("Choose Action : ")) - 1
    if choice<0 or choice > player.get_action_len()-1:
            print(Colors.WARNING+"Invalid Choice."+Colors.ENDC)
            continue
    
    print("You chose",player.get_action(choice))

    if choice == 0:
        attack_dmg = player.generate_damage()
        enemy.take_damage(attack_dmg)
        print("Enemy took",attack_dmg,"Damage.")

    elif choice == 1:
        print(Colors.OKBLUE +"\n\nSPELLS"+Colors.ENDC)
        player.choose_magic()
        choice = int(input("Choose Magic : ")) - 1


        spell = magic[choice].get_magic_name()
        cost = magic[choice].get_magic_cost()
        magic_dmg = magic[choice].generate_damage()

        if cost > player.get_mp():
            print("You don't have enough MP")
            continue
            
        player.reduce_mp(cost)

        if magic[choice].get_magic_type() == 'medical':
            player.heal_hp(magic_dmg)
            print("Your spell",spell,"healed",magic_dmg,"hp")

        elif magic[choice].get_magic_type() == 'destroy' :
            enemy.take_damage(magic_dmg)
            print("Your spell",spell,"dealt",magic_dmg,"damage")
        
        

    enemy_choice = 0
    if  enemy_choice == 0:
        attack_dmg = enemy.generate_damage()
        player.take_damage(attack_dmg)
        print("You Took",attack_dmg,"damage")
        

    print(Colors.OFGREEN+"\n-------------------------------")
    print("Enmey Hp : ",enemy.get_hp())
    print("\nYour Hp : ",player.get_hp())
    print("Your Mp : ",player.get_mp())
    print("-------------------------------",Colors.ENDC)

    if enemy.get_hp() <= 0:
        print(Colors.OFGREEN+"You have defeated the enemy....."+Colors.ENDC)
    elif player.get_hp() <= 0:
        print(Colors.FAIL+"Enemy wins......"+Colors.ENDC)

    q=input()
    if q=='q' or q=='Q':
        break

