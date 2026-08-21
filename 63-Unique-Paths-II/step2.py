class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths = [[0 for _ in range(num_columns + 1)] for _ in range(num_rows + 1)]
        if obstacleGrid[0][0] == 1:
            return 0

        num_paths[0][0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == 1:
                    num_paths[row][column] = 0
                    continue

                num_paths[row][column + 1] += num_paths[row][column]
                num_paths[row + 1][column] += num_paths[row][column]

        return num_paths[num_rows - 1][num_columns - 1]
