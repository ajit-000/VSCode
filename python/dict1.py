# dict1 = dict({(1, 'a'), (2, 'b')})
# print(dict1)


# dict2 = dict(first="abc", second="bdk")
# print(dict2["first"])
# print(dict2.get('first'))


# "GET" function will only get the value but it doesn't
#  update the dictionary

# dict3 = {1: 'abc', 2: 'def'}
# print(dict3.get(3, 4))
# print(dict3)


# Nested Dictionary, pop method & pop_item :

# dict4 = {1: {1: 'abc', 2: 'def'}, 2: [3, 'lnnn', 4, 'oooooh']}
# dict4[1].pop(1)
# dict4.pop(1)
# dict4.popitem()
# print(dict4)
# dict4.clear()
# del(dict4)
# print(dict4)

# dict5 = {1: 'xnp', 2: 'ham'}
# for i in dict5.keys():
#     print(i)
# for i in dict5.values():
#     print(i)
# for i, j in dict5.items():
# print(i, j, sep=":")

# dict6 = {1: {1: 'abc', 2: 'def'}, 2: [3, 'lnnn', 4, 'oooooh']}
# a = dict6.copy()
# print(id(a))
# print(id(dict6))
# a[1] = 2
# print(a)

# dict7 = {1: {1: 'abc', 2: 'def'}, 2: [3, 'lnnn', 4, 'oooooh']}
# y = "Hello"
# z = dict.fromkeys(dict7, y)
# print(z)

# dict8 = {1: {1: 'abc', 2: 'def'}, 2: [3, 'lnnn', 4, 'oooooh']}
# dict8.update({3: 'sef', 4: 'bsdfk'})
# print(dict8)
