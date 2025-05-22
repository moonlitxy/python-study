from collections.abc  import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print('key:',key)

# 默认情况下，dict迭代的是key
for value in d.values():
    print('value',value)



# 判断一个对象是否是可迭代对象
print(isinstance('abc',Iterable))


# 遍历 key value
for key,value in enumerate([1,3,9,6]):
    print("key:",key,"value:",value)


# 查找最小和最大元素
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    x = L[0]
    min = x
    max = x
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min,max)


print("min max :",findMinAndMax([1,3,9,6]))