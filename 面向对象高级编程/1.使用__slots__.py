
# 定义__slots__
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'alice'
# s.score = 95   # 不能够被使用
print(s.name)
print(s.score)