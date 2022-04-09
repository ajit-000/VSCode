class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, x):
        head=self.head
        sml = ListNode()
        lar = ListNode()
        l1 = sml
        l2 = lar
        temp = head
        while temp != None:
            curr = temp.next
            if temp.val < x:
                l1.next = temp
                temp.next = None
                l1 = temp
            else:
                l2.next = temp
                temp.next = None
                l2 = lar
            temp = curr
        l1.next = lar.next
        return sml.next


# if __name__ == "__main__":
#     link=Solution()
#     link.a = ListNode(1)
#     b = ListNode(4)
#     a.next = b
#     c = ListNode(3, b)
#     d = ListNode(2, c)
#     e = ListNode(5, d)
#     f = ListNode(2, e)
#     f.next = None
