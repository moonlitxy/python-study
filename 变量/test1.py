import  keyword

a = "s"
b = 's1'

print(a,b)

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

var1 = '字符串1'
var2 = "字符串2"

var3 = """字符串3"""

print("index1:",var1[2])

var4 = "hello world!"
var4 = var4[::-1]
print("var4 slice:", var4)


lst = [0,1,2,3,4]
lst.append("8")

exd = [9,9,9]
lst.extend(exd)
print("lst:", lst)


