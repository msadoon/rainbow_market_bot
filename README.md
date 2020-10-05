# Welcome to 🌈📈 Bot!

This is an elegant piece of software that does 1 of 2 things at 4:30 EDT (GMT -4) every weekday. It either prints 🌈🐻 when the S&P 500 index has had a negative day, or 🌈🐂 when it had a plus day. It sends this message to any group with a bot on Telegram.

# To Do

- scale emoji's by percentage gain/loss ✅
- add > 10% caption text.
- use ^GSPC as the ticker symbol instead of SPY to offset inaccuracy of dividend payoffs

# Files

## Where does the bot send messages?

The bot sends messages using this line of code.

	'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message


## How does it send messages:

When you create a bot on Telegram, you be given a **secure key** use that as your ``bot_token`` above.

The ``bot_chatID`` comes when you add the bot to a Telegram group and type ``/start`` in the group.

Use this command
	https://api.telegram.org/bot%3Cbot_token%3E/getUpdates

to find the ``chat: id`` in the returned JSON.
	
It'll look similar to this:

	> "update_id": ,
	"chat": **{**
	"id": **<use this number>**,
	"title": "",
	"type": "group",
	"all_members_are_administrators": **true**

## Other Resources

Here's all the resources I used to build this bot.

Not I used my NAS's DSM Task Scheduler to run the script every weekday at 4:30pm. Python also has a library called Schedule that will keep the script running but execute the function at any given interval (listed below).

https://pypi.org/project/schedule/

Install Python packages:
https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests

Main article I started with:
https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

How to run script on AWS (should be free tier):
https://aws.amazon.com/getting-started/hands-on/run-serverless-code/

How to schedule jobs on AWS lamba
https://docs.aws.amazon.com/eventbridge/latest/userguide/run-lambda-schedule.html
