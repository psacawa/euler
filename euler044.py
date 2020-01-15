import numpy as np
import math

def main ():
	for d in xrange (1, 5000):
		D = P (d)
		for q in xrange (5000):
			Q = P (q)
			if Q > 2*D: break
			if jestPieciokatny (Q-D) and jestPieciokatny(Q+D):
				print D, Q

def P (n):
	return n*(3*n-1)//2

def jestPieciokatny (p):
	if p <= 0: return False
	f = (1 + math.sqrt (1 + 24*p))/6
	n = round (f)
	return (n*(3*n-1)/2 == p)

if __name__ == "__main__":
	main ()
