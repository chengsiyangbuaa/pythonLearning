from Person import Gender
from Person import Person

xiaoqiezi = Person(name="xiao qie zi",idNo="4396")#self 不用去写，解释器帮我们自动写上去了
lu17 = Person(name="617",idNo="2200")
lu17.gender = Gender.female
xiaoqiezi.eat(2200.4396)
Person.eat(xiaoqiezi,2200.4396)
print(lu17.description())