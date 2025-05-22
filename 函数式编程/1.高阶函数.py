# 变量可以指向函数
f = abs
print("value:",f(-3))  #  value: 3


# map()  and   reduce()
# map() func 将传入的参数依次作用到序列的每个元素，并把结果作为新的Interator返回

def f(x):
    return x * x

# filter函数的使用
def is_odd(n):
    return n % 2 == 1

ans = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
print("ans:",ans)


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
ans = list(filter(not_empty,['A', '', 'B', None, 'C', '  ']))
print("ans1:",ans)


# sorted 排序
list = [36, 5, -12, 9, -21]
print("排序后的list:",sorted(list))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print("绝对值排序后的list:",sorted(list,key=abs))

strList = ['bob', 'about', 'Zoo', 'Credit']
print( '排序字符串，ASCII编码顺序:',sorted(strList, key=str.lower)) 
print( '排序字符串，ASCII编码顺序,颠倒顺序:',sorted(strList, key=str.lower,reverse=True)) 


# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print('by_name:',L2)

#按成绩
def by_score(t):
    return -t[1]  # 按照成绩从高到低排序
    # return t[1]

L2 = sorted(L, key=by_score)
print('by_score:',L2)