
class Student(object):
    def get_score(self):
         return self._score
    
    def set_score(self,value):
         if not isinstance(value,int):
              raise ValueError("score value type is wrong")
         if value < 0 or value > 100:
              raise ValueError("score must between 0 ~ 100!")
         self._score = value

s = Student()
s.set_score(60)
print('set score:',s.get_score())



# 使用装饰器
class Students(object):
    @property  # 把一个get变成一个属性
    def score(self):
         return self._score
    
    @score.setter   # 把一个setter变成一个属性赋值
    def score(self,value):
         if not isinstance(value,int):
              raise ValueError("score value type is wrong")
         if value < 0 or value > 100:
              raise ValueError("score must between 0 ~ 100!")
         self._score = value

s = Students()
s.score = 60
print("加入装饰器后,设置分数:",s.score)


# 练习  请利用@property给一个Screen对象加上 width 和 height 属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
         return self._width
    
    @width.setter
    def width(self,_width):
        self._width = _width 
    @property
    def height(self):
         return self._height
    @height.setter
    def height(self,_height):
        self._height = _height    
    @property
    def resolution(self):
        return self._width * self._height
    
scr = Screen()
scr.height = 100
scr.width = 20     
print("set height:",scr.height,",set width:",scr.width)
print("resolution:",scr.resolution)

