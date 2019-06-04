import yampy
import random
import BingoBotConfig

access_token = BingoBotConfig.access_token
##yammer = yampy.Yammer(access_token=access_token)

already_called = []

def pick_number():
    picked = random.randint(1, 75)
    return f'{"BINGO"[(picked - 1) // 15]}{picked}'

