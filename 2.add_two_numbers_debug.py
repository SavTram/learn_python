class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l = ListNode()
        cur = l
        c=0
        while l1 or l2 or c:
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            p = (p1 + p2) % 10 + c
            c = (p1+p2) //10
            cur.next = ListNode(p)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l.next

# l1 = [2,4,3], l2 = [5,6,4]
a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
l1 = a
a.next = b
b.next = c
e = ListNode(5)
d = ListNode(6)
f = ListNode(4)
l2 = e
e.next = d
d.next = f


sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next

