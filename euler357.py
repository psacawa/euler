# -*- coding:utf-8 -*-
import numpy as np
LIMIT = 100000000
pier = []

def main ():
	jp = [True] *(LIMIT // 2)
	for c in range (2, LIMIT//2):
		if jp[c]:
			pier.append(c)	
			for d in range (2*c, LIMIT//2, c):
				jp[d] = False
	print len (pier)
#	wyn = rek (1, 0, 2)
	
	
def rek (i,  obec, n ):
	print i,obec, n
	if i == len (pier):
		return 0
	if (n > LIMIT):
		return 0
	wyn = jgen (n)
	for j in range (i, len(pier)):
		wyn += rek (j+1, obec+1, n*pier[j])
	return wyn

	

if __name__ == "__main__":
	main ()
