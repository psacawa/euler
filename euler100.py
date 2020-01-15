# -*- coding:utf-8 -*-
from math import sqrt

def main ():
	N, B = float (50), 35
#	N , B =10**12, 707106781180
	Ns = float (N)
	N0 , B0 = N*(N-1), 2*B*(B-1)
	while True:
		while 2*B*(B-1) < N0:
			B += 1
		B0 = 2*B*(B-1)
		if  B0 == N0:
		#	break
			print B, N, N/Ns
			Ns = N
			B+=1
		while B0 > N*(N-1):
			N += 1
		N0 = N*(N-1)
		if  B0 == N0:
#			break
			print B, N, N/Ns
			Ns = N
			N+=1
#		print B, N
	print N

if __name__ == "__main__":
	main ()
