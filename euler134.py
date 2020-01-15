# -*- coding:utf-8 -*-
from math import log,ceil
LIMIT = 1000004

def main ():
	t = [True]* LIMIT
	pier = []
	for c in range (2, LIMIT):
		if t[c]:
			pier.append(c)
			for d in range (2*c, LIMIT, c): t[d] = False
	wyn = 0
	for c in range (2, len(pier)-1):
		D = 10**int(ceil(log (pier[c],10)))
		C = odwroc (D, pier[c+1])
		E = (odwroc (D, pier[c+1])*(pier[c+1]-pier [c])) % pier[c+1]
#		print pier[c], pier[c+1],"-", D, C,  E, E*D + pier[c]
		wyn += E*D + pier[c]
	print wyn


def odwroc (n, p):
	p0 = p
	s, t= [1, 0],[0,1]
	while p != 0:
		q, r = n//p, n% p
		s.append (s[-2]-q*s[-1])
		t.append(t[-2]-q*t[-1])
		n,p = p, r
	return s[-2] if s[-2] > 0 else s[-2]+p0
	

if __name__ == "__main__":
	main ()
