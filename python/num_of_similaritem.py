from pprint import pprint

sentence = [1, 2, 3, 2, 3, 1, 4, 6, 4, 5, 6]
char_len = {}
for char in sentence:
    if char in char_len:
        char_len[char] += 1
    else:
        char_len[char] = 1
for x, y in char_len.items():
    if y == 1:
        print(x, "occured only once in the list")
# pprint(char_len, width=1)
