from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)
        for y in range(len(matrix) // 2):

            for x in range(start, end - 1):
                lst = matrix[y][x]
                save = matrix[x][-y - 1]
                matrix[x][-y - 1] = lst
                lst = save

                save = matrix[-y - 1][-x - 1]
                matrix[-y - 1][-x - 1] = lst
                lst = save

                save = matrix[-x - 1][y]
                matrix[-x - 1][y] = lst
                lst = save

                save = matrix[y][x]
                matrix[y][x] = lst
                lst = save

            #    left

            start += 1
            end -= 1



if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate = Solution().rotate(l)
    assert [[7, 4, 1], [8, 5, 2], [9, 6, 3]] == l
