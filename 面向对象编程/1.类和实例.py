
# 面向对象编程 - object Oriented Programming(OOP),OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bartAnswer = bart.print_score()
lisaAnswer = lisa.print_score()



lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())