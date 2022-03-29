s = input()
for i in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(i(j) for j in s))
