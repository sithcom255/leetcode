from typing import Optional, List


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        counter = 0
        node = head
        while node:
            counter += 1
            node = node.next

        if counter == 1:
            return head

        k = k % counter
        if k == 0:
            return head

        counter = 0
        candidate = None
        node = head
        last = head
        while node:
            if candidate:
                candidate = candidate.next
            if counter == k:
                candidate = head
            counter += 1
            last = node
            node = node.next

        new_head = candidate.next
        last.next = head
        candidate.next = None

        return new_head


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
    x = Solution().rotateRight(give_head([1, 2, 3, 4, 5, 6]), 4)
    while x:
        print(f"{x.val}")
        x = x.next
