
# def my_abs(x):
#     if x >= 0:
#         return x
#     else :
#         return -x

# check func arg type   isinstance  判断是不是想要的类型
def my_abs(x):
    if  not isinstance(x,(int,float)):
        raise TypeError("bad type")
    if x >= 0:
        return x
    else :
        return -x



print("abs:", my_abs(-12.345))




# 定义参数，如果每次都传入默认参数

def add_end (L = None):
    if L is None:
        L = []
    L.append('end')
    return L

print("add end:",add_end())
print("add end2:",add_end())



# 传入可变参数

def person(name , age , **kw):
    if 'city' in kw:
        print("kw contain city")
    if 'job' in kw:
        print("kw contain job")
        pass

print("person:" , person("city",12, city = 'city'))     