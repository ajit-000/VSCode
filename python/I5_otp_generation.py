def otp_generator(num, n):
    x = ""
    num = str(num)
    for i in range(0, len(num), 2):
        p = int(num[i])**2
        x = x+str(p)
    return x[:n]


print(otp_generator(91741749, 4))
