def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(source, "--->", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(source, "--->", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)


if __name__ == "__main__":
    n = 4
    TowerOfHanoi(n, 'A', 'B', 'C')
