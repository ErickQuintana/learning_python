import random
import pokemon_lib
# These are the battling pokes

#This is my battling pokemon 
#Change chnage the pokemon to be the exact same to have a close match i.e pok1 = poke 2
pokemon1 = {'name':'charemelon','lvl':30,'type':'fire', 'hp':90, 'speed':80,'special Attack':80,'Defense':58,'special_defense':65}
pokemon2 = {'name':'slowpoke','lvl':30,'type':'water', 'hp':90, 'speed':15,'special Attack':40,'Defense':58, 'special_defense':40}
pokes = [pokemon1,pokemon2]
round = 1
#Main battling loop    
while (pokemon1['hp']  > 0 and pokemon2['hp'] > 0 ):
    print("This is round",round)
    round += 1
    #Determine who atcks first
    n = random.random()
    atk = None
    df = None
    if (pokemon2['speed']/(pokemon1['speed']+pokemon2['speed'])) >= n:
        atk = pokemon2
        df = pokemon1
    else:
        atk = pokemon1
        df = pokemon2

    #These are the moves that pokemon can use
    move1 = {'name':'tackle','type':'normal','damge':20}
    move2 = {'name':'flamepunch','type':'fire','damge': 30}
    move3 = {'name':'water gun','type':'water','damge':30}
    moveset = [move1, move2,move3]
    
    
    if atk == pokemon1:
        move = random.choice(moveset)
        damge =pokemon_lib.damage(pokemon1,move,pokemon2)
        pokemon2['hp'] -= damge
        print(pokemon1["name"],"used",move["name"],"damage:",damge)
        print(pokemon1['name'],"hp",pokemon1["hp"],pokemon2["name"],"hp",pokemon2["hp"])
    if atk == pokemon2:
        move = random.choice(moveset)
        damge = pokemon_lib.damage(pokemon2,move,pokemon1)
        pokemon1['hp'] -= damge
        print(pokemon2["name"],"used",move["name"],"damage:",damge)  
        print(pokemon1['name'],"hp",pokemon1["hp"],pokemon2["name"],"hp",pokemon2["hp"])  
    if atk['hp'] < 0:
        print("winner is",df["name"])
        break
    if df['hp'] < 0:
        print("winner is",atk["name"])
        break
        
        
    if df == pokemon1:
        move = random.choice(moveset)
        damge =pokemon_lib.damage(pokemon1,move,pokemon2)
        pokemon2['hp'] -= damge
        print(pokemon1["name"],"used",move["name"],"damage:",damge)
        print(pokemon1['name'],"hp",pokemon1["hp"],pokemon2["name"],"hp",pokemon2["hp"])
    if df == pokemon2:
        move = random.choice(moveset)
        damge = pokemon_lib.damage(pokemon2,move,pokemon1)
        pokemon1['hp'] -= damge
        print(pokemon2["name"],"used",move["name"],"damage:",damge)
        print(pokemon1['name'],"hp",pokemon1["hp"],pokemon2["name"],"hp",pokemon2["hp"])
    if atk['hp'] < 0:
        print("winner is",df["name"])
        break
    if df['hp'] < 0:
        print("winner is",atk["name"])
        break
    




