

import time
import random

dead = False
inventory = []

class weapon:                                         # defining weapons
    def __init__(self,name,damage,critchance=15):
        self.name = name
        self.damage = damage
        self.critchance = critchance

wooden_sword = weapon('wooden sword',4,15)            # adding weapons to inventory
silver_dagger = weapon('silver dagger',4,25)
BFG = weapon('BFG',100,100)
light_saber = weapon('light saber',4,15)
infantry_rifle = weapon('infantry rifle',2,20)
inventory.append(wooden_sword)
inventory.append(silver_dagger)
inventory.append(BFG)
inventory.append(infantry_rifle)

def VATS(name,health=10,power=3):               # the combat
    global dead
    global inventory
    roundCount = 0
    display = '|' * health   # displaying health
    acc = 0        # accuracy
    damage = 0
    crit = False
    headshot = False
    target_list = ['head','torso','right arm','left arm','right leg','left leg']         # possible targets for enemy
    health2 = 10                # player health
    display2 = '|' * health2    # player health displey
    FireAttack = False          # enemy special attack
    critChance = 15
    SPattackUse = 0       # detecting how many times the enemy has used their special attack
    Weapon = weapon('',0,0)   # empty weapon variable
    weapons = ''
    if infantry_rifle in inventory:
        weapons += ' infantry rifle '
    if wooden_sword in inventory:
        weapons += ' wooden sword '
    if silver_dagger in inventory:
        weapons += ' silver dagger '
    print(weapons)
    while True:
        weaponChoice = input('select weapon: ')
        if weaponChoice == 'infantry rifle' and infantry_rifle in inventory:
            Weapon = infantry_rifle
            break
        elif weaponChoice == 'wooden sword' and wooden_sword in inventory:
            Weapon = wooden_sword
            break
        elif weaponChoice == 'silver dagger' and silver_dagger in inventory:
            Weapon = silver_dagger
            break
        elif weaponChoice == 'light saber':
            Weapon = light_saber
            break
        elif weaponChoice == 'BFG':
            Weapon = BFG
            break
        else:
            print('invalid name')
            continue
                                                    # defining all the body parts ////////////////////////////////////
    class head:
        hp = 3
        prob = random.randint(1,25)
        crippled = False
    class torso:
        hp = 5
        prob = random.randint(1,95)
        crippled = False
    class right_arm:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class left_arm:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class right_leg:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class left_leg:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class p_right_arm:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class p_left_arm:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class p_right_leg:
        hp = 3
        prob = random.randint(1,95)
        crippled = False
    class p_left_leg:
        hp = 3
        prob = random.randint(1,95)
        crippled = False

        display = '|' * health
        print('')
        print(name,': ',display,sep='')

                                                # the printer //////////////////////////////////////////////////////////

        head.prob = random.randint(1,25)
        torso.prob = random.randint(1,95)
        right_arm.prob = random.randint(1,95)
        left_arm.prob = random.randint(1,95)
        right_leg.prob = random.randint(1,95)
        left_leg.prob = random.randint(1,95)
        print(head.prob,'%',' head ',sep='')
        print('')
        print(torso.prob,'%',' torso ',sep='')
        print('')
        print(right_arm.prob,'%',' right arm ',sep='')
        print('')
        print(left_arm.prob,'%',' left arm ',sep='')
        print('')
        print(right_leg.prob,'%',' right leg ',sep='')
        print('')
        print(left_leg.prob,'%',' left leg ',sep='')
        print('')

        while True:
            shoot = input('select target: ')                   # selecting targets /////////////////////////////////////
            if shoot == 'head':
                acc = head.prob
                headshot = True
                target = 'head'
            elif shoot == 'torso':
                acc = torso.prob
                target = 'torso'
            elif shoot == 'right arm':
                acc = right_arm.prob
                target = 'right arm'
            elif shoot == 'left arm':
                acc =  left_arm.prob
                target = 'left arm'
            elif shoot == 'right leg':
                acc = right_leg.prob
                target = 'right leg'
            elif shoot == 'left leg':
                acc = left_leg.prob
                target = 'left leg'
            else:
                print('invalid name')
                continue
            break
        print('')
                                                  # adding advantages and disadvantages based on crippled limbs
        if right_leg.crippled == True:
            acc += 5
        if left_leg.crippled == True:
            acc += 5
        if p_right_arm.crippled == True:
            acc -= 5
        if p_left_arm.crippled == True:
            acc -= 5
        critChance = Weapon.critchance
        if random.randint(1,100) <= acc:                    # running the hit chance
            print('hit')
            damage = random.randint(1,Weapon.damage)
            if random.randint(1,100) <= critChance:             # running the critical hit chance
                crit = True
            if crit == True:
                damage = damage * 2
                print('critical!!!!')
            if headshot == True:                     # checking for headshots
                damage = health
            time.sleep(1)
        else:
            print('miss')
            time.sleep(1)
        health -= damage
        if target == 'head':                    # damaging limbs and checking if they were crippled
            head.hp -= damage

        if target == 'torso':
            torso.hp -= damage

        if target == 'right arm':
            right_arm.hp -= damage
            if Weapon.name == 'light saber':
                right_arm.crippled = True
            if right_arm.hp <= 1:
                right_arm.crippled = True
            if right_arm.crippled == True:
                print("crippled")
                time.sleep(1)

        if target == 'left arm':
            left_arm.hp -= damage
            if Weapon.name == 'light saber':
                left_arm.crippled = True
            if left_arm.hp <= 1:
                left_arm.crippled = True
            if left_arm.crippled == True:
                print("crippled")
                time.sleep(1)

        if target == 'right leg':
            right_leg.hp -= damage
            if Weapon.name == 'light saber':
                right_leg.crippled = True
            if right_leg.hp <= 1:
                right_leg.crippled = True
            if right_leg.crippled == True:
                print("crippled")
                time.sleep(1)

        if target == 'left leg':
            left_leg.hp -= damage
            if Weapon.name == 'light saber':
                left_leg.crippled = True
            if left_leg.hp <= 1:
                left_leg.crippled = True
            if left_leg.crippled == True:
                print("crippled")
                time.sleep(1)

        damage = 0                        # reseting values that are going to be reused
        acc = 0
        crit = False
        critChance = 15
        headshot = False
        if health < 1:                   # seeing if enemy is dead
            print('')
            print(name,'dead')
            break
        time.sleep(0.5)

        shoot2 = ''                               # enemy turn starts ///////////////////////////////////////////////
                                                  # enemy turn is the same as player turn except for charge attack

        p_head  = random.randint(1,25)
        p_torso = random.randint(1,95)
        p_r_arm = random.randint(1,95)
        p_l_arm = random.randint(1,95)
        p_r_leg = random.randint(1,95)
        p_l_leg = random.randint(1,95)

        print('enemy selecting...')
        time.sleep(0.4)
        shoot2 = random.choice(target_list)

        if shoot2 == 'head':
            acc = p_head
            headshot = True
        if shoot2 == 'torso':
            acc = p_torso
        if shoot2 == 'right arm':
            acc = p_r_arm
        if shoot2 == 'left arm':
            acc = p_l_arm
        if shoot2 == 'right leg':
            acc = p_r_leg
        if shoot2 == 'left leg':
            acc = p_l_leg
        print('')
        acc = random.randint(1,100)
        if right_arm.crippled == True:
            acc -= 5
        if left_arm.crippled == True:
            acc -= 5
        if p_right_leg.crippled == True:
            acc += 5
        if p_left_leg.crippled == True:
            acc += 5
        if random.randint(1,100) <= acc:
            if random.randint(1,100) <= critChance:
                crit = True
            if crit == True:
                damage = damage * 2
                print('critical!!!!')
            if headshot == True:
                damage = health2
            time.sleep(1)
        else:
            print('miss')
            time.sleep(1)
        time.sleep(1)

        if target == 'right arm':
            p_right_arm.hp -= damage
            if p_right_arm.hp <= 1:
                p_right_arm.crippled = True
                print("crippled")
                time.sleep(1)

        if target == 'left arm':
            p_left_arm.hp -= damage
            if p_left_arm.hp <= 1:
                p_left_arm.crippled = True
                print("crippled")
                time.sleep(1)

        if target == 'right leg':
            p_right_leg.hp -= damage
            if p_right_leg.hp <= 1:
                p_right_leg.crippled = True
                print("crippled")
                time.sleep(1)

        if target == 'left leg':
            p_left_leg.hp -= damage
            if p_left_leg.hp <= 1:
                p_left_leg.crippled = True
                print("crippled")
                time.sleep(1)

        health2 -= damage
        display2 = '|' * health2
        damage = 0
        acc = 0
        crit = False
        headshot = False
        if health2 < 1:
            print('')
            print('You died')
            dead = True
            break
        print('current health:',display2)
        time.sleep(1)
    if dead == True:
        exit()
