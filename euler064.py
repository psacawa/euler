# -*- coding: utf-8 -*-
from math import sqrt, floor
LIMIT = 10000 

def main ():
	wynik = 0
	for N in xrange (2, LIMIT+1):
		if int (sqrt(N))**2 != N:
			ciag = []
			m,l = 0,1
			a = floor (sqrt (N))
			while True:
				m,l = l*a-m,int ((N-m**2)/l)-l*a**2+2*m*a
				a = floor ((sqrt (N) + m)/l)
				if (m,l,a) in ciag:
					break
				ciag.append((m,l,a))
#			print N, ciag
			if len (ciag) % 2 == 1:
#				print N
				wynik += 1
	print wynik

if __name__ == "__main__":
	main ()
