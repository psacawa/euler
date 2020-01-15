import math
import numpy as np
LIMIT = 10**15

def main ():
	mag = []
	for b in xrange (2, 135):
		x = b**2
		while x < LIMIT:
			if cyfsuma (x) == b:
				mag.append (x)
			x *= b
	mag.sort ()
	print mag[-1]
			
		

def cyfsuma (n):
	wyn = 0
	while n != 0:
		wyn += n % 10
		n = n // 10
	return wyn
		

if __name__ == "__main__":
	main ()
