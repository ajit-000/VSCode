class abc:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    #     print(a, b)

    def music(self):
        print("Music Class")


class cdf(abc):
    def music(self):
        print("Muziik")


if __name__ == "__main__":
    # p = abc(2, 3)
    # x = cdf(5, 6)
    # x.music()
    # x = cdf()
    # x.music()
    x = abc()
    x.music()
