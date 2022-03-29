def ev_od(a, b):
    if a % 2 == b % 2:
        return (a+b+1)//2
    return (b-a+1)//2


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(ev_od(a, b))
