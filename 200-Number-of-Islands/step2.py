from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def detect_whole_island(row: int, column: int):
            nodes_to_see: deque[tuple[int, int]] = deque([(row, column)])
            seen_nodes.add((row, column))
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

                    if grid[r][c] == "1":
                        nodes_to_see.append((r, c))
                    seen_nodes.add((r, c))

        num_rows = len(grid)
        num_columns = len(grid[0])
        seen_nodes: set[tuple[int, int]] = set()
        num_islands = 0
        for row in range(num_rows):
            for column in range(num_columns):
                if (row, column) in seen_nodes:
                    continue
                if grid[row][column] == "0":
                    seen_nodes.add((row, column))
                    continue

                detect_whole_island(row, column)
                num_islands += 1

        return num_islands
