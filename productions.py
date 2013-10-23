import re, sys, copy

class Production:
	""" Stores information about grammar productions """
	LHS = "" 
	RHS = "" 
	placeholderPos = 0

	def __init__(self, grammarString):
		# Remove newline characters from productions
		grammarString = grammarString.strip('\n')

		# Split the productions into LHS and RHS
		splitString = re.split("->", grammarString)
		if(len(splitString) == 1):
			self.LHS = "'"
			self.RHS = splitString[0]
		elif(len(splitString) == 2):
			self.LHS = splitString[0]
			self.RHS = splitString[1]
		else:
		 	errorMessage = "Production '%s' has too many '->'" % grammarString
		 	raise Exception(errorMessage)
	
	def charFollowingPlaceholder(self):
		return self.RHS[self.placeholderPos + 1]

	def goto(self, symbol):
		if(self.charFollowingPlaceholder() == symbol):
			#create a copy of the current production	
			prodToReturn = copy.deepcopy(self)
			prodToReturn.placeholderPos += 1
			return prodToReturn
		else:
			return null

	def __str__(self):
		printRHS = list(self.RHS)
		printRHS.insert(self.placeholderPos, '@')
		return "%s->%s" % (self.LHS, ''.join(printRHS))

	def __eq__(self, other):
		if not isinstance(other, Production):
			return false

		return ((self.LHS == other.LHS) and
			(self.RHS == other.RHS) and
			(self.placeholderPos == other.placeholderPos))
	
	def stringForGrammar(self):
		return "%s->%s\n" % (self.LHS, self.RHS)

