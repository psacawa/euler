# -*- coding:utf-8 -*-

def main ():
	wart = [0]*250250
	S = [[0]* 250 for c in xrange (250250)]
	for n in range (250250):
		wart [n] = exp (n+1,n+1)
		print n+1, wart[n]
	print wart[0: 5]
	
def exp (b, p):
	b = b % 250
	wyn = 1
	while p != 0:
		wyn = wyn *(b**(p%2)) %250
		b = b**2
		p //= 2
	return wyn

if __name__ == "__main__":
	main ()
