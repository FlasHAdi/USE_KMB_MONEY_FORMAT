''' 1. '''
# Add
USE_MONEY_K_FORMAT = True

if USE_MONEY_K_FORMAT:
	def FormatMoneyToK(string):
		moneyString = str(string)
		money = 0

		if 'k' in moneyString:
			if len(moneyString) > 1:
				money = int(moneyString.replace('k', '000'))
		elif 'K' in moneyString:
			if len(moneyString) > 1:
				money = int(moneyString.replace('K', '000'))

		return money
