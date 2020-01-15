#-*- coding:utf-8 -*-
from operator import mul
p = 2
L = 10**9+1

def arny (N , b):
	wyn = []
	while N != 0:
		wyn.append( N % b)
		N = N // b
	return wyn[::-1]

def main (p, L):
	wyn = 0
	X = arny (L, p )
#	print X
	for c in range(len(X)):
		X[c] += 1
	for c in xrange (len(X)):
		wyn += reduce (mul, X[0:c], 1)*X[c]*(X[c]-1)//2* (p*(p+1)//2)**(len(X)-c-1)
#		print reduce (mul, X[0:c], 1)*X[c]*(X[c]-1)//2* (p*(p+1)//2)**(len(X)-c-1)
	return wyn	


if __name__ == "__main__":
#	for c in range (10):
#		print main (p, c)
	print main (7, 10**9)
