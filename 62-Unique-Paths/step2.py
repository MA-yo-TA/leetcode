from collections import deque


class Solution:
    def uniquePaths(self, num_rows: int, num_columns: int) -> int:
        num_paths = [[0] * num_columns for _ in range(num_rows)]
        frontier = deque([(0, 0)])
        seen = set([(0, 0)])
        num_paths[0][0] = 1
        while frontier:
            row, column = frontier.popleft()
            if row + 1 < num_rows:
                num_paths[row + 1][column] += num_paths[row][column]
                if (row + 1, column) not in seen:
                    frontier.append((row + 1, column))
                    seen.add((row + 1, column))
            if column + 1 < num_columns:
                num_paths[row][column + 1] += num_paths[row][column]
                if (row, column + 1) not in seen:
                    frontier.append((row, column + 1))
                    seen.add((row, column + 1))

        return num_paths[num_rows - 1][num_columns - 1]
