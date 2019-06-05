import yampy
import random
import BingoBotConfig

access_token = BingoBotConfig.access_token
#yammer = yampy.Yammer(access_token=access_token)
already_picked = {column:[] for column in 'BINGO'}

def check_ball(func):
    print('Check ball')
    def wrapper(d):
        print('Wrapper')
        func_res = func()
        print('Wrapper return')
        return func_res[1] in d[func_res[0]]
    print('Check ball return')
    return wrapper

@check_ball
def pick_ball(min=1, max=5):
    print('Pick ball')
    picked_number = random.randint(7,10)
    picked_letter = f'{"BINGO"[(picked_number - 1) // 15]}'
    print(picked_letter, picked_number)
    print('Pick ball return')
    return (picked_letter, picked_number)

while not pick_ball(already_picked):
    print('False, repicking...')

    

def print_drawn(dict):
    print('Called numbers:')
    for i in dict:
        print(f'{i}: {dict[i]}')
