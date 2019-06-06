#!python3.7

import yampy
import random
import BingoBotConfig
import time

group_id = BingoBotConfig.group_id #as an int
access_token = BingoBotConfig.access_token #as a string
yammer = yampy.Yammer(access_token=access_token) #as a string
picked = {column:[] for column in 'BINGO'}

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

def display_called(dict=picked):
    '''Format the dict of called balls for human-readable printing.'''
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
    all_balls = display_called()
    m = yammer.messages.create(f'{ball[0]}{ball[1]}', group_id=group_id)
    replied_to_id = m['messages'][0]['thread_id']
    time.sleep(15)
    r = yammer.messages.create(all_balls, replied_to_id=replied_to_id)
