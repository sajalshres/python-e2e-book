# Errors and Exceptions
Until now error messages haven’t been more than mentioned, but if you have tried out the examples you have probably seen some. 
There are (at least) two distinguishable kinds of errors:
* Syntax errors
* Exceptions

## Syntax Errors (Parsing Errors)

**Example:**


```python
>>> while True print('Ohh Man!, not again')
```

*Output:*


```python
  File "<ipython-input-2-a34048f0cb3e>", line 1
    while True print('Ohh Man!, not again')
               ^
SyntaxError: invalid syntax
```

The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow: 

In the example, the error is detected at the function `print()`, since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

## Exceptions
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions

**Example:**


```python
10 * (1/0)
```

*Output:*


```python
---------------------------------------------------------------------------

ZeroDivisionError                         Traceback (most recent call last)

<ipython-input-3-0b280f36835c> in <module>
----> 1 10 * (1/0)
```


```python
ZeroDivisionError: division by zero
```

**Example:**

```python
4 + spam*3
```

*Output:*


```python
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-4-c98bb92cdcac> in <module>
----> 1 4 + spam*3
```


```python
NameError: name 'spam' is not defined
```

**Example:**

```python
'2' + 2
```

*Output:*


```python
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-5-d2b23a1db757> in <module>
----> 1 '2' + 2
```


```python
TypeError: can only concatenate str (not "int") to str
```


## Handling Exception
Exceptions ca be handled using the try..except statement. You basically put all your statements in `try` block and put error handlers in `except` block

**Example:**


```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

*Output:*

```python
Please enter a number: $2
Oops!  That was no valid number.  Try again...
Please enter a number: 2
```


## `raise` Exceptions

The `raise` statement allows the programmer to force a specified exception to occur.

**Example:**


```python
raise NameError('How you doin?')
```

*Output:*


```python
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-7-6a59564f9d69> in <module>
----> 1 raise NameError('How you doin?')
```


```python
NameError: How you doin?
```

If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the `raise` statement allows you to re-raise the exception:

**Example:**


```python
try:
    raise NameError('How you doin?')
except NameError:
    print('An exception flew by!, How you doin?')
    raise
```

*Output:*

```python
An exception flew by!, How you doin?
```

```python
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-8-4bd984bb795d> in <module>
      1 try:
----> 2     raise NameError('How you doin?')
      3 except NameError:
      4     print('An exception flew by!, How you doin?')
      5     raise
```


```python
NameError: How you doin?
```


## Let's clean up
The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.

**Example:**


```python
try:
    raise NameError('How you doin?')
finally:
    print('Goodbye, world!')
```

*Output:*

```python
Goodbye, world!
```

```python
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-9-5e7cc627406e> in <module>
      1 try:
----> 2     raise NameError('How you doin?')
      3 finally:
      4     print('Goodbye, world!')
```


```python
NameError: How you doin?
```
