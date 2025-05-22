# 匿名函数的使用
list1 = list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9,10]))
print('list1:',list1)

# 改造下方函数为匿名函数
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print('L:',L)

print("ans:",list(filter(lambda x: x%2 ==1,range(1,20))))