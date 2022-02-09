from enum import Enum

class Gender(Enum):#枚举类型，（继承）
    male = 0 #效率+可读性
    female = 1

#定义一个类
class Person:
    "Person class"
    def __init__(self,idNo="N/A",name="N/A"):#构造函数，constructor  在实例化一个对象的同时初始化它
        self.sName = name
        self.sId = idNo
        self.iWeight = 0
        self.gender = Gender.male # 定义了4个属性

    def speak(self):
        print("Person::speak()")
        print("I am %s . Nice to meet you"%self.sName)

    def eat(self,weight):
        self.iWeight += weight
        print("I just ate %.2f gram's food"%weight)

    def description(self):
        assert self.gender in (Gender.male,Gender.female)
        s = "Id:%s\tName:%s\n"%(self.sId,self.sName)
        t = "Gender:%s\tBody weight:%d" % ("Male" if self.gender==Gender.male else "Female",self.iWeight)
        return s+t
        
if __name__ =='__main__':
    lu17 = Person(name="617")#调用__init()__函数创建一个实例instance，也叫对象object
    print(type(lu17))
    print(lu17.sName)#实例里有它的属性和方法，对实例的属性的访问
    print(lu17.sId)
    print(lu17.iWeight)
    print(lu17.gender)
    lu17.speak()#调用实例的方法
    lu17.eat(120.0)
    print(lu17.description())


