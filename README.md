# BingoBot

A simple bot designed to generate bingo numbers (for standard 75-ball format) and post them to Yammer using [yampy](https://github.com/yammer/yam-python).

## Configuration

BingoBotConfig.py must contain the following user-specific values. A dummy file is included in this repo for reference.

1. group_id = *group_id (aka feed id) of Yammer group, as an int*
2. access_token = *developer access token generated at https://www.yammer.com/client_applications, as a str*

## Functionality

Call `start_game()` to start the script. Optional keyword argument `wait=` (default of 900 seconds) can be used to adjust the time between new numbers.

#### Basic program flow is as follows:

1. Check the current user to verify that the access token is valud.
1. Generate a legal letter/number combo.
1. Check that the letter/number combo is unique to the current game. If not, repick.
1. Once a unique combo has been generated, add it to the dictionary of already-picked numbers.
1. Send the new number with `yampy` as a new post to the specified group. Capture the `replied_to_id` of that post. 
1. Format the dictionary of already-picked numbers as a long string with newlines after each letter, and send it as a reply to the latest new number post.
1. `sleep()` for the amount of time specified before looping to `while`.

## To-do

* ~~Core gameplay functions~~ done
* File handling (save/load external dict in case of script interruption)
* Exception handling (connection errors, posting errors)
* Logging (and CPU time measuring if using PA -- see below)

Ideally, I learn enough Flask or Django to get this running completely web-based, with HTML input buttons. More likely I'll just put it up on [PythonAnywhere](https://www.pythonanywhere.com) as a strictly command-line script.
