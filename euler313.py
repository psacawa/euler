# -*- coding:utf-8 -*-
import math
LIMIT = 100

def main ():
	wynik = 0
	jp = [True]*LIMIT
	wart = []
	for c in xrange (2, LIMIT):
		if jp[c]:
			wart.append(c**2)
			for d in xrange (2*c, LIMIT, c):
				jp[d] = False
	for r in wart:
		wynik += int # cholera
		
	print wynik
	
def S (m, n):
	m, n = max(m, n), min (n, m)
	return 8*n-11 if (m ==n) else 9*m-n-16

if __name__ == "__main__":
	main ()
