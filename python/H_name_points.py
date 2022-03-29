def name_point(s1, s2):
    point = 0
    for i in range(0,len(max(s1, s2))):
        if s1[i] == s2[i]:
            point += 2
        elif s1[i] in s2:
            point += 1
        elif s1[i]=="\0" or s2[i]=="\0":
            return point
        else:
            continue
    return point


if __name__ == "__main__":
    s1 = input("Enter the string : ")
    s2 = input("Enter the string : ")
    print(f"Total Points are : {name_point(s1,s2)}")
