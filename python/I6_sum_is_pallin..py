#  innum = 67
#  num1 = 66
#  num2 = 77
#  num1 + num2 = 143, which is not a palindrome.
#  Decrement innum by 1, innum = 66
#  num1 = 55
#  num2 = 77

#  innum = 4
#  num1 = 3(greatest palindrome smaller than 4)
#  num2 = 5(smallest palindrome greater than 4)
#  num1 + num2 = 8, which is a palindrome.
#  outnum = 8

def check_pal(N):
    N = str(N)
    if len(N) == 1 and N <= 9:
        return N
    else:
        for i in range(len(N)):
            if N[i] == N[i+1]:
                N = int(N)
                N -= 1
                return N
            else:
                return int(N)


def sm_lr(num):
    num = check_pal(num)

    if len(str(num)) == 1 and num < 9:
        print("The smaller pallindrome is: ", int(num)-1)
        print("The largest pallindrome is: ", int(num)+1)

    else:
        n = str(num)
        n = int(n[:1])
        x1, x2 = [n]*2, [n+1]*2
        x1 = map(str, x1)
        x2 = map(str, x2)
        x1 = "".join(x1)
        x2 = "".join(x2)
        print("The smallest Pallindrome is: ", x1)
        print("The largest Pallindrome is: ", x2)


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    sm_lr(num)
