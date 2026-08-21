class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        OBSTACLE = 1
        if obstacle_grid[-1][-1] == OBSTACLE:
            return 0

        num_rows = len(obstacle_grid)
        num_columns = len(obstacle_grid[0])
        num_paths = [[0 for _ in range(num_columns + 1)] for _ in range(num_rows + 1)]
        num_paths[0][0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacle_grid[row][column] == OBSTACLE:
                    num_paths[row][column] = 0
                    continue

                num_paths[row][column + 1] += num_paths[row][column]
                num_paths[row + 1][column] += num_paths[row][column]

        return num_paths[num_rows - 1][num_columns - 1]
