#!/usr/bin/env python3.7

from dataclasses import dataclass, field
import logging
from typing import List
import sys
import heapq as hq
import numpy as np
from itertools import product

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class BoardHistory:
    """
    Turn array m into int
    0 = empty, 1 = red, 2 = blue
    Upper-left cell ([0,0]) is most sigmificant base-3 digit
    """

    distance: int = 0
    position: np.ndarray
    checksum: int
    _m = {"l": 76, "r": 82, "u": 85, "d": 68}

    def __init__(self, **kwargs):
        self.distance = kwargs.pop("distance", 0)
        self.position = kwargs.pop("position")
        try:
            prev_checksum = kwargs.pop("prev_cs")
            dir = kwargs.pop("dir")
            self.checksum = prev_checksum * 243 + BoardHistory._m[dir]
        except KeyError as e:
            self.checksum = 0

    def empty_pos(self):
        for i in range(4):
            for j in range(4):
                if self.position[i, j] == 0:
                    return i, j
        logging.error("No empty tile")
        raise Exception("No empty tile")

    @classmethod
    def from_arr(self) -> np.ndarray:
        n = self.position
        result: np.ndarray = np.zeros(16)
        for i in range(16):
            result[-i - 1] = n % 3
            n = n // 3
        return result.reshape((4, 4))

    def to_int(self) -> int:
        pos = self.position
        result = 0
        for i in pos.flatten():
            result = 3 * result + i
        return int(result)


start_board = np.array([0, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]).reshape(4, 4)
end_board = np.array([0, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1]).reshape(4, 4)
start = BoardHistory(distance=0, position=start_board)
heap: List[BoardHistory] = [start]
shortest_dist = {start.to_int(): 0}


def main():
    """Solve Euler 244"""
    while len(heap) != 0:
        current: BoardHistory = hq.heappop(heap)
        distance = current.distance
        checksum = current.checksum
        logging.debug(current)
        i, j = current.empty_pos()
        # generuje generator krotek w postaci ((x, y), 'd')
        dir_gen = zip (filter(
            lambda p: abs(i - p[0]) + abs(j - p[1]) == 1,
            product(range(i - 1, i + 2), range(j - 1, j + 2)),
        ), 'ulrd') 
        for p, dir in dir_gen:
            logging.debug (f"pos={p} dir={dir}")

            next_pos = current.position.copy()
            next_pos[i, j], next_pos[p] = next_pos[p], next_pos[i, j]
            next = BoardHistory(
                distance=distance + 1, position=next_pos, prev_cs=checksum, dir="u"
            )
            next_key = next.to_int()
            if next_key not in shortest_dist:
                shortest_dist [next_key] = next.distance
            else:
                if next.distance < shortest_dist[next_key]:
                    shortest_dist[next_key] = next.distance
if __name__ == "__main__":
    main()
