string = input("Enter the string: ")
sub_string = input("Enter the sub string: ")
x = len(sub_string)
ss = 0
if sub_string in string:
    for i in range(0, len(string)-1):
        if string[i:i+x] == sub_string:
            ss += 1
            i += 1
        else:
            i += 1
    print(f"{ss} {sub_string} present in {string}")

else:
    print(f"{sub_string} not present in {string}")
