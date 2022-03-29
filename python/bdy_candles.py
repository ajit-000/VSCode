candles = [3, 2, 1, 3]
num = 0
x = max(candles)
for i in candles:
    if i == x:
        num += 1
print(num)
