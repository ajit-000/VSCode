def longestValidParentheses(s):
    stack = [-1]
    m = 0
    for i in range(len(s)):
        # print(stack,i)
        if s[i] == ')':
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                m = max(m, i-stack[-1])
        else:
            stack.append(i)
    return m


if __name__ == "__main__":
    s = input()
    print(longestValidParentheses(s))
