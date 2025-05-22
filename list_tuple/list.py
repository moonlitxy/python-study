from datetime import datetime
classmates = ["michael","Bob","john"]
print("当前时间：",datetime.now())

print("list 长度：",len(classmates))
print("index 0 is:", classmates[0])
print("error index is :", classmates[-3])  # -4越界  当为-1  -2 -3 时，数据倒着开始的

# 向list末尾中添加一个元素
classmates.append("maria")
print("append bytes ans is :",classmates[-1])

# 插入元素到指定的索引位置
classmates.insert(1,"index2")
print("index 1 value:",classmates[1])

# 删除末尾元素
classmates.pop()
print("删除后的列表为：", classmates)

# 删除指定位置的元素
classmates.pop(1)
print("remove taget index value:", classmates)