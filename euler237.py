#!/usr/bin/env python3.7

import sys
import numpy as np


def main(N):
    cur = {"4c": 1, "14": 1, "12": 0, "34": 0, "23": 0, "4o": 0}
    for i in range(N - 1):
        new = {
            "4c": cur["4c"] + cur["12"] + cur["34"],
            "4o": cur["4o"] + cur["14"],
            "12": cur["4o"] + cur["14"],
            "34": cur["4o"] + cur["14"],
            "14": cur["12"] + cur["34"] + cur["4c"] + cur["23"],
            "23": cur["14"],
        }
        new = {k: v % 10 ** 8 for k, v in new.items()}
        cur = new
        #  print (cur)
    print(cur["14"])


def mod_pow(b: np.ndarray, e):
    """Potęga kwadratowej macierzy"""
    base = b.copy()
    result = np.identity(b.shape[0])
    for i in reversed(format(e, "b")):
        if i == "1":
            result = np.matmul(result, base).astype (int) % (10 ** 8)
        #  print (base)
        base = np.matmul(base, base).astype (int) % (10 ** 8)
    return result.astype(int)


if __name__ == "__main__":
    N = int (sys.argv [1]) if len(sys.argv) > 1 else 10**12
    #  main(N)

    #  cur = [
    #      "4c",
    #      "4o",
    #      "14",
    #      "12",
    #      "34",
    #      "23",
    #  ]
    transition = np.array(
        [
            [1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 1],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
        ]
    )
    long_trans = mod_pow(transition, N-1 )
    result = long_trans.dot (np.array ([1,0,1,0,0,0]))
    print (result[2] % (10 ** 8)) # '14' pozycja planszy długiej na N kwadraty
