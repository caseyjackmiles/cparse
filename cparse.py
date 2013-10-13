#!/usr/bin/env python

import sys
from productions import Production

def main():
	# Check the command line arguments
	if len(sys.argv) != 2:
		print """Usage:
			./cparse productionsFile.txt """
		sys.exit(0)

	# Read in the original grammar
	# and augment it
	origGrammar = createAugmentedGrammar()

	print "Augmented Grammar\n-----------------"
	for prod in origGrammar:
		sys.stdout.write(prod.stringForGrammar())

	print "============================="
	grammarSymbols = retrieveAllGrammarSymbols()
	


def createAugmentedGrammar():
	grammar = list()
	with open(sys.argv[1], 'r') as grammarFile:
		for line in grammarFile.readlines():
			# Create a new Production instance for each line
			try:
				newProd = Production(line)
			except Exception, e:
				print "Error: %s" % e
				sys.exit(0)
			grammar.append(newProd)
	grammarFile.close()

	return grammar

def retrieveAllGrammarSymbols():
	grammarSymbols = list()
	with open(sys.argv[1], 'r') as grammarFile:
		for line in grammarFile.readlines():
			line = line.strip('\n')
			# Get the position of the first '->'
			i = line.find("->")			
			if(i == -1):
				continue
			else:
				symbolsFromLine = list(line[:i]) + list(line[i+2:])

				for symbol in symbolsFromLine:
					if symbol not in grammarSymbols:
						grammarSymbols.append(symbol)

	grammarFile.close()

	return grammarSymbols

if __name__ == "__main__":
	main()
