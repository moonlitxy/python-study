
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
s = d.get("mic",-1)
if s == -1:
    print("不存在")
else:
    print("存在")



# set 与 dict一样，区别在于 set 没有value
h = {1,2,3,4,7}
print("set:",h)

h1 = set([1,3,5,3,7,2,9])
print("h1:",h1)

h.add(5)
print("h append key after:",h)


h.remove(3)
print("h remove key after:",h)


a = [1,9,4,6,10]
a.sort()
print("排序后：",a)

# 不可变对象
b = 'abc'
c = b.replace('a','A')
print("replace str :",c,",b:",b)