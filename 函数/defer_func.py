# 递归函数调用
def fact(n):
    if n == 1:
        return 1
    return n * fact((n-1))

print("fact value:" , fact(5))        