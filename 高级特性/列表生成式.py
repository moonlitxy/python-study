
s = [x*x for x in range(1,11) if x%2==0]
print("s:",s)
    

# 字母转化为小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower()  for s in L1 if isinstance(s,str)]
print('change lower:',L2)