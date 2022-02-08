from re import A


class MagicMethod:
    def __init__(self,name="N/A"):
        self.sName = name
        print("::__init__")

    def __del__(self):
        print("::__del__")

a = MagicMethod()
b = a
a = 1
print("-----------")
b = 1
print("-----------")
