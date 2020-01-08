''' 1. '''
# Add import
import constInfo

''' 2. ENABLE_CHEQUE_SYSTEM '''
# Search @ def OnAccept
			money_text = self.pickValueEditLine.GetText()

# Add below
			if constInfo.USE_MONEY_K_FORMAT:
				if 'k' in money_text or 'K' in money_text::
					money_text = str(constInfo.FormatMoneyToK(money_text))


''' 3. '''
# Search @ def OnAccept
			text = self.pickValueEditLine.GetText()

# Add below
			if constInfo.USE_MONEY_K_FORMAT:
				if 'k' in text or 'K' in text::
					text = str(constInfo.FormatMoneyToK(text))
