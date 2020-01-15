#-*- coding:utf-8 -*-

import numpy as np

def main ():
	s = np.zeros((1000,1000))
	t = 0
	for c in range (1000):
		for d in range (c):
			t = (615949*t +797807) % (2**20)
			s[c,d] = t - 2**19	
	suma = np.zeros ((1000,1000,1000))
	baza = np.zeros ((1000,1000,1000)) 
	for c in range (1000):
		print c
		for d in range (c+1):
			baza [c,d,0] = s[c,d]
			suma [c,d,0] = s[c,d]
			for r in range (1,c-d):
				baza[c,d,r] = baza[c,d,r-1] + s[c,d]
	print "przeszło"
	naj = 0
	for w in range (1, 1000):
		for c in range (1000-w):
			for d in range (c+1):
				suma [c,d,w] = suma [c,d,w-1] + baza [c+w,w-1]
				if suma [c,d,w] > naj:
					naj = suma[c,d,w]
	print naj	

if __name__ == "__main__":
	main ()
