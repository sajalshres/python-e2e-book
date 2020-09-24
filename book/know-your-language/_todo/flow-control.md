# Control the flow

Python uses the usual flow control statements known from other languages, with some twists.

There are three control flow statements in Python - `if`, `for` and `while`.

## `if` Statement
The most well-known statement type is the if statement. 
For example:


```python
if True:
    print('Yup, it\'s true')
```

    Yup, it's true

```python
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0: # keyword ‘elif’ is short for ‘else if’
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

    Please enter an integer: 5
    More


## `for` Statement
The for statement in Python differs a bit from what you may be used to in C or Pascal.
Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):


```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

```

    cat 3
    window 6
    defenestrate 12


## The `range()` function
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.


```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4

```python
for i in range(5, 10):
    print(i)
```

    5
    6
    7
    8
    9

```python
for i in range(-10, -100, -30):
    print(i)
```

    -10
    -40
    -70


We can get a list from a range


```python
list(range(4))
```


    [0, 1, 2, 3]

## `break`, `continue` and `else`

The break statement, like in C, breaks out of the innermost enclosing for or while loop.

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. 


```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

```python
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```


When used with a loop, the `else` clause has more in common with the `else` clause of a `try` statement than it does with that of `if` statements: a `try` statement’s `else` clause runs when no exception occurs, and a loop’s `else` clause runs when no `break` occurs. 

The `continue` statement, also borrowed from C, continues with the next iteration of the loop:


```python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
```

```python
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```


## `pass` statement

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:


```python
class MyEmptyClass:
    pass
```

`pass` can also be used as a place-holder for a function or conditional body when you are working on something new, to allow you to keep thinking at a more abstract level. 


```python
def initlog(*args):
    pass   # TODO: Implement this!
```
