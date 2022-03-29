# LIST COMPREHENSIONS EXAMPLES

# l1 = ["ajit", "ajuu", "subh", "remo", "aj"]
# l2 = [i.upper() for i in l1 if i.startswith("a")]
# print(l2)

# l3 = [i*2 for i in range(10)]
# print(l3)

# SET COMPRIHENSIONS

# s1 = "shimmishimmiaah shimmi aah shimmi aah driving swalahlalah.. "
# s2 = {i for i in s1 if i in "aeiou"}
# print(s2)

# DICTIONARY COMPRIHENSIONS

# d = {x: x**2 for x in range(10)}
# print(d)

# l1 = [10, 20, 30, 40, 50, 60]
# l2 = ["oo yeh!!", "come on..", "go hard",
#       "deep..", "harder...", "ahhh...ah.."]
# d2 = {l1[i]: l2[i] for i in range(len(l1))}
# print(d2)

# FROM 2 LIST THEIR ARE BETTER WAYS TO CREATE DICTIONARY
# BY USING "zip" function which take mapping of 2 lists and take it as tuple
# and then by using "dict" keyword we will create an dictionary

# l1 = [10, 20, 30, 40, 50, 60]
# l2 = ["oo yeh!!", "come on..", "go hard",
#       "deep..", "harder ...", "ahhh...ah.."]
# d3 = dict(zip(l1, l2))
# print(d3)

# REVERSING AN DICTIONARY USING COMPREHENSIONS
# OR SWAPPING KEY AND VALUES
# TAKING KEY AS VALUES AND VALUES AS KEY

# d4 = {101: "maggie", 102: "biriyani", 103: "egg role", 104: "momos"}
# d5 = {v: k for (k, v) in d4.items()}
# print(d5)
