#i -*- coding:utf-8 -*-
from math import log, exp, ceil, floor, e
from fractions import gcd

def main ():
	wyn = 0
	for N in range (5, 10001):
		lom = int (floor(N / e))
		if log (N) > (lom+1)*(log(lom+1)) - lom*log(lom): lom += 1
#		print -N if term (lom /gcd (N, lom)) else N
		wyn += -N if term (lom / gcd (N, lom)) else N
	print wyn

def f (N, r):
	return (N/r)**r

def term (n):
	while n % 2 == 0: n /= 2
	while n % 5 == 0: n /= 5
	return n == 1

if __name__ == "__main__":
	main ()
