from timeit import timeit

code1 = '''
try:
    age = 0
    fact = 10/age
except (NameError,ValueError,ZeroDivisionError):
    pass
    # print("An Error...")
else:
    pass
    # print("No Error Encountered")
'''

code2 = '''
def calculate_age(x):
    if x<=0:
        # print("Value Entered is not valid")
        return None
    return x/10

calculate_age(-5)
'''

print("First Code= ", timeit(code1, number=10000))
print("Second Code= ", timeit(code2, number=10000))
