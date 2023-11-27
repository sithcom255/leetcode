from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        bigger = len(nums1)
        smaller = len(nums2)

        if bigger < smaller:
            bigger, smaller = smaller, bigger
            nums1, nums2 = nums2, nums1

        if not nums2:
            mid = bigger // 2
            if bigger % 2 == 1:
                return nums1[mid]
            return (nums1[mid - 1] + nums1[mid]) / 2

        l = 0
        r = smaller + bigger + 1
        needed = (l + r) // 2

        condition = True
        while l <= r:
            lefts = [-100_000_000, -100_000_000]
            rights = [100_000_000, 100_000_000]

            mid = (l + r) // 2
            b_mid = mid
            s_mid = needed - mid
            if s_mid > len(nums2):
                le = len(nums2) - s_mid
                s_mid += le
                b_mid -= le

            if 0 < b_mid <= len(nums1):
                lefts[0] = nums1[b_mid - 1]
            if 0 <= b_mid < len(nums1):
                rights[0] = nums1[b_mid]
            if s_mid >= 0:
                if 0 < s_mid <= len(nums2):
                    lefts[1] = nums2[s_mid - 1]
                if 0 <= s_mid < len(nums2):
                    rights[1] = nums2[s_mid]
            else:
                rights[1] = nums2[0]

            if max(lefts) <= min(rights):
                if (bigger + smaller) % 2 == 0:
                    return (max(lefts) + min(rights)) / 2
                else:
                    return min(max(lefts), min(rights))
            else:
                if rights[0] < rights[1]:
                    l = mid + 1
                elif rights[0] > rights[1]:
                    r = mid - 1
                else:
                    return rights[0]


if __name__ == '__main__':
    # print(Solution().findMedianSortedArrays(nums1=[], nums2=[3]))
    # print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
    # print(Solution().findMedianSortedArrays([1, 3], nums2=[2]))
    print(Solution().findMedianSortedArrays([1], nums2=[2, 3]))
    # print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5], nums2=[1, 2, 5]))
    # print(Solution().findMedianSortedArrays([1, 3], nums2=[2, 7]))
