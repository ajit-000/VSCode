def findMinLength(s, n):

    st = []
    for i in range(n):

        if (len(st) == 0):
            st.append(s[i])

        elif (s[i] == '1'):
            st.pop()

        else:
            st.append(s[i])

    ans = 0
    finalStr = []
    while (len(st) > 0):
        ans += 1
        finalStr.append(st[-1])
        st.pop()

    print("The final string size is: ", ans)
    
    if (ans == 0):
        print("The final string is: EMPTY")

    else:
        print("The final string is: ", *finalStr)


if __name__ == "__main__":
    n = int(input("Enter the length of string: "))
    s = input("Enter the string: ")
    findMinLength(s, n)
