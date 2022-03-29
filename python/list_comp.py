l1 = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
prices = [item[1] for item in l1]
print(prices)
filtered = [item for item in l1 if item[1] >= 10]
print(filtered)
