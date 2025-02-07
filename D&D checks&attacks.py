import random, math
prof = 2
orcHP = 100
playerclass = input("do you want to be a fighter(f) of a wizard(w) ")
while True:
    if playerclass == 'f':
        HP = 20
        break
    elif playerclass == 'w':
        HP = 10
        break
    else:
        print("input not reconized")
def roll20():
    D20roll = random.randint(1,20)#this produces a random number
    return(D20roll)
def roll8():
    d8roll = random.randint(1,6)
    return d8roll
def rolld6(dicename):
    dicename = random.randint(1,6)#this produces a random number
    return dicename
def getstats(statname):
    rolls = []
    rolls += [rolld6(1)]
    rolls += [rolld6(2)]
    rolls += [rolld6(3)]#this adds the rolls to a list
    rolls += [rolld6(4)]
    rolls += [rolld6(5)]
    rolls = sorted(rolls)#this sorts the rolls
    first = (rolls[4])
    second = (rolls[3])
    third = (rolls[2])
    stat = first + second + third
    print("your", statname , "is", stat)
    return stat#return allows variables outside the function
def getmult(thing):
    thingmult = math.floor((thing - 10)/2)
    return thingmult
dex = getstats("dextertity")
dexmult = getmult(dex)
print ("your dexterity modifier is",dexmult)
strength = getstats("strength")
strenmult = getmult(strength)
print ("your strength modifier is",strenmult)
wis = getstats("wisdom")
wismult = getmult(wis)
print ("your wisdom modifier is",wismult)
int = getstats("inteligence")
intmult = getmult(int)
print ("your  inteligence  modifier is",intmult)
con = getstats("constitution")
conmult = getmult(con)
print ("your charisma modifier is",conmult)
rizz = getstats("charisma")
rizzmult = getmult(rizz)
print ("your charisma modifier is",rizzmult)

while True:
    choice = input('(c)check or (a)attack')
    if choice == 'c':
        print("what kind of check do you want to make?")
        check = input("inteligence(i) charisma(r) dexterity(d) wisdom(w) strength(s) or constitution(c)")
        roll = roll20()
        dnot = 0
        if check == 'i':
            roll += intmult
        elif check == 'r':
           roll += rizzmult
        elif check == 'd':
            roll += dexmult
        elif check == 'w':
            roll += wismult
        elif check == 's':
            roll += strenmult
        elif check == 'c':
            roll += conmult
        else:
            dnot = 1
        if not dnot == 1:
            print("you rolled a", roll)
    elif choice == 'a':
        roll = roll20()
        weapon = input("melee(m) or spell(s) attack?")
        if weapon == 'm':
            roll += strenmult
            if playerclass == 'f':
                roll += prof
        elif weapon == 's':
            roll += intmult
            if playerclass == 'm':
                roll += prof
        else:
            print("Input not valid")
        roll = str(roll)
        if roll == '15' or roll > '15':
            damage = roll8()
            orcHP -= damage
            print("you hit with a",roll)
            print("you hit the orc and did", damage, 'damage')
            print("the orc is now at", orcHP,"HP")
        else:
            print("you did not hit the orc")
            
    else:
        print("action not reconized")