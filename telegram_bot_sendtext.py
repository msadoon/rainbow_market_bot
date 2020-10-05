import re, requests
from io import BytesIO
from lxml import html
from PIL import Image
from emojipy import Emoji

def image(rawHTML):
	imageSource = html.fromstring(rawHTML)
	imageSourceURL = imageSource.xpath('//img[@class="emojione"]/@src')[0]
	response = requests.get(imageSourceURL)
	image = Image.open(BytesIO(response.content))

	return image

def rainbowImage():
	rawHTML = Emoji.to_image("\U0001F308")
	downloadedImage = image(rawHTML)

	return downloadedImage

def bearImage():
	rawHTML = Emoji.to_image("\U0001F43B")
	downloadedImage = image(rawHTML)

	return downloadedImage

def bullImage():
	rawHTML = Emoji.to_image("\U0001F402")
	downloadedImage = image(rawHTML)

	return downloadedImage

def mergeImages(image1, image2):
	(width1, height1) = image1.size
	(width2, height2) = image2.size

	result_width = width1 + width2
	result_height = max(height1, height2)

	result = Image.new('RGBA', (result_width, result_height))
	result.paste(im=image1, box=(0, 0))
	result.paste(im=image2, box=(width1, 0))

	return result

def imageBytes(image):
	buffer = BytesIO()
	image.save(buffer, 'png')
	buffer.seek(0)
	image_bytes = buffer.read()
	buffer.close()

	return image_bytes

def scale(percentChange):
	#0.0 == 0.25 // increment scale by 0.075 for every 1% change up to 10%
	#5.0 == 0.625
	#10.0 == 1.0
	# effectively scales from 0 - 10% - anything higher is an huge historical outlier.
	# https://en.wikipedia.org/wiki/List_of_largest_daily_changes_in_the_S%26P_500_Index
	constant = 0.075
	baseScale = 0.25
	maxScale = 1.0

	if percentChange <=0:
		total = baseScale
	elif percentChange >= 0.10:
		return maxScale
	else:
		multiplier = percentChange * 100
		modifier = multiplier * constant
		total = modifier + baseScale

	return total

def resize(image, percentChange):
	(width, height) = image.size
	scaledPercentChange = scale(percentChange)
	size = ((width*scaledPercentChange, height*scaledPercentChange))
	
	image.thumbnail(size)

	(resizedWidth, resizedHeight) = image.size

	center = ((int(round((width - resizedWidth)/2)), int(round((height - resizedHeight)/2))))

	backgroundImage = Image.new('RGBA', (width, height))
	backgroundImage.paste(image, center)

	return backgroundImage

def telegramBotSendImage(image):
	bot_token = ''
	bot_chatID = ''
	send_image_url = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto?chat_id=' + bot_chatID
	(width, height) = image.size
	imageData = imageBytes(image)

	#image.show()
	requests.post(send_image_url, files=dict(photo=imageData, width=width, height=height))

def sendRainbowImage():
	finhubbSPYQuote = "https://finnhub.io/api/v1/quote?symbol=SPY&token=bs6hkvvrh5rdv3m3os40"
	response = requests.get(finhubbSPYQuote)
	baseImage = rainbowImage()

	json = response.json()
	prevClose = json["pc"]
	close = json["c"]

	if prevClose >= close:
		indicatorImage = bearImage()
		scale = ((prevClose - close) / prevClose)
		combinedImage = mergeImages(baseImage, indicatorImage)
	elif prevClose < close:
		indicatorImage = bullImage()
		scale = ((close - prevClose) / prevClose)
		combinedImage = mergeImages(baseImage, indicatorImage)

	scaledImage = resize(combinedImage, scale)

	telegramBotSendImage(scaledImage)

sendRainbowImage()
