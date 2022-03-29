# def change_pos(text):
#     text = list(text)
#     index = -1

#     # Loop from last index until half of the index
#     for i in range(len(text)-1, int(len(text)/2)-1, -1):

#         # match character is alphabet or not
#         if text[i].isalpha():
#             temp = text[i]
#             while True:
#                 index += 1
#                 if text[index].isalpha():
#                     text[i] = text[index]
#                     text[index] = temp
#                     break
#     return text


def change_pos(N):
    N = list(N)
    N1 = []
    for i in range(len(N)-1, -1, -1):
        if N[i].isalpha():
            N1.append(N[i])
    for i in range(len(N)):
        if not N[i].isalpha():
            N1.insert(i, N[i])
    return N1


if __name__ == "__main__":
    N = input("Enter the string : ")
    print("".join(change_pos(N)))
