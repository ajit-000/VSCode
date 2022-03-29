s = "12:00:00PM"
if s[-2:] == "AM" and s[:2] == "12":
    print("00" + s[2:-2])
elif s[-2:] == "AM":
    print(s[:-2])
elif s[-2:] == "PM" and s[:2] == "12":
    print(s[:-2])
else:
    ans = int(s[:2]) + 12
    print(str(str(ans) + s[2:8]))
