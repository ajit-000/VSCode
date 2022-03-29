# SHORT METHOD VIA SLICING

# s = input("Enter any string : ")
# if s == s[::-1]:
#     print(s, "is pallindrome")
# else:
#     print(s, "is not pallindrome")

# LONG METHOD BY COMPARING FIRST AND LAST DIGIT AND SO ON...

s = input("Enter any string : ")
low = 0
high = len(s)-1
while low < high:
    if s[low] != s[high]:
        print(s, "is not pallindrome")
    low += 1
    high -= 1
else:
    print(s, "is pallindrome")
