#-*- coding:utf-8 -*-
from string import maketrans
LIMIT = 1000000

def main ():
	naj = LIMIT
	jestPierwszy = [True]*LIMIT
	Pierwszy = []
	for c in range (2, LIMIT):
		if jestPierwszy [c]:
			Pierwszy.append (c)
			for d in range (2*c, LIMIT, c):
				jestPierwszy[d] = False
	for p in Pierwszy:
#		print p
		Tekst = str (p)
		for d in range (10):
			n = Tekst.count (chr (ord ('0')+d))
			if n > 0 and n % 3 == 0:
				v = 0
				nizszy = p
				for e in range (10):
					tlum = maketrans (char(d), char(e))
					prze = Tekst.translate(tlum)
					if jestPierwszy [int(prze)] and (e != 0 or prze[0] != char (e)):
						v += 1
						if prze < nizszy:
							nizszy = prze
				if v == 8 and nizszy < naj:
					naj = nizszy
	print naj	
def char (n):
	return chr (ord ('0')+n)

if __name__ == "__main__":
	main ()
