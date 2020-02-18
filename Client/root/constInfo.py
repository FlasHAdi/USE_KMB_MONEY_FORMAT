''' 1. '''
# Add
USE_KMB_MONEY_FORMAT = True

if USE_KMB_MONEY_FORMAT:
	def __ConvertMoneyText(self, text, powers = dict(k = 10**3, m = 10**6, b = 10**9)):
		"""
		Format string value in thousands, millions or billions.

		'1k' = 1.000
		'100kk' = 100.000.000
		'100m' = 100.000.000
		'1b' = 1.000.000.000
		'1kmb' = 1.000 (can't use multiple suffixes types)

		:param text: string
		:return: int
		:date: 10.01.2020
		:author: Vegas
		"""

		match = re.search(r'(\d+)({:s}+)?'.format('+|'.join(powers.keys())), text, re.I)
		if match:
			moneyValue, suffixName = match.groups()
			moneyValue = int(moneyValue)
			if not suffixName:
				return moneyValue

			return moneyValue * (powers[suffixName[0]] ** len(suffixName))

		return 0
