class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def rev_ll(self):
        headnode = self.head
        curr = self.head
        prev, nex = None, None
        while(curr != None):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        headnode = prev
        return headnode

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


def recursive_reverse(prev, curr):
    h = curr
    if curr != None:
        recursive_reverse(curr, curr.next)
        curr.next = prev
    else:
        h = prev


if __name__ == "__main__":
    link = LL()
    link.head = Node(input())
    headnode = link.head
    sec = Node(input())
    th = Node(input())
    link.head.next = sec
    sec.next = th
    link.printList()
    print()

    # link.head = link.rev_ll() # When we solving without Recursion
    # link.printList()

    # Recursive Method:-
    recursive_reverse(None, headnode)
    link.printList()
