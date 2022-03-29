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

    def insertPos(headNode, position, data):
        head = headNode

    # This condition to check whether the
    # position given is valid or not.
        if (position < 1):
            print("Invalid position!")

        if position == 1:
            newNode = Node(data)
            newNode.nextNode = headNode
            head = newNode

        else:
            # Keep looping until the position is zero
            while (position != 0):
                position -= 1

                if (position == 1):

                    # adding Node at required position
                    newNode = Node(data)

                # Making the new Node to point to
                # the old Node at the same position
                    newNode.nextNode = headNode.nextNode

                # Replacing headNode with new Node
                # to the old Node to point to the new Node
                    headNode.nextNode = newNode
                    break

                headNode = headNode.nextNode
                if headNode == None:
                    break
            if position != 1:
                print("position out of range")
        return head


if __name__ == "__main__":
    link = LL()
    link.head = Node(input("Enter Node :"))
    sec = Node(input("Enter Node :"))
    th = Node(input("Enter Node :"))
    link.head.next = sec
    sec.next = th
    link.printList()
    nn = input("Enter Node to insert: ")
    # link.insertPos(, 2, 5)
    link.printList()
