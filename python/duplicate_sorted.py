def dup(nums):
    return list(set(nums))


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(dup(nums))
