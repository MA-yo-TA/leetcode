class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        OBSTACLE = 1
        if obstacle_grid[-1][-1] == OBSTACLE:
            return 0

        num_rows = len(obstacle_grid)
        num_columns = len(obstacle_grid[0])
        num_paths = [0] * (num_columns + 1)
        num_paths[0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacle_grid[row][column] == OBSTACLE:
                    num_paths[column] = 0
                    continue

                num_paths[column + 1] += num_paths[column]

        return num_paths[num_columns - 1]
