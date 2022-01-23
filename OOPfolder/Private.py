class Private:
    def __init__(self):
        self.__privateAttribute = 1 #__ 私有属性

    def __privateMethod(self):
        print("This method should not be called outside!")

    def publicMethod(self):
        self.__privateMethod()
        print("__privateAttribute :",self.__privateAttribute)

if __name__ == "__main__":
    p = Private()
    # i = p.__privateAttribute
    # p.__privateMethod()
    p.publicMethod()