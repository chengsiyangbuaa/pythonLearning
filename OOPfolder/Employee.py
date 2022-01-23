from Person import Person, Gender
#父类parent class 超类super class 基类base class
#子类sub class 扩展类 derived class 继承类 inherited class
class Employee(Person):#继承 inheritence  
    def __init__(self,emplNo,idNo,name):
        super(Employee,self).__init__(idNo,name)  #把Person对象初始化了。super(Employee,self)指获得Employee类型的父类对象，并且这个对象是self的对象
        self.sEmployeeNo = emplNo
        self.sJobTitle = ''
        self.sDepartment = ''
        self.iWeekSalary = 0

    def work(self):
        print("I am a ",self.sJobTitle+", I am working with mt partners in department:",self.sDepartment )
    
    def speak(self):#重写overwrite
        print("Employee::speak()")
        super().speak()
        print("I am happy to work for you.")

    def description(self):
        assert self.gender in (Gender.male,Gender.female)
        s = "ID :%s\tEmployee No:%s\tName: %s \n" % (self.sId,self.sEmployeeNo, self.sName)
        t = "gender:%s\tJob Title: %s\tDepartment: %s\n" %(
            'Male' if self.gender==Gender.male else 'Female', self.sJobTitle, self.sDepartment
        )
        return s+t


if __name__ =='__main__':
    dora = Employee('10001','3298674444','Dora Chan')
    dora.gender = Gender.female
    dora.sDepartment = "Marketing"
    dora.sJobTitle = "Sales"
    dora.iWeekSalary = 2300

    dora.work()
    print()
    dora.speak()
    print()
    dora.eat(230)
    print()
    print(dora.description())