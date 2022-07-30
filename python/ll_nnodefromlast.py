class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def nth_node(self, node):
        prev, curr = self.head, self.head
        for i in range(node):
            curr = curr.next
        while curr != None:
            prev = prev.next
            curr = curr.next
        print(prev.data)


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
    print()
    link.nth_node(int(input("Enter Position :")))
