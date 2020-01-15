# -*- coding:utf-8 -*-
from fractions import Fraction

def main ():
	a,b = 1.001,1.01
	for r in xrange (1000):
		X = s ((a+b)/2, 5000)
		if X > -6*10**11:
			a = (a+b)/2
		else:
			b = (a+b)/2
	print "%.12f" %  a

def s (r, N):
	return (900*(r**N-1)* (r-1) - 3 * ((r*N-N - 1) * (r**N)+1))/ (r-1)**2


if __name__ == "__main__":
	main ()
