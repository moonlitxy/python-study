import functools

# 转化进制
def int2(x, base=2):
    return int(x, base)



# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base = 2)
# ans = int2('2')
ans = int2('1000000')
print("二进制结果:",ans)