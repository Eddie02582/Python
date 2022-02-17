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

## 存取權限

python 並沒有像其他OOP的程式可以透過private/protected/public等修飾詞來管理,透過__開頭來表示私有
將原本的self.name 改成self.__name,self.age 改成self.__age


```python
class Person:    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(self.__name + "'s age is: " + str(self.__age))

```

當使用person.__age就會出現 AttributeError: 'Person' object has no attribute '__age'
```
person = Person("Eddie",30)
person.__age
```


但還是可以透過下列方式
```
person._Person__age
```


## 屬性
當欄位設定為私有屬性,可以透過屬性的方式取得

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

基本上這兩個都可以不透過創件物件來使用函數

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

執行可以發現一樣

```python
>>> Person.static_method()
static_method
>>> Person.class_method()
class_method
```

透過class_method 建立instance,由於python 沒有多載,所以無法有用不同的__init__(建構式)產生物件,這邊的cls 類似於Person


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

就可以透過
```python
person = Person.from_birth_year("Eddie",1991)

```

當然使用staticmethod也可以

```pytohn
   ...
    @staticmethod
    def static_from_birth_year(name,birth_year):
        return Person(name, date.today().year - birth_year) 

```



既然這樣都使用staticmethod就好,當使用繼承時,cls 就產生差別,使用classmethod是Man的實體,使用static_from_birth_year是Person實體

```python
class Man(Person):
    sex = 'Male'  
man = Man.from_birth_year('John', 1985)
print(isinstance(man, Man))
man1 = Man.static_from_birth_year('John', 1985)
print(isinstance(man1, Man))
```

#繼承

子類別繼承父類別可以使用其函數(非private,這邊將__改成_),也可以新增或改寫函數,可以透過super呼叫父類別的函數<br>
這邊的繼承相當於其他語言的virtual

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
        #改寫init,並透過super先呼叫父類別的__init__
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
        print(self._name + "是" + self._grade)

```


如果要使用abstract ,在父類別不實作,在子類別實作

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
        print(self._name + "是" + self._grade)
```

假設如果拿掉display就會發生錯誤

```python
>>> student1 = Student("Eddie",30,'senior')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    student1 = Student("Eddie",30,'senior')
TypeError: Can't instantiate abstract class Student with abstract methods display
```

也可以使用







