import yampy
import random
import BingoBotConfig

access_token = BingoBotConfig.access_token
#yammer = yampy.Yammer(access_token=access_token)
picked = {column:[] for column in 'BINGO'}

def pick():
    number = random.randint(1,75)
    letter = f'{"BINGO"[(number - 1) // 15]}'
    return (letter, number)

def new_ball(dict=picked):
    letter, number = pick()    
    while number in dict[letter]:
        print(f'{letter} {number}: Repicking...')
        letter, number = pick()
    dict[letter].append(number)
    return (letter, number)

def print_drawn(dict=picked):
    print('Called numbers:')
    for i in dict:
        print(f'{i}: {sorted(dict[i])}')

t=0
while t < 25:
    new_ball()
    t+=1
print_drawn()
