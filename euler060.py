# -*- coding:utf-8 -*-
import numpy as np
import math
LIMIT = 100000000
WLIMIT = 1229

def main ():
	p,pierwszy,ob,na = [True]*LIMIT, [], [],[]
	for i in xrange (2, LIMIT):
		if p[i]:
			pierwszy.append(i)
			for j in range (2*i, LIMIT, i):
				p [j] = False
	ob = [set ([c]) for c in pierwszy[0:WLIMIT]]
	for s in range (2, 6):
		for c in xrange (len (ob)):
			for d in xrange (c+1, len(ob)):
				if len (ob [c] | ob [d]) == s and ob[c] | ob [d] not in na:
					abort = False
					for x in ob[c]:
						for y in ob[d]:
							if x !=y and ( not przyj (x, y, pierwszy) or not przyj (y, x, pierwszy)): 
								abort =True
								break
						else: continue
						break
					if s > 2: print ob [c] | ob [d], abort
					if not abort :
						na.append (ob[c]| ob[d])
		print na
		ob = na
		na = []  
	wyn = LIMIT
	for X in ob:
		if sum (X) < wyn:
			wyn = sum (X)
	print wyn

def bs (L, n):
	a, b = 0, len (L)
	while a < b:
		if L[(a+b)//2] == n: return True
		elif L [(a+b)//2] > n: b = (a+b)//2
		elif L [(a+b)//2] < n: a = (a+b)//2+1
	return False

	

def przyj (p, q, pierwszy):
	return bs (pierwszy, int (str(p) + str (q)))
	

if __name__ == "__main__":
	main ()
