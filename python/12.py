# table of the number using for loop

# n = int(input("Enter the number :"))
# for i in range(1,11):
#     print(n, "*", i, "=", n*i)


# table of the number till user want

n = int(input("Enter the number :"))
# Enter till you want multiples of n
print("Enter till you want multiples of", n, ":",end=' ')
m = int(input())
for i in range(1, m+1):
    print(n, "*", i, "=", n*i)
