#!python3.7

import yampy
import random
import BingoBotConfig
import time

group_id = BingoBotConfig.group_id #as an int
access_token = BingoBotConfig.access_token #as a string
yammer = yampy.Yammer(access_token=access_token) #as a string
picked = {column:[] for column in 'BINGO'}

def check_access_token():
    try:
        user = yammer.client.get('/users/current')
        return True
    except yampy.errors.UnauthorizedError as e:
        print('UnauthorizedError: Please refresh access_token at \n'
              'https://www.yammer.com/client_applications and update BingoBotConfig.py')
        return False
    
def pick():
    '''Pick a random ball from the legal pool.'''
    number = random.randint(1,75)
    letter = f'{"BINGO"[(number - 1) // 15]}'
    return (letter, number)

def new_ball(dict=picked):
    '''Check that the picked ball is unique and add it to the dict.'''
    letter, number = pick()    
    while number in dict[letter]:
        print(f'{letter} {number}: Repicking...')
        letter, number = pick()
    dict[letter].append(number)
    return (letter, number)

def format_called(dict=picked):
    '''Format the dict of called balls for human-readable printing.'''
    for i in dict:
        dict[i] = sorted(dict[i])
    s = ''
    for letter in 'BINGO':
        s += f'{letter}: '
        for called in dict[letter]:
            s += f'{called} '
        s += '\n'
    return s

def call_ball(group_id=group_id):
    '''Post the verified-unique ball to the Yammer API as a new thread,
    then reply to that thread with the listing of all called balls.'''
    ball = new_ball()
    all_balls = format_called()
    m = yammer.messages.create(f'{ball[0]}{ball[1]}', group_id=group_id)
    replied_to_id = m['messages'][0]['thread_id']
    time.sleep(5)
    r = yammer.messages.create(all_balls, replied_to_id=replied_to_id)

def start_game():
    while check_access_token():
        call_ball()
        time.sleep(30)
    else:
        return False
