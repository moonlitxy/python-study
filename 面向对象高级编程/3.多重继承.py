
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')
    

# 多重继承
class Dog(object,Runnable):
    pass

