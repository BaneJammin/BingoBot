# import yampy
import random
import config
import time
import json

group_id = config.group_id
access_token = config.access_token #as a string
# yammer = yampy.Yammer(access_token=access_token) #as a string
picked = {column:[] for column in 'BINGO'}
savegame = r'.\savegame.txt'

# def auth():
#     try:
#         user = yammer.client.get('/users/current')
#         return True
#     except yampy.errors.UnauthorizedError as e:
#         print('UnauthorizedError: Please refresh access_token at \n'
#               'https://www.yammer.com/client_applications and update BingoBotConfig.py')
#         return False

def pick_new(number=None, picked=picked):
    '''Add a new ball to the list'''
    if not number:
        number = random.randint(1, 75)
    letter = f'{"BINGO"[(number - 1) // 15]}'
    if number not in picked[letter]:
        picked[letter].append(number)
        picked[letter] = sorted(picked[letter])
        return letter, number
    else:
        print(f'Repicking {letter} {number}...')
        return pick_new(number=random.randint(1, 75))

def format_called(picked=picked):
    '''Arrange the list of picked balls for printing'''
    s = ''
    for letter, numbers in picked.items():
        s += f'{letter}: {" ".join(str(value) for value in numbers)}\n'
    return s
    
def call_ball(group_id=group_id):
    '''Post the verified-unique ball to the Yammer API as a new thread,
    then reply to that thread with the listing of all called balls.'''
    ball = pick_new()
    all_balls = format_called()
    # m = yammer.messages.create(f'{ball[0]}{ball[1]}', group_id=group_id)
    print(f'{ball[0]}{ball[1]}')
    #replied_to_id = m['messages'][0]['thread_id']
    time.sleep(5)
    # r = yammer.messages.create(all_balls, replied_to_id=replied_to_id)    

def start_game(wait=15):
    if True: #auth():
        call_ball()
        #looping on range(wait) in 1s intervals allows for KeyboardInterrupt
        for i in range(wait):
            time.sleep(1)
    else:
        return False
