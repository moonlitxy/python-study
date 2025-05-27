from enum  import Enum,unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name , member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


@unique   # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6    
    # Saa = 6

print('ans:',Weekday['Tue'])


class Gender(Enum):
    Male = 0
    Female = 1

class People(object):
    def __init__(self,name,gender):
        self.name = name 
        self.gender = gender

s = People("bard",Gender.Male)
if s.gender == Gender.Male:
    print('性别正确')
else:
    print('性别错误')        