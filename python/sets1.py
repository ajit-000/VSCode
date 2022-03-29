# Sets in Python
# Set is a collection in python which is unordered,mutable
# uses Hash Data Structure(uses hashing internally).

# s1 = [2, 3, 5, 12, 2, 7, 5, 8]
# s1 = {1, 2, 3, 3, 4, 5, 4, 1, 2}
# s2 = set(s1)
# print(len(s1))
# print(len(s2))
# print(s1)


# set1 = {1, 'abc', 23, 'bcd', 69, 'k', 0}
# print(set1)
# for i in set1:
#     print(i)


# set1 = {1, 'abc', 23, 'bcd', 69, 'k', 0}
# set1.add('jd')
# set1.update([1, 2, 3])
# print('aj' in set1)
# print(set1)
# set1.clear()
# print(set1)
# del(set1)


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)
# print(set1 | set2)
# set1.intersection_update(set2)
# print(set1)
# print(set2)


# Frozen set is used to convert mutable set in to im-mutable

from typing import FrozenSet


# A = FrozenSet([1, 2, 3, 4])
# print(A)
# we can't add elements in frozen set because this become immutable
# A.add(5)
