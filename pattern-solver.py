#!/usr/bin/python
import sys
import getopt

class pattern:
	def __init__(self, hintsString):
		self._canGoOn = True
		self.loadHintsFromString(hintsString)
		self._iter = 0
	
	def solve(self):
		print "iteration %i:"%self._iter;
		self._iter = self._iter +1
		self._canGoOn = False
		
	def loadHintsFromString(self, hintsString):
		hints = hintsString.split('/')
		nbHints = len(hints)
		self.hintsX = [hint.split('.') for hint in hints[0:nbHints/2]]
		self.hintsY = [hint.split('.') for hint in hints[nbHints/2:nbHints]]
		
	def canGoOn(self):
		return self._canGoOn
	
	def getAscii(self):
		lines = []
		maxHintsX = max([len(hint) for hint in self.hintsX])
		maxHintsY = max([len(hint) for hint in self.hintsY])
		for y in range(0,maxHintsX):
			line = ' ' * maxHintsY
			for hintX in self.hintsX:
				if len(hintX)>=(maxHintsY-y):
					line += hintX[len(hintX)-maxHintsY+y]
				else:
					line += ' '
			lines.append(line)
		for hintY in self.hintsY:
			line = ''
			for x in range(0,maxHintsY):
				if len(hintY)>=(maxHintsY-x):
					line += hintY[len(hintY)-maxHintsY+x]
				else:
					line += ' '
			lines.append(line)
		return lines
	
	def printAscii(self):
		for line in self.getAscii():
			print line


def main():
    solver=pattern("2/1.3/3.2/3.3/5.1.1/1.4/5.1/1.3/2.4.1/1.3/9/3.1.1/3.1/1.3/6/1.3/1.2/1.3/4.1.1/5")
    while (solver.canGoOn()):
		solver.printAscii()
		solver.solve()

if __name__ == "__main__":
    main()
