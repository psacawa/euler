# -*- coding:utf-8 -*-
from math import sqrt
from fractions import gcd
LIMIT = (10**9-1)/3

def main ():
	wyn =0
	for m in range (2,int (sqrt(LIMIT))):
		for n in range ((m%2==0), m, 2):
			if gcd (m, n) == 1:
				a,b = m**2 + n**2, min (m**2-n**2, 2*m*n)
				if 2*(a+b) > 10**9:
					break
				if (a - 2*b)**2 == 1 and 2*(a+b) <= 10**9:
					wyn += 2*(a+b)
	print wyn

if __name__ == "__main__":
	main ()
