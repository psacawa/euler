LIMIT = 10000

def main ():
	Pierwszy = []
	Tocjent = [0]*LIMIT
	jestPierwszy  = [True]*LIMIT
	for c in range(2,LIMIT-1):
		if jestPierwszy [c]:
			Pierwszy.append (c)
			d = 2
			while c*d < LIMIT:
				jestPierwszy[c*d] = False
				d +=1
	print len (Pierwszy)

if __name__ == "__main__":
	main ()


