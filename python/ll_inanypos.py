class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


def insertPos(headNode, position, data):
    head = headNode

    if (position < 1):
        print("Invalid position!")

    if position == 1:
        newNode = Node(data)
        newNode.nextNode = headNode
        head = newNode

    else:
        while (position != 0):
            position -= 1

            if (position == 1):
                newNode = Node(data)
                newNode.nextNode = headNode.nextNode
                headNode.nextNode = newNode
                break

            headNode = headNode.nextNode
            if headNode == None:
                break
        if position != 1:
            print("position out of range")
    return head


def printList(head):
    while (head != None):
        print(' ' + str(head.data), end='')
        head = head.nextNode
    print()


if __name__ == '__main__':

    # Creating the list 3.5.8.10
    head = Node(3)
    head.nextNode = Node(5)
    head.nextNode.nextNode = Node(8)
    head.nextNode.nextNode.nextNode = Node(10)
    print("Linked list before insertion: ", end='')
    printList(head)
    data = 12
    position = 3
    head = insertPos(head, position, data)
    print("Linked list after insertion of 12 at position 3: ", end='')
    printList(head)

    # front of the linked list
    data = 1
    position = 1
    head = insertPos(head, position, data)
    print("Linked list after insertion of 1 at position 1: ", end='')
    printList(head)

    # insertion at end of the linked list
    data = 15
    position = 7
    head = insertPos(head, position, data)
    print("Linked list after insertion of 15 at position 7: ", end='')
    printList(head)
