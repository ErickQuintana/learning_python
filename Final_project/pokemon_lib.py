#Calculate the damage taking int account move, df poke, atk poke
import random
def damage(atk_poke,move,df_poke):
    if atk_poke["type"] == "water" and df_poke['type'] == "fire":
        y = 1.5
    elif  atk_poke['type'] == 'fire' and df_poke['type'] == 'water':
        y =  .83
    else:
        y = 1
    if atk_poke['type'] == move['type']:
        x = 1.5
    else:
        x = 1
    z = random.randint(217,255)
    amount =((((((((((2*atk_poke["lvl"])/5)+2)*atk_poke['special Attack']*move['damge'])/df_poke["Defense"])/50)+2)*x)*y/10)*z)/255
    return amount
    
    
    
"""
 damamge =(((2*lvl)/(5+2))*B*C)/D)/50)+2)*X)*Y/10)*Z)/255

lvl = attacker's Level
B = attacker's Attack or Special
C = attack Power
D = defender's Defense or Special
X = same-Type attack bonus (1 or 1.5)
Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
Z = a random number between 217 and 255
"""