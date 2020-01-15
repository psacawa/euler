#!/usr/bin/env python3.7

import pdb

from dataclasses import dataclass, field
import logging
from typing import List
import sys
import heapq as hq
import numpy as np
from itertools import product

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@dataclass(init=False)
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
            self.dir = kwargs.pop("dir")
            self.checksum = (prev_checksum * 243 + BoardHistory._m[self.dir]) % (
                int(1e8) + 7
            )
        except KeyError as e:
            self.checksum = 0
            self.dir = "X"
        self.key = BoardHistory._to_int(self.position)

    def empty_pos(self):
        for i in range(4):
            for j in range(4):
                if self.position[i, j] == 0:
                    return i, j
        logging.error("No empty tile")
        raise Exception("No empty tile")

    @staticmethod
    def _to_int(pos) -> int:
        result = 0
        for i in pos.flatten():
            result = 3 * result + i
        return int(result)

    def __lt__(self, bd):
        return self.distance < bd.distance

    def __str__(self):
        return f"{self.position}\nCS: {self.checksum} dist: {self.distance} dir: {self.dir}"


start_board = np.array([0, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]).reshape(4, 4)
end_board = np.array([0, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1]).reshape(4, 4)
start = BoardHistory(distance=0, position=start_board)
end = BoardHistory(distance=0, position=end_board)
heap: List[BoardHistory] = [start]
shortest_dist = {start.key: 0}


def main():
    """Solve Euler 244"""
    result = 0
    num = 0
    while len(heap) != 0:
        #  pdb.set_trace ()
        num += 1
        logging.debug(num)
        current: BoardHistory = hq.heappop(heap)

        #  this is unnecessary because the graph searched here has all edge lenths = 1
        #  however in general this speeds up Dijkstra so I've included it
        if current.key == end.key:
            logging.debug(f"Path found:\n {current}")
            result += current.checksum

        distance = current.distance
        checksum = current.checksum
        #  logging.debug(f"Popped from stack:\n {current}")
        i, j = current.empty_pos()
        # generuje generator krotek w postaci ((x, y), 'd')
        dir_gen = zip(
            filter(
                lambda p: abs(i - p[0]) + abs(j - p[1]) == 1,
                product(range(i - 1, i + 2), range(j - 1, j + 2)),
            ),
            "drlu",
        )
        for p, dir in dir_gen:
            # check invalid grid position
            if not (0 <= p[0] < 4 and 0 <= p[1] < 4):
                continue

            next_pos = current.position.copy()
            next_pos[i, j], next_pos[p] = next_pos[p], next_pos[i, j]
            next = BoardHistory(
                distance=distance + 1, position=next_pos, prev_cs=checksum, dir=dir
            )
            key = next.key
            if key in shortest_dist and next.distance > shortest_dist[key]:
                continue
            #  logging.debug (f"Moving: pos={p} dir={dir}")
            #  logging.debug (next)
            # as before, this  check is now unnecessary
            else:
                shortest_dist[key] = next.distance
                hq.heappush(heap, next)

    print(result)


if __name__ == "__main__":
    main()
