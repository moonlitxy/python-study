import logging
# try 机制
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')



def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2


def main():
    try:
        print('try P24...')
        bar(0)
    except Exception as e:
        # print('Error:',e)
        logging.exception(e)
    finally:
        print('Finally P30...')

main()