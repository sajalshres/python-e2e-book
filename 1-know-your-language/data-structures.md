# Data Structures
* Provides structure which can hold data together.
* Used to store a collection of related data.

## Lists
* Holds ordered collection of items.
* Should be enclosed in square brackets i.e. `[]`
* We can add, remove or even search items in a lists, implying Lists are mutable data types.

### List Methods:
`list.append(x)`
Add an item to the end of the list. Equivalent to `a[len(a):] = [x]`.

`list.extend(iterable)`
Extend the list by appending all the items from the `iterable`. Equivalent to `a[len(a):] = iterable`.

`list.insert(i, x)`
Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

`list.remove(x)`
Remove the first item from the list whose value is equal to x. It raises a `ValueError` if there is no such item.

`list.pop([i])`
Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

`list.clear()`
Remove all items from the list. Equivalent to `del a[:]`.

`list.index(x[, start[, end]])`
Return zero-based index in the list of the first item whose value is equal to x. Raises a `ValueError` if there is no such item.
The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

`list.count(x)`
Return the number of times x appears in the list.

`list.sort(key=None, reverse=False)`
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

`list.reverse()`
Reverse the elements of the list in place.

`list.copy()`
Return a shallow copy of the list. Equivalent to a[:].

An example that uses most of the `list` methods:


```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
```

Output:


    2


```python
fruits.count('tangerine')
```

Output:


    0


```python
fruits.index('banana')
```

Output:


    3


```python
fruits.index('banana', 4)
```

Output:


    6


```python
fruits.reverse()
fruits
```

Output:


    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']


```python
fruits.append('grape')
fruits
```

Output:


    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']


```python
fruits.sort()
fruits
```

Output:


    ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']


```python
fruits.pop()
```

Output:


    'pear'

## List as a Stack
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use `append()`. To retrieve an item from the top of the stack, use `pop()`


```python
stack = [3, 4, 5]
stack.append(6)
```


```python
stack
```

Output:


    [3, 4, 5, 6]


```python
stack.append(7)
stack
```

Output:


    [3, 4, 5, 6, 7]


```python
stack.pop()
```

Output:


    7


```python
stack
```

Output:


    [3, 4, 5, 6]


```python
stack.pop()
```

Output:


    6


```python
stack
```

Output:


    [3, 4, 5]

## List as Queue
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose.

To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends. For example:


```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
```

Output:


    'Eric'


```python
queue.popleft()                 # The second to arrive now leaves
```

Output:


    'John'


```python
queue                           # Remaining queue in order of arrival
```

Output:


    deque(['Michael', 'Terry', 'Graham'])

## List Comprehensions
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

### Problem: Create list of squares

Traditional approach:


```python
squares = []
for x in range(10):
    squares.append(x**2)

squares
```

Output:


    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


```python
squares = [x**2 for x in range(10)] # More concise and readable right?
squares
```

Output:


    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### Few more examples:


```python
[python for python in 'python']
```

Output:


    ['p', 'y', 't', 'h', 'o', 'n']


```python
[number for number in range(10)]
```

Output:


    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


```python
[number for number in range(10) if number % 2 == 0]
```

Output:


    [0, 2, 4, 6, 8]


```python
[number for number in range(100) if number % 2 == 0 if number % 5 == 0]
```

Output:


    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


```python
['Even' if number%2==0 else "Odd" for number in range(10)]
```

Output:


    ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


```python

# create a new list with the values doubled
[x*2 for x in vec]
```

Output:


    [-8, -4, 0, 4, 8]


```python
# filter the list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
[x for x in vec if x >= 0]
```

Output:


    [0, 2, 4]


```python
# apply a function to all the elements
vec = [-4, -2, 0, 2, 4]
[abs(x) for x in vec]
```

Output:


    [4, 2, 0, 2, 4]

## `del`


```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
```

Output:


    [1, 66.25, 333, 333, 1234.5]


```python
del a[2:4]
a
```

Output:


    [1, 66.25, 1234.5]


```python
del a # del can also be used to delete entire variables
a
```

