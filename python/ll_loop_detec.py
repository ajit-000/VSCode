class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def loop_dec_optimised(self):
        slow, fast = self.head, self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("True")
                return
        else:
            print("False")
            return


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
    fv.next = sec
    # Printing Linked List will give an Infinite Loop
    link.loop_dec_optimised()
