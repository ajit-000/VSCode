text = input("Enter the text : ")
pat = input("Enter the pattern you want to search : ")
pos = text.find(pat)
while pos >= 0:
    print(pos)
    pos = text.find(pat, pos+1)
