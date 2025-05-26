
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
# print("name:",bart.__name)

# 练习
class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
    
    def getGender(self):
        return self._name
    
    def setGender(self,gender):
        if gender!='male' and gender!='female':
            raise ValueError("wrong gender")
        else :
            self._gender = gender

stu = Student('张三',"male")
print("student:",stu.getGender())        
stu.setGender('female')
print("stu2:",stu.getGender()) 