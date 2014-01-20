import datetime
import importlib
import sys
# --
import creds
# --
from bs4 import BeautifulSoup
import requests

active_notifiers = [
	'Growl',
]

# Create a connection
with requests.session() as c:
	# Login
	c.post('https://www.seamless.com/food-delivery/login.m', data={
		'username': creds.username,
		'password': creds.password
	})

	# Grab order history
	request = c.get('https://www.seamless.com/OrderHistory.m?vendorType=1')

	# Parse order history HTML to grab last order date
	soup = BeautifulSoup(request.text)
	try:
		last_order_date = soup.find_all('td', class_='first date')[0].strong.text
	except Exception as e:
		# If last_order_date couldn't be grabbed, it's likely that the login 
		# process didn't work - double check your credentials!
		sys.exit()

	# Grab today's date in the same format Seamless uses so you can compare
	today = '{dt.month}/{dt.day}/{dt.year}'.format(dt=datetime.datetime.now())

	if last_order_date != today:
		# Nofify
		notifiers_mod = importlib.import_module('notifiers')
		for notifier in active_notifiers:
			try:
				class_ = getattr(notifiers_mod, notifier)
				n = class_()
				n.notify()
			except Exception as e:
				pass