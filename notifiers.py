# Each notifier class should have a notify() method

import gntp.notifier

class Growl():
	def notify(self):
		growl = gntp.notifier.GrowlNotifier(
			applicationName="Don't Forget Lunch!",
			notifications=['reminder']
		)

		growl.register()

		growl.notify(
			noteType='reminder',
			title="Don't Forget Lunch!",
			description="Looks like you haven't ordered lunch yet... better hurry!"
		)

