from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0

        l = 0
        r = len(height) - 1
        m = min(height[l], height[r]) * r

        while l < r:
            candidate = min(height[l], height[r]) * (r -l)
            if m < candidate:
                m = candidate
            else:
                if height[l] <= height[r]:
                    l += 1
                else:
                    r -= 1
        return m


if __name__ == '__main__':
    print(49 == Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
