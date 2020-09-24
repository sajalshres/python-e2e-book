# Object Oriented Programmingn (OOP)
Object-oriented Programming, or OOP, is a programming paradigm which provides a means of structuring programs so that properties(attributes) and behaviors(methods) are bundled into individual objects.

For example, an object could represent a car with properties like name, color, wheels etc. and with behaviors like accelerate, brake, steer etc. An object could also represent a person with properties like name, age, sex, etc and with behaviours like talking, eating, walking, running etc.

Another common programming paradigm is procedural programming which structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, which flow sequentially in order to complete a task.

The key takeaway is that objects are at the center of the object-oriented programming paradigm, not only representing the data, as in procedural programming, but in the overall structure of the program as well.

## Namespaces and Scopes

## Namespaces
* Is basically a system to make sure that all the names in a program are unique and can be used without any conflict.
* **Interesting fact**: Python implements namespaces as dictionaries
* There is a name-to-object mapping, with the names as keys and the objects as values.
* Multiple namespaces can use the same name and map it to a different object.
* **Name:** an unique identifier & **Space:** something related to scope.

### Types of Namespace

* **Local namespace** includes local names inside a function.
* **Global namespace** includes names from various imported modules that you are using in a project.
* **Built-in namespace** includes built-in functions and built-in exception names.

### Examples:


```python
# var1 is in the global namespace 
var1 = 5
def some_func(): 
    # var2 is in the local namespace 
    var2 = 6
    def some_inner_func(): 
        # var3 is in the nested local 
        # namespace 
        var3 = 7
```


```python
num_of_people = 5

def add_people(): 
    global num_of_people 
    num_of_people = num_of_people + 1
    print(num_of_people) 

add_people()
```

    6


## Scopes
* Namespace uniquely identifies names in a program, but it does't allow us to use a variable anywhere we want.
* Scopes are region where a Python's object are accessible without any prefix.

### Types of Scopes
During execution of a program, following scope exists:

* **innermost scope**, which is searched first, contains the local names
* **scopes of any enclosing functions**, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
* **next-to-last scope** contains the current module’s global names
* **outermost scope** (searched last) is the namespace containing built-in names

### Example


```python
def some_func(): 
    print("Inside some_func") 
    def some_inner_func(): 
        var = 10
        print("Inside inner function, value of var:",var) 
    some_inner_func() 
    print("Try printing var from outer function: ",var) 
some_func()
```

    Inside some_func
    Inside inner function, value of var: 10



    ---------------------------------------------------------------------------
    
    NameError                                 Traceback (most recent call last)
    
    <ipython-input-16-5fc192decd15> in <module>
          6     some_inner_func()
          7     print("Try printing var from outer function: ",var)
    ----> 8 some_func()


    <ipython-input-16-5fc192decd15> in some_func()
          5         print("Inside inner function, value of var:",var)
          6     some_inner_func()
    ----> 7     print("Try printing var from outer function: ",var)
          8 some_func()


    NameError: name 'var' is not defined



```python
a_num = 10
b_num = 11
 
def outer_func():
    global a_num
    a_num = 15
    b_num = 16
    def inner_func():
        global a_num
        a_num = 20
        b_num = 21
        print('a_num inside inner_func :', a_num)
        print('b_num inside inner_func :', b_num)
    inner_func()
    print('a_num inside outer_func :', a_num)
    print('b_num inside outer_func :', b_num)
     
outer_func()
print('a_num outside all functions :', a_num)
print('b_num outside all functions :', b_num)
```

    a_num inside inner_func : 20
    b_num inside inner_func : 21
    a_num inside outer_func : 20
    b_num inside outer_func : 16
    a_num outside all functions : 20
    b_num outside all functions : 11


## Class in Python
* User-defined data structure used to define arbitrary information about something.
* For example, a `Car()` class can have properties like name, type etc.
* **Note:** Class is just like a blueprint, it doesn't hold any state.

## Object in Python
* While class is a blueprint, an Object (Instance) is a copy of class with real values.
* Its like a Car with real name 'i20' and model '2019'

## A Glance at Classes

### Defining Class

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```


```python
class PythonClass:
    pass # pass is like a place holder where the code will enventually be written.
```

### Instance Attributes
* All classes create objects, and all objects contain characteristics called attributes (sometimes referred to as properties)
* Use the `__init__()` method to initialize the object's initial attributes. (State)
* `__init__()` method must have at least one argument `self`, which refers to object itself.


```python
class Car:
    
    # Instance Attributes
    def __init__(self, name, unid):
        self.name = name
        self.unid = unid 
```

**Note**: We never call the __init__() method; it gets automatically called when a new instance is created.

### Class Attributes
* Shared by all the instances of the class.
* Class attributes remain the same for all instances.


```python
class Car:
    
    # Class Attribute
    type = 'vehicle'
    
    # Instance Attributes
    def __init__(self, name, unid):
        self.name = name
        self.unid = unid 
```

### Instantiate an Object(s) from a Class
* means creating a new, unique instance of a class


```python
class Car:
    pass

Car()
```


    <__main__.Car at 0x1db880825e0>


```python
Car()
```


    <__main__.Car at 0x1db88082f40>


```python
car_A = Car()
car_B = Car()

