#-*- coding:utf-8 -*-
import math

def main ():
	plik = open ("p098_words.txt").read()
	slownik = [[] for i in xrange (20)]
	i = -1
	while i < len (plik):
		nast = plik[i+1:].find(',') 
		if (nast == -1): nast = len(plik) ; 
		else: nast += i+1
		#print i, nast
		slowo = plik[i+2: nast -1]
		i = nast
		slownik[len(slowo)].append(slowo)
	anagram = [[] for i in xrange (20)]
	for l in xrange (20):
			for v in slownik[l]:
				syg = alf_spek (v)
				for s,b in anagram[l]:
					if s== syg:
						b.append (v)
						break
				else:
					anagram[l].append((syg,[v]))
	naj = 0
	for l in xrange (5,20):
		for syg,sl in anagram[l]:
			if len (sl) >= 2:
				S = map (struk_spek, sl)
				for n in xrange (int (math.ceil(math.sqrt (10**(l-1)))),int (math.ceil(math.sqrt (10**l)))):
					if struk_spek (str (n**2)) == S[0]:
						proba = tlumacz (sl[0], sl[1], str(n**2))
						if kwadrat (int(proba)) and proba[0] != '0':
							naj = max (naj, n**2, int(proba))
	print naj

def kwadrat (n ):
	return  int(math.sqrt(n))**2 == n
				
def alf_spek (slowo):
	wynik = [0]*26
	for c in xrange (26):
		wynik[c] = slowo.count (chr(c+ord('A')))
	return wynik

def struk_spek (slowo):
	n = 0
	widz = []
	wynik = []
	for c in slowo:
		if c not in widz:
			widz.append(c)
		wynik.append(widz.index(c))
	return wynik

def tlumacz (stare, nowe, klucz):
	ret = ""
	for c in nowe:
		ret += klucz [stare.find(c)]
	return ret

if __name__ == "__main__":
	main ()
