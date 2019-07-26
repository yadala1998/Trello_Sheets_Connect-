class sheetRow:
	def_init_(self, rowNumber, cardName, description, label):
		self.rowNumber = rowNumber
		self.cardName = cardName
		self.description = description
		self.label = label

	def getRowNumber(self):
		return self.rowNumber

	def getCardName(self):
		return self.cardName

	def getDescription(self):
		return self.description

	def getLabel(self):
		return self.label
	
