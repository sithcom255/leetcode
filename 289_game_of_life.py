from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                c = 0
                res = 0
                for y_ in range(max(0, y-1), min(y, y+2), 1):
                    for x_ in range(max(0, x-1), min(x, x+2), 1):
                        if y == y_ and x == x_:
                            continue
                        if 0 <= y_ < len(board) and 0 <= x_ < len(board[0]):
                            val = board[y_][x_]
                            if val == 1 or val == -2:
                                c += 1

                if board[y][x] == 0:
                    if c == 3:
                        res = -1
                    else:
                        res = 0
                else:
                    if c < 2:
                        res = -2
                    elif c == 2 or c == 3:
                        res = 1
                    elif c > 3:
                        res = -2
                board[y][x] = res

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == -2:
                    board[y][x] = 0
                if board[y][x] == -1:
                    board[y][x] = 1



if __name__ == '__main__':
    p = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(p)
    assert [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]] == p
