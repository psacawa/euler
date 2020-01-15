#-*- coding:utf-8 -*-
import math
LIMIT = 1500000

def main ():
	razy = [0]*(LIMIT+1)
	for n in range(1, LIMIT):
		for m in range(n+1, LIMIT, 2):
			if nwd (m, n) == 1:
				p= 2*m*(m+n)
				if p > LIMIT: break
				for r in range (p, LIMIT+1, p):
					razy [r] += 1
		if 2*(n+1) > LIMIT: break
	jedynki = 0
	for c in range (1, LIMIT):
		if razy [c] == 1: jedynki += 1
	print (jedynki)


def nwd (m, n):
	return m if n == 0 else nwd (n, m % n)

if __name__ == "__main__":
	main ()
