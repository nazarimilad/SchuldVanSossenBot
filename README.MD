## Description

This bot is a Reddit bot which automatically add a "Het is de schuld van de sossen!"-comment to any post in /r/Belgium identified by one of more provided keywords

## Usage

1. Authentification configuration: Put your Reddit credentials in the 'examplepraw.ini'-config file. After this, rename the config file to just 'praw.ini'
2. Optional personalisation: You can personalize the message of the bot by changing the message variable in the bot.py file. The same applies to the keywords.

To run the script only once, run `python bot.py` in the same folder as where the bot.py script is located.

To automate it (to actually use it as a bot), you can use crontab on Linux.

