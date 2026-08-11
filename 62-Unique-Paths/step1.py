from collections import deque


class Solution:
    def uniquePaths(self, num_rows: int, num_columns: int) -> int:
        grid = [[0] * num_columns for _ in range(num_rows)]
        frontier = deque([(0, 0)])
        seen = set([(0, 0)])
        grid[0][0] = 1
        while frontier:
            index_row, index_column = frontier.popleft()
            num_ways = grid[index_row][index_column]
            if index_row + 1 < num_rows:
                grid[index_row + 1][index_column] += num_ways
                if (index_row + 1, index_column) not in seen:
                    frontier.append((index_row + 1, index_column))
                    seen.add((index_row + 1, index_column))
            if index_column + 1 < num_columns:
                grid[index_row][index_column + 1] += num_ways
                if (index_row, index_column + 1) not in seen:
                    frontier.append((index_row, index_column + 1))
                    seen.add((index_row, index_column + 1))

        return grid[num_rows - 1][num_columns - 1]
