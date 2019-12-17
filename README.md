# BingoBot

A simple bot designed to generate valid bingo letter-numbers (for standard 75-ball format) and post them to Yammer using [yampy](https://github.com/bghull/yam-python).

## Configuration

Create a `config.py` file from the dummy provided:

1. group_id = *group_id (aka feed id) of Yammer group, as an int*
2. access_token = *developer access token generated at https://www.yammer.com/client_applications, as a str*

Call `start_game()` (optional `wait` parameter defaults to 15 minutes) to begin posting.

## Considerations

Yampy is installed from a fork of the GitHub repo because PyPi is not updated for Python 3 support.