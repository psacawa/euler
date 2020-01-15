# -*- coding:utf-8 -*-
from fractions import Fraction 
# no niby wszystko gra, tylko odpowiedź nie właściwa; przyczyna nieznana

def main ():
	t = [True] * 501
	str = "PPPPNNPPPNPPNPN"
	pierwszy = []
	for c in range (2, 501):
		if t[c]:
			pierwszy.append(c)
			for d in range (2*c, 501, c):
				t[d] = False
	t[1] = False
	print pierwszy
	lpier, lzloz = len (pierwszy), 500-len(pierwszy)
	praw = [[Fraction (0,1)]*501 for c in range (15)]
	for c in range (1, 500+1):
		praw [0][c] = Fraction (2, 1500) if t[c] else Fraction (1, 1500)
#		praw [0][c] = Fraction (2, lpier+500) if t[c] else Fraction (1, lpier+500)
	for e in range (1, len(str)):
		praw [e][1] = praw [e-1][2] * wspol (str[e], t[1])*Fraction (1,2)
		praw [e][2] = praw[e-1][1]*wspol (str[e], t[2]) + praw [e-1][3]* wspol(str[e], t[2])*Fraction (1,2)
		praw [e][500] = praw [e-1][499] *wspol (str[e], t[500])*Fraction (1,2)
		praw [e][499] = praw[e-1][498]*wspol (str[e], t[499])*Fraction (1,2) + praw [e-1][500]* wspol(str[e], t[499])
		for c in range (3, 499):
			praw [e][c] = (praw[e-1][c-1]*wspol (str[e], t[c]) + praw [e-1][c+1]* wspol(str[e], t[c]))*Fraction (1,2)
	wyn = Fraction (0,1)
	for c in range (1, 500 + 1):
		wyn += praw [14][c]
	print wyn
	for c in range (490, 501):
		print c, praw [0][c], praw [1][c]

def wspol (liter, pierwszosc):
	return Fraction (2,3) if ((pierwszosc and liter == "P") or (~pierwszosc and liter == "N")) else Fraction (1,3)

if __name__ == "__main__":
	main ()
