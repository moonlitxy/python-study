from datetime import datetime
def now():
    print("now is now")

f = now
# print('函数原来名称:',f.__name__)
print(f.__name__)



def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
