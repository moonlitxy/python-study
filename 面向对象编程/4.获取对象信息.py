import types


print("type:",type(1234))

if  type("abs")==str:
    print("is str")
else:
    print('is not str')

# 获得一个对象的所有属性和方法

print(dir('abc'))
# is str
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
# 'translate', 'upper', 'zfill']

# 自己写一个len() 方法
class MyDog():
    def __len__(self):  # 两个下划线
        return 100
    

dog = MyDog()
print("dog len:",len(dog))


# 定义__slots__
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'alice'
# s.score = 95   # 不能够被使用
print(s.name)
print(s.score)