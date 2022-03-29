import math


def counter_g(n):
    count = 0
    if n == 1:
        return "Louis"
    while n != 1:
        count += 1
        if math.log2(n) == int(math.log2(n)):
            n = n//2
        else:
            n -= 2**int(math.log2(n))
    print(count)
    if count % 2 == 0:
        return "Louis"
    else:
        return "Richard"


if __name__ == "__main__":
    n = int(input("Enter the number : "))
    print(counter_g(n))
