import datetime

import creds

import requests
from bs4 import BeautifulSoup

payload = {
	'username': creds.username,
	'password': creds.password
}

# Create a connection
with requests.session() as c:
	# Login
	c.post('https://www.seamless.com/food-delivery/login.m', data=payload)

	# Grab order history
	request = c.get('https://www.seamless.com/OrderHistory.m?vendorType=1')

	# Parse order history HTML to grab latest order date
	soup = BeautifulSoup(request.text)
	last_order_date = soup.find_all('td', class_='first date')[0].strong.text
	
	today = '{dt.month}/{dt.day}/{dt.year}'.format(dt=datetime.datetime.now())

	if last_order_date != today:
		print 'YOU HAVENT ORDERED TODAY!!'
	else:
		print 'you cool'
