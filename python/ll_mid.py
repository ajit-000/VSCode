class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def midll(self):
        temp = self.head
        cnt = 0
        while temp != None:
            cnt += 1
            temp = temp.next
        # print("\n",cnt)
        temp = self.head
        for i in range(cnt//2):
            temp = temp.next
        print("\n")
        print(temp.data)

    def midll_optimised(self):
        fast = self.head
        slow = self.head

        if self.head is None:
            print("invalid node")
            return

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print()
        print(slow.data)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    link = LL()
    link.head = Node(input())
    sec = Node(input())
    th = Node(input())
    fr = Node(input())
    fv = Node(input())
    link.head.next = sec
    sec.next = th
    th.next = fr
    fr.next = fv
    link.printList()
    link.midll_optimised()
