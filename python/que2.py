def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si


x = int(input("Enter the principal Amount : "))
y = int(input("Enter the time period : "))
z = int(input("Enter the rate of interest : "))
simple_interest(x, y, z)