Output:


    ---------------------------------------------------------------------------
    
    NameError                                 Traceback (most recent call last)
    
    <ipython-input-49-91b8cc03fd62> in <module>
    ----> 1 del a # del can also be used to delete entire variables
          2 a


    NameError: name 'a' is not defined


## Tuples
Tuples are like lists except they are immutable like strings. They are useful when a statement or a function can safely assume that collection of values will not change.


```python
t = 12345, 54321, 'hello!'
t[0]
```

Output:


    12345


```python
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
```

Output:


    ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))


```python
# Tuples are immutable:
t[0] = 88888
```

Output:


    ---------------------------------------------------------------------------
    
    TypeError                                 Traceback (most recent call last)
    
    <ipython-input-52-9e19cce22619> in <module>
          1 # Tuples are immutable:
    ----> 2 t[0] = 88888


    TypeError: 'tuple' object does not support item assignment

```python
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```

Output:


    ([1, 2, 3], [3, 2, 1])


```python
v[0][0] = 'Changed'
v
```

Output:


    (['Changed', 2, 3], [3, 2, 1])

### Sequence Unpacking
Reverse operation of tuple packing


```python
t = 12345, 54321, 'hello!' # Tuple packing
a, b, c = t # Sequence unpacking
print(a,b,c)

# Requres as many variables on left as ther are on right element.
```

Output:

    12345 54321 hello!


## Sets
* Unordered collection with no duplicate elements.
* Supports mathematical operations like union, interaction, difference.

You can create sets using `{}` or `set()` function


```python
shopping_basket = {'apple', 'orange', 'pineapple', 'apple', 'pear'}
shopping_basket
```

Output:


    {'apple', 'orange', 'pear', 'pineapple'}


```python
shopping_basket = set()
type(shopping_basket)
```

Output:


    set


```python
shopping_basket = {}
type(shopping_basket)
```

Output:


    dict


```python
shopping_basket = {'apple', 'orange', 'pineapple', 'apple', 'pear'}
'apple' in shopping_basket
```

Output:


    True


```python
'strawberry' in shopping_basket
```

Output:


    False


```python
a = set('abracadabra')
b = set('alacazam')
a # unique letters in a
```

Output:


    {'a', 'b', 'c', 'd', 'r'}


```python
b # unique letters in b
```

Output:


    {'a', 'c', 'l', 'm', 'z'}


```python
a - b # letters in a but not in b
```

Output:


    {'b', 'd', 'r'}


```python
a | b # letters in a or b or both
```

Output:


    {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}


```python
a & b # letters in both a and b
```

Output:


    {'a', 'c'}


```python
a ^ b # letters in a or b but not bot
```

Output:


    {'b', 'd', 'l', 'm', 'r', 'z'}

### Set comprehensions


```python
a = {x for x in 'abracadabra' if x not in 'abc'}
a
```

Output:


    {'d', 'r'}

## Dictionary
A dictionary is data structure similar to contacts. You can find an address or contact of a person by his/her/its name.
In dictionary, we associate name (i.e. keys) with details (i.e. values)
Dictionary are indexed by keys, which can be any immutable types (string or numbers) and must be unique.


```python
contact = {
    'Ram Kasula': 9840298755,
    'Anu Pau': 98651201503,
    'Kade Hade': 9863331239
}

contact['Ram Kasula']
```

Output:


    9840298755


```python
del contact['Kade Hade']
contact
```

Output:


    {'Ram Kasula': 9840298755, 'Anu Pau': 98651201503}


```python
contact['Santa Behen'] = 9845022233
contact
```

Output:


    {'Ram Kasula': 9840298755, 'Anu Pau': 98651201503, 'Santa Behen': 9845022233}


```python
list(contact)
```

Output:


    ['Ram Kasula', 'Anu Pau', 'Santa Behen']


```python
sorted(contact)
```

Output:


    ['Anu Pau', 'Ram Kasula', 'Santa Behen']


```python
'Santa Behen' in contact
```

Output:


    True


```python
'Kade Hade' in contact
```

Output:


    False


```python
dict([('A',1), ('B',2)])
```


    {'A': 1, 'B': 2}

### Dictionary Comprehensions


```python
{number: number**2 for number in (1, 2, 3)}
```

Output:


    {1: 1, 2: 4, 3: 9}
