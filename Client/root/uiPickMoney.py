''' 1. '''
# Add import
import constInfo

''' 2. ENABLE_CHEQUE_SYSTEM '''
# Search @ def OnAccept
			money_text = self.pickValueEditLine.GetText()

# Add below
			if constInfo.USE_KMB_MONEY_FORMAT:
				if money_text:
					moneyValue = min(constInfo.__ConvertMoneyText(text), self.maxValue)
					if moneyValue:
						if self.eventAccept:
							self.eventAccept(moneyValue)

''' 3. '''
# Search @ def OnAccept
			text = self.pickValueEditLine.GetText()

# Add below
			if constInfo.USE_KMB_MONEY_FORMAT:
				if text:
					moneyValue = min(constInfo.__ConvertMoneyText(text), self.maxValue)
					if moneyValue:
						if self.eventAccept:
							self.eventAccept(moneyValue)
