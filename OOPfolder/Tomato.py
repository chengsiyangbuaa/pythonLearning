#类对象的属性和方法
class Tomato:
    objectCount = 0
    def smile():
        print("This smile() function without self parameter")

    def __init__(self):
        Tomato.objectCount += 1

    
if __name__ == "__main__":
    t1 = Tomato()
    t2 = Tomato()
    print("Tomato.objectCount = ",Tomato.objectCount)
    Tomato.smile()
    print("t1.objectCount",t1.objectCount)
    # t1.smile()
    d = dict.fromkeys(["id","name","age"],"unknown") #这个就是类对象的方法