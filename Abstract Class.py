from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print('Passed Value: ',x)
    @abstractmethod
    def task(self):
        print('We are inside absclass task.')
class test_method(Absclass):
    def task(self):
        print('We are inside test_method task.')
test_obj=test_method()
test_obj.task()
test_obj.print(100)       