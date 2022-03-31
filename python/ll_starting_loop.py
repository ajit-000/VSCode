class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def start_pos(self):
        slow, fast = self.head, self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow.next == fast.next:
                slow = self.head
                break
        else:
            print("No Loop")
            return
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print(slow.data)


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
    link.start_pos()
