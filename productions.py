import re, sys

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
		return RHS[placeholderPos + 1]

	def __str__(self):
		printRHS = list(self.RHS)
		printRHS.insert(self.placeholderPos, '@')
		return "%s->%s" % (self.LHS, ''.join(printRHS))
	
	def printForGrammar(self):
		sys.stdout.write("%s->%s" % (self.LHS, self.RHS))

