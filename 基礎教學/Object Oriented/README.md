# Object Oriented




## Define Class

```python
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

```

## Use Class

```python
person = Person("Eddie",30)
person.display

```

## �s���v��

python �èS������LOOP���{���i�H�z�Lprivate/protected/public���׹����Ӻ޲z,�z�L__�}�Y�Ӫ�ܨp��
�N�쥻��self.name �令self.__name,self.age �令self.__age


```python
class Person:    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(self.__name + "'s age is: " + str(self.__age))

```

��ϥ�person.__age�N�|�X�{ AttributeError: 'Person' object has no attribute '__age'
```
person = Person("Eddie",30)
person.__age
```


���٬O�i�H�z�L�U�C�覡
```
person._Person__age
```


## �ݩ�
�����]�w���p���ݩ�,�i�H�z�L�ݩʪ��覡���o

```python
class Person:    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
        
    def display(self):
        print(self.__name + "'s age is: " + str(self.__age))

```


## staticmethod vs classmethod

�򥻤W�o��ӳ��i�H���z�L�Х󪫥�ӨϥΨ��

```python
class Person:    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    @staticmethod
    def static_method():
        print('static_method')
        
    @classmethod
    def class_method(cls):
        print('class_method')
        
    def display(self):
        print(self.__name + "'s age is: " + str(self.__age))

```

����i�H�o�{�@��

```python
>>> Person.static_method()
static_method
>>> Person.class_method()
class_method
```

�z�Lclass_method �إ�instance,�ѩ�python �S���h��,�ҥH�L�k���Τ��P��__init__(�غc��)���ͪ���,�o�䪺cls ������Person


```python
from datetime import date

class Person:    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    @classmethod
    def from_birth_year(cls,name,birth_year):
        return cls(name, date.today().year - birth_year)
        
    def display(self):
        print(self.__name + "'s age is: " + str(self.__age))
```

�N�i�H�z�L
```python
person = Person.from_birth_year("Eddie",1991)

```

��M�ϥ�staticmethod�]�i�H

```pytohn
   ...
    @staticmethod
    def static_from_birth_year(name,birth_year):
        return Person(name, date.today().year - birth_year) 

```



�J�M�o�˳��ϥ�staticmethod�N�n,��ϥ��~�Ӯ�,cls �N���ͮt�O,�ϥ�classmethod�OMan������,�ϥ�static_from_birth_year�OPerson����

```python
class Man(Person):
    sex = 'Male'  
man = Man.from_birth_year('John', 1985)
print(isinstance(man, Man))
man1 = Man.static_from_birth_year('John', 1985)
print(isinstance(man1, Man))
```

#�~��

�l���O�~�Ӥ����O�i�H�ϥΨ���(�Dprivate,�o��N__�令_),�]�i�H�s�W�Χ�g���,�i�H�z�Lsuper�I�s�����O�����<br>
�o�䪺�~�Ӭ۷���L�y����virtual

```python
class Person:    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
        
    def display(self):
        print(self._name + "'s age is: " + str(self._age))
        
        
class Student(Person):   

    def __init__(self, name, age, grade):
        #��ginit,�óz�Lsuper���I�s�����O��__init__
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade


    def display(self):
        super().display()
        print(self._name + "�O" + self._grade)

```


�p�G�n�ϥ�abstract ,�b�����O����@,�b�l���O��@

```python
import abc
#or can use =>class Person(abc.ABC): 
class Person(metaclass=abc.ABCMeta):    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
        
    @abc.abstractmethod
    def display(self):
        return NotImplemented
        
        
class Student(Person):   

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade
        
    def display(self):
        super().display()
        print(self._name + "�O" + self._grade)
```

���]�p�G����display�N�|�o�Ϳ��~

```python
>>> student1 = Student("Eddie",30,'senior')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    student1 = Student("Eddie",30,'senior')
TypeError: Can't instantiate abstract class Student with abstract methods display
```

�]�i�H�ϥ�







