
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
