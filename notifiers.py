# Each notifier class should have a notify() method

class Growl():
	def __init__(self):
		print 'growl init'

	def notify(self):
		print 'notify:growl'

class Email():
	def __init__(self):
		print 'email init'

	def notify(self):
		print 'notify:email'
