sliceA = ['Michael', 'Sarah', 'Tracy']


print("索引0到2：",sliceA[:3])
print("索引0到1：",sliceA[:2])


# 创建0-100 数列
nums = list(range(100))

print("nums:",nums)

#取后10个数
print("取后10个数:",nums[-10:])

print("前10个数,每2个取一个：", nums[:10:2] )

print("所有数,每5个取一个:",nums[::5])

# 去除切片首尾的空格

def trim(s):
    while len(s)>0 and s[0]== ' ':
        s = s[1:]
    while len(s) > 0 and s[-1]==' ':
        s =s [:-1]
    return s    

print("trim:",trim(' a123b'))