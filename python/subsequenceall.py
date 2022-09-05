def printSubsequence(input, output):
    if len(input) == 0:
        print(output)
        return
    printSubsequence(input[1:], output+input[0])
    printSubsequence(input[1:], output)


output = ""
input = input()
printSubsequence(input, output)
