# -*- coding:utf-8 -*-
from math import ceil
LIMIT = 100
fib = [1,1]
#A,B = "1415926535","8979323846"
A,B = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679", "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

def main ():
	for i in xrange (LIMIT):
		fib.append (fib[-1] + fib[-2])
	wyn  = 0
	for c in xrange (18):
		wyn += 10**c *cyfr ((127+19*c)*7**c)
	print wyn

def cyfr (n):
#	print n , len (A)
	n0,t = int(ceil(float( n) / len (A))), 0
	while fib[t] < n0: t+= 1
	while t >= 2:
#		print t, n0
		if n0 <= fib [t-2]:
			t = t-2
		else:
			n0 = n0 - fib [t-2]
			t = t-1
#	print t, n0
	if t == 0: return int (A [(n % len (A))-1])
	else: return int(B [(n % len (A))-1])

if __name__ == "__main__":
	main ()
