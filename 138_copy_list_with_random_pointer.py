from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        if head is None:
            return None

        c = head
        new_head = None
        n_c = None

        while c is not None:
            new = Node(c.val)
            new.random = c.random
            if n_c:
                n_c.next = new
                n_c = new
            else:
                n_c = new
            if new_head is None:
                new_head = new
            lookup[c] = new
            c = c.next

        n_c = new_head

        while n_c is not None:
            if n_c.random is not None:
                val = lookup[n_c.random]
                n_c.random = val
            n_c = n_c.next

        return new_head

def give_head(nums: List[int]):
    head = None
    last = None
    for n in nums:
        new = Node(n)
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
    x = Solution().copyRandomList(give_head([2, 4, 3]), give_head([5, 6, 4]))
    while x:
        print(x.val)
        x = x.next
