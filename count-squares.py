"""
You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

    Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
    Query - Given a single query point, count the number of ways to choose three additional points from the data structure such that the three points and the query point form a square. The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.

Implement the CountSquares class:

    CountSquares() Initializes the object.
    void add(int[] point) Adds a new point point = [x, y].
    int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.

"""

from typing import Dict, Set, Tuple, List


class CountSquares:

    def __init__(self):
        self.points: Dict[Tuple[int, int], int] = {}
        self.x_mapping: Dict[int, Set[int]] = {}
        self.y_mapping: Dict[int, Set[int]] = {}

    def add(self, point: List[int]) -> None:
        assert len(point) == 2, "Point must have exactly 2 coordinates"
        x, y = point

        self.points[(x, y)] = self.points.get((x, y), 0) + 1

        self.x_mapping.setdefault(x, set()).add(y)
        self.y_mapping.setdefault(y, set()).add(x)

    def count(self, point: List[int]) -> int:
        assert len(point) == 2, "Point must have exactly 2 coordinates"
        x, y = point

        square_count = 0

        for x2 in self.y_mapping.get(y, set()):
            if x == x2:
                continue

            square_count += self.get_square_count(x, x2, y)

        return square_count

    def get_square_count(self, x1: int, x2: int, y: int) -> int:
        distance = abs(x2 - x1)
        square_count = 0

        # Square above the query point
        square_count += (
            self.points.get((x2, y), 0)
            * self.points.get((x1, y + distance), 0)
            * self.points.get((x2, y + distance), 0)
        )

        # Square below the query point
        square_count += (
            self.points.get((x2, y), 0)
            * self.points.get((x1, y - distance), 0)
            * self.points.get((x2, y - distance), 0)
        )

        return square_count
