from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(0)
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        rest = []
        extra = None
        while l1 is not None or l2 is not None or extra:
            if l1:
                l = l1.val
            else:
                l = 0
            if l2:
                p = l2.val
            else:
                p = 0
            res = l + p
            if extra:
                res = res + extra
                extra = None
            if res > 9:
                extra = 1
                res = res % 10
            rest.append(res)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return self.give_head(rest)

    def give_head(self, nums: List[int]):
        head = None
        last = None
        for n in nums:
            new = ListNode(n)
            if head is None:
                head = new

            if last is None:
                last = new
            else:
                last.next = new
                last = new
        return head


def give_head(nums: List[int]):
    head = None
    last = None
    for n in nums:
        new = ListNode(n)
        if head is None:
            head = new

        if last is None:
            last = new
        else:
            last.next = new
            last = new
    return head


if __name__ == '__main__':
    # print(Solution().addTwoNumbers(give_head([1, 2, 4]), give_head([1, 2, 3])).val)
    x = Solution().addTwoNumbers(give_head([2, 4, 3]), give_head([5, 6, 4]))
    while x:
        print(x.val)
        x = x.next
