class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def inb(self, nn):
        beg = Node(nn)
        beg.next = self.head
        self.head = beg

    def ine(self, nn):
        en = Node(nn)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = en

    def inm(self, nn, pd):
        if pd is None:
            print("No such Node Exist")
            return
        mid = Node(nn)
        mid.next = pd.next
        pd.next = mid


if __name__ == "__main__":
    link = LL()
    link.head = Node(input("Enter Node :"))
    sec = Node(input("Enter Node :"))
    th = Node(input("Enter Node :"))
    link.head.next = sec
    sec.next = th
    link.printList()
    nn = input("Enter Node to insert: ")
    link.inm(nn, link.head.next)
    link.printList()
