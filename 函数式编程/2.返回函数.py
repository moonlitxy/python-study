def calcam_func(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 延迟求和计算函数
def lay_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lay_sum(1, 3, 5, 7, 9)
print("f:",f())


# 闭包使用的时候，不能够在循环当中使用闭包，不然会得到相同的值
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())



def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1(),f2(),f3())



# 每次调用递增
def createCounter():
        num = 0
        def counter():
            nonlocal num
            num = num +1
            return num
        return counter   
 
ans = createCounter()
print("ans counter:",ans())
print("ans counter2:",ans())