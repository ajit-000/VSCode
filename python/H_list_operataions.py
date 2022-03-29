from os import remove


def list_operation(n):
    op = []
    s = ""
    print('''
1-) append(x) - Append string x to the end of s.
2-) delete(n) - Delete the last n characters of s.
3-) print(n) - Print the nth character of s.
4-) undo - Undo the last (not previously undone) operation of type  or,
           reverting  to the state it was in prior to that operation.

Enter the operations : ''')

    for i in range(0, n):
        x = input()
        op.append(x)
    print(op)

    for i in range(0, n):
        store = op[i].split()

        if store[0] == "1":
            s = s+store[1]

        elif store[0] == "2":
            pass


if __name__ == "__main__":
    x = int(input("Enter the number of operations you want : "))
    list_operation(x)
