from collections import deque
from enum import IntEnum
from itertools import product


class NodeType(IntEnum):
    WATER = 0
    LAND = 1


class Solution:
    def maxAreaOfIsland(self, grid: list[list[NodeType]]) -> int:
        num_rows = len(grid)
        num_columns = len(grid[0])
        seen_nodes: set[tuple[int, int]] = set()

        def get_area_of_island(row: int, column: int) -> int:
            nodes_to_see = deque([(row, column)])
            seen_nodes.add((row, column))
            area = 1
            while nodes_to_see:
                node = nodes_to_see.popleft()
                for r, c in (
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                    (node[0] - 1, node[1]),
                    (node[0] + 1, node[1]),
                ):
                    if not (0 <= r < num_rows and 0 <= c < num_columns):
                        continue
                    if (r, c) in seen_nodes:
                        continue

                    if grid[r][c] == NodeType.LAND:
                        area += 1
                        nodes_to_see.append((r, c))
                    seen_nodes.add((r, c))

            return area

        max_area_of_island = 0
        for row, column in product(range(num_rows), range(num_columns)):
            if (row, column) in seen_nodes:
                continue
            if grid[row][column] == NodeType.WATER:
                seen_nodes.add((row, column))
                continue

            area = get_area_of_island(row, column)
            max_area_of_island = max(area, max_area_of_island)

        return max_area_of_island
