# -*- coding: utf-8 -*-
from fractions import Fraction
from math import sqrt, floor
LIMIT = 1000

def main ():
	wynik, hmaks = 0, 0
	for D in xrange (2, LIMIT+1):
		if int (sqrt( D))**2 == D:
			continue
		X = sqrt (D)
		r,s = Fraction (1), Fraction (0)
		a, h, k = [], [0,1],[1,0]
		while True:
			X = r * sqrt (D) + s
			a.append (Fraction (floor (X)))
#			X = Fraction(1) / (X - a[-1])
			r,s  =r/ (r**2*D - (s-a[-1])**2, (a[-1]-s)/(r**2*N - (s-a[-1])**2)
			h.append (a[-1]* h[-1] + h[-2])
			k.append (a[-1]* k[-1] + k[-2])
			print a [-1], h[-1],k[-1]
			if h[-1]**2 - D* k[-1]**2 == 1.0:
				print D, a
				if h[-1] > hmaks:
					hmaks = h[-1]
					wynik = D
				break
		
	print wynik

if __name__ == "__main__":
	main ()
