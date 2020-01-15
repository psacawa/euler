# -*- coding:utf-8 -*-
import numpy as np

def main ():
    wynik = 0
    plik = open("p096_sudoku.txt")
    for i in xrange (50):
        plik.readline()
        S = np.zeros ((9,9), dtype = int)
        for c in xrange (9):
            str = plik.readline()
            for d in xrange (9):
                S[c,d] = ord (str[d])-ord ('0')
        Rozwiaz(S)
    plik.close ()

def Rozwiaz (S):
    """
    while nie skonczony:
        Naiwny 
        for cyfry i pozycje 
            for możliwości:
                naiwny (S+modyfikacja)
            if jeden nie sprzeczny:
                przyjąć
                break + continue
            
    """
    zajete,dost,rz_wolny, ko_wolny, kw_wolny,po_wolny = Dostepnosc (S)
    while zajete != 81:
        zajete = Naiwny (S, zajete, dost, rz_wolny, ko_wolny, kw_wolny,po_wolny)
        #print S,zajete
        if zajete != 81: print S
        for cyf in range (1,10):
        break
        


def Naiwny (S, zajete, dost, rz_wolny, ko_wolny, kw_wolny, po_wolny):
    # główna pętla
    while True:
        x,y = 0,0
        for cyf in range (1,10):
            for c in range (9):
                if rz_wolny[cyf][c] == 1 or 
                ko_wolny[cyf][c] == 1 or
                kw_wolny[cyf][c] == 1 or
                po_wolny[cyf-1,c]:
                    anom = 0             # część obrzydliwego haku
                    if rz_wolny[cyf][c] == 1:
                        for d in range (9):
                            if dost[cyf][c,d]:
                                x,y = c,d
                                break
                    elif ko_wolny[cyf][c] == 1:
                        for d in range (9):
                            if dost[cyf][d,c]:
                                x,y = d,c
                                break
                    elif kw_wolny [cyf][c] == 1:
                        for d in range (9):
                            if dost [cyf][3*(c//3)+(d//3), 3*(c%3)+ (d%3)]:
                                x,y = 3*(c//3)+(d//3), 3*(c%3)+ (d%3)
                                
                                break
                    elif po_wolny [cyf-1,c] == 1: # ten ostatni to tani hak
                        for d in range (1,10):
                            if dost[d][cyf-1,c] :
                                x,y = cyf-1,c
                                anom = d
                                break
                    S[x,y] = d if d else cyf
                    zajete += 1
#                    print "x, y, cyfra = ", x, y, cyf
                    break
            else: continue
            break
        else: break
# uaktualnij dostępność
        for cyf in range (1,10):
            dost[cyf][x,y] = False
        for e in range (9):
            dost [S[x,y]][x,e] = False
            dost [S[x,y]][e,y] = False
            dost [S[x,y]][3*(x//3)+(e//3), 3*(y//3)+ (e%3)]= False
        rz_wolny = [[0]*9 for i in range (10)]
        ko_wolny = [[0]*9 for i in range (10)]
        kw_wolny = [[0]*9 for i in range (10)]
        for cyf in range (1, 10):
            for e in range (9):
                for f in range (9):
                    rz_wolny [cyf][e] += dost[cyf][e,f]
                    ko_wolny [cyf][e] += dost[cyf][f,e]
                    kw_wolny [cyf][e] += dost [cyf][3*(e//3)+(f//3), 3*(e%3)+ (f%3)]
# sprawwdź niesprzeczność
        for c in range (9):
            for d in range (9):
                if S[c,d] == 0:
                    mozna = False
                    for cyf in range (1,10):
                        if dost[cyf][c,d]:
                            mozna = True
                            break
                    if not mozna:
                        return -1
    return zajete

def Dostepnosc (S):
    zajete = 0
    dost = [np.matrix (([True]*81)).reshape ((9,9)) for i in range (10)]
    for c in range (9):
        for d in range (9):
            if S[c,d] != 0:
                for cyf in range (1,10):
                    dost[cyf][c,d] = False
    wyst = [0]*10
    rz_wolny = [[0]*9 for i in range (10)]
    ko_wolny = [[0]*9 for i in range (10)]
    kw_wolny = [[0]*9 for i in range (10)]    
    po_wolny = 9*np.matrix(np.ones ((9,9)),dtype = int)
    for cyf in xrange (1,10):
        for x in xrange (9):
            for y in xrange (9):
                if S[x,y] == cyf:
                    zajete += 1
                    dost [cyf][[x],:] = np.matrix([False]*9)
                    dost [cyf][:,[y]] = np.matrix([False]*9).T
                    for e in range (9):
                        dost[cyf][3*(x//3) + e%3, 3*(y//3) + e//3] = False    
                wyst[cyf] += dost[cyf][x,y]
        for e in range (9):
            for f in range (9):
                rz_wolny [cyf][e] += dost[cyf][e,f]
                ko_wolny [cyf][e] += dost[cyf][f,e]
                kw_wolny [cyf][e] += dost [cyf][3*(e//3)+(f//3), 3*(e%3)+ (f%3)]
                po_wolny [e,f] += dost[cyf][e,f]
    return zajete, dost,rz_wolny, ko_wolny, kw_wolny,po_wolny


if __name__ == "__main__":
    main ()
