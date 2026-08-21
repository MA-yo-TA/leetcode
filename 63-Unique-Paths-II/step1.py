class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
        if obstacleGrid[0][0] == 1:
            return 0

        num_paths[0][0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == 1:
                    num_paths[row][column] = 0
                    continue

                if column + 1 < num_columns:
                    num_paths[row][column + 1] += num_paths[row][column]
                if row + 1 < num_rows:
                    num_paths[row + 1][column] += num_paths[row][column]

        return num_paths[-1][-1]
