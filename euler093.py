# -*- coding:utf-8 -*-
from sets import Set
from fractions import Fraction

def main ():
	mozliwe = {c: [c] for c in range (1, 10)}
	lep, wyn = 0,0
	for a in range (1, 10):
		for b in range (1, 10):
			mozliwe [10*a+b] = wymysl (a, b)
	for a in range (1, 10):
		for b in range (1, 10):
			for c in range (1,10):
				if cyf([a,b,c]) not in mozliwe:
						mozliwe [cyf ([a,b,c])] = Set([])
				for x in mozliwe [a]:
					for y in mozliwe [cyf([b,c])]:
						mozliwe [cyf([a,b,c])] |= wymysl (x,y)		
	for a in range (1, 10):
		for b in range (1, 10):
			for c in range (1,10):
				for d in range (1, 10):
					if cyf([a,b,c,d]) not in mozliwe:
						mozliwe [cyf([a,b,c,d])] = Set([])
					for x in mozliwe [a]:
						for y in mozliwe [cyf([b,c,d])]:
							mozliwe [cyf([a,b,c,d])] |= wymysl (x, y)
					for x in mozliwe [cyf([a,b])]:
						for y in mozliwe [cyf([c,d])]:
								mozliwe [cyf([a,b,c,d])] |= wymysl (x,y)
#	print mozliwe
	for a in range (1, 10):
		for b in range (a+1, 10):
			for c in range (b+1,10):
					for d in range (c+1, 10):
						k = cyf ([a,b,c,d])
						l = 0
						while l+1 in mozliwe [k]: l += 1
						if l > lep:
							lep = l
							wyn =k
	print wyn
					
def cyf (L):
	L.sort()
	wyn = 0
	for c in L:
		wyn = 10*wyn + c
	return wyn

def wymysl (a , b ):
	wyn = Set([a+b,abs(a-b), a*b])
	if b != 0 : wyn |= Set ([Fraction (a,b)])
	if a != 0 : wyn |= Set ([Fraction (b,a)])
	return wyn

if __name__ == "__main__":
	main ()
