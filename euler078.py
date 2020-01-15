# -*- coding:utf-8 -*-
LIMIT = 10^1
p = [[None]*(c+1) for c in range (LIMIT)]

def main ():
	print p
	for c in range (7):
		print ewal (c,c)
	

def ewal (n, k):
	global p
	if p[n][k] != None:
		return p[n][k]
	if k == 1:
		p[n][k] = 1
	else:
		wyn = 0
		for k in range (1, n):
			wyn += ewal (n-k, k)
		p[n][k] = wyn
	return p[n][k]

if __name__ == "__main__":
	main ()