car_A == car_B
```


    False

### Instance Methods

* Define inside a class, and can be used to get the content or perform operation on an instance/attributes.
* Similar to `__init__()` method, they also have `self` variable

```python
class Car:
    
    # Class Attribute
    type = 'vehicle'
    
    # Instance Attributes
    def __init__(self, name, unid):
        self.name = name
        self.unid = unid
    
    # An instance method
    def description(self):
        return "Car name is {} and its ID is {}".format(self.name, self.unid)
    
    # An instance method
    def honk(self, level=1):
        return "Car is honking at level {}".format(level)

# Instantiate Car object
i20 = Car("i20", 1123)

# Call instance method
print(i20.description())
print(i20.honk(2))
```

    Car name is i20 and its ID is 1123
    Car is honking at level 2


Attribute lookup prioritize the instance, when same attribute name occurs. See below:


```python
class Person:
    name = 'Kshitiz Maharjan'
    sex = 'Male'

p1 = Person()
print(p1.name, p1.sex)

p2 = Person()
p2.sex = 'Female'
print(p2.name, p2.sex)
print(p1.name, p1.sex)
```

    Kshitiz Maharjan Male
    Kshitiz Maharjan Female
    Kshitiz Maharjan Male


### Modify Attributes


```python
class Email:
    def __init__(self):
        self.is_sent = False
    
    def send_email(self, message):
        print("Sending:", message)
        self.is_sent = True
```


```python
email = Email()
email.is_sent
```


    False


```python
email.send_email("Ehh Bhaiii, K chhha?")
email.is_sent
```

    Sending: Ehh Bhaiii, K chhha?

    True

## Inheritance
* One class takes attributes and methods of another.
* Child class derived from Parent class
* Child class override or extend attributes and methods of parent's class.

### Syntax:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```


```python
class Car:
    
    # Class attributes
    type = 'vehicle'
    
    # Instance Attributes / Initialize
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
    
    # instance method
    def accelerate(self, speed):
        return "Car %s is acclerating at %d" % (self.name, speed)

# Child class of Car
class SuperCar(Car):
    def zoom(self):
        return "Car %s zoomed" % (self.name)
```


```python
i20 = Car('i20', 'Hyundai', 2020)
print(i20.type)
print(i20.name)
print(i20.year)
print(i20.accelerate(2))
```

    vehicle
    i20
    2020
    Car i20 is acclerating at 2

```python
lamborghini = SuperCar('Huracan', 'Lamborghini', 2019)
print(lamborghini.type)
print(lamborghini.name)
print(lamborghini.year)
print(lamborghini.accelerate(10))
print(lamborghini.zoom())
```

    vehicle
    Huracan
    2019
    Car Huracan is acclerating at 10
    Car Huracan zoomed


### Multiple Inheritance
* Python also supports multiple inheritance.

### Syntax:
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

* If attribute not found in `DerivedClassName`, it is searched in `Base1`
* If not found there, it is searched in `Base2`, and the search goes on.

### Override

* Child classes can override attributes and methods of parent clasess. 
* See example below:


```python
class Car:
    
    # Class attributes
    type = 'vehicle'
    
    # Instance Attributes / Initialize
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
    
    # instance method
    def accelerate(self, speed):
        return "Car %s is acclerating at %d" % (self.name, speed)

# Child class of Car
class SuperCar(Car):
    type = 'Luxury vehicle'
    def zoom(self):
        return "Car %s zoomed" % (self.name)
```


```python
i20 = Car('i20', 'Hyundai', 2020)
print(i20.type)

lamborghini = SuperCar('Huracan', 'Lamborghini', 2019)
print(lamborghini.type)

```

    vehicle
    Luxury vehicle

```python
class Car:
    
    # Class attributes
    type = 'vehicle'
    
    # Instance Attributes / Initialize
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
    
    # instance method
    def accelerate(self, speed):
        return "Car %s is acclerating at %d" % (self.name, speed)

# Child class of Car
class SuperCar(Car):
    type = 'Luxury vehicle'
    
    def accelerate(self, speed):
        return "Car %s is acclerating at %d" % (self.name, speed*2)
    
    def zoom(self):
        return "Car %s zoomed" % (self.name)


i20 = Car('i20', 'Hyundai', 2020)
print(i20.accelerate(10))

lamborghini = SuperCar('Huracan', 'Lamborghini', 2019)
print(lamborghini.accelerate(10))
```

    Car i20 is acclerating at 10
    Car Huracan is acclerating at 20


### `isinstance()`
* determines if an instance is also an instance of a certain parent class.


```python
isinstance(lamborghini, Car)
```


    True


```python
isinstance(lamborghini, SuperCar)
```


    True


```python
isinstance(1, int)
```


    True


```python
x = 4.2

isinstance(x, (int, float))
```


    True

## Private Variables


```python
class Car:
    
    # Instance Attributes / Initialize
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.__type = 'vehicle'
        self._num_of_wheels = 4
    
    def get_type(self):
        return self.__type
    
    # instance method
    def accelerate(self, speed):
        return "Car %s is acclerating at %d" % (self.name, speed)
```


```python
i20 = Car('i20', 'Hyundai', 2020)
i20.get_type()
```


    'vehicle'


```python
i20.__type
```


    ---------------------------------------------------------------------------
    
    AttributeError                            Traceback (most recent call last)
    
    <ipython-input-37-e31da153b0a7> in <module>
    ----> 1 i20.__type


    AttributeError: 'Car' object has no attribute '__type'

```python
i20._Car__type
```


    'vehicle'


```python
i20._num_of_wheels
```


    4

## Name Mangling

* **Note** : Revisit after automation module.
