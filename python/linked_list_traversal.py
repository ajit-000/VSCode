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
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    link = LL()
    link.head = Node(input())
    sec = Node(input())
    th = Node(input())
    link.head.next = sec
    sec.next = th
    link.printList()
