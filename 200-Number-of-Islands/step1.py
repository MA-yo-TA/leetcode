from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def find_whole_island(row: int, column: int):
            nodes_to_see: deque[tuple[int, int]] = deque([(row, column)])
            while nodes_to_see:
                node = nodes_to_see.popleft()
                seen_nodes.add((row, column))
                for r, c in [
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                    (node[0] - 1, node[1]),
                    (node[0] + 1, node[1]),
                ]:
                    if 0 <= r < num_rows and 0 <= c < num_columns:
                        if (r, c) not in seen_nodes and grid[r][c] == "1":
                            nodes_to_see.append((r, c))
                        seen_nodes.add((r, c))

        num_rows = len(grid)
        num_columns = len(grid[0])
        seen_nodes: set[tuple[int, int]] = set()
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == "0":
                    seen_nodes.add((r, c))
                    continue
                if (r, c) in seen_nodes:
                    continue

                find_whole_island(r, c)
                num_islands += 1

        return num_islands
