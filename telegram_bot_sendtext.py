import requests

def getSP500Index():
	finhubbSPYQuote = "https://finnhub.io/api/v1/quote?symbol=SPY&token=bs6hkvvrh5rdv3m3os40"
	response = requests.get(finhubbSPYQuote)

	json = response.json()
	openValue = json["pc"]
	closeValue = json["c"]

	rainbowMarket = "🌈"

	if openValue > closeValue:
		rainbowMarket = "🌈🐻"
	elif openValue < closeValue:
		rainbowMarket = "🌈🐂"

	telegram_bot_sendtext(rainbowMarket)

def telegram_bot_sendtext(bot_message):
	bot_token = ''
	bot_chatID = ''
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)


getSP500Index()
