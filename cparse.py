#!/usr/bin/env python

import sys
from productions import Production

def main():
	# Check the command line arguments
	if len(sys.argv) != 2:
		print """Usage:
			./cparse productionsFile.txt """
		sys.exit(0)

	origGrammar = createAugmentedGrammar()
	print "Augmented Grammar\n-----------------"
	for prod in origGrammar:
		prod.printForGrammar()


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

if __name__ == "__main__":
	main()
