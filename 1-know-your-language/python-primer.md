# Applying Primer
## Numbers
The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. 
Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages 
(for example, Pascal or C); parentheses (()) can be used for grouping. For example:
```python
>>> 2+2
4
```
```python
>>> 50 - 5*6
20
```
```python
>>> (50 - 5*6) / 4
5.0
```
```python
>>> 8 / 5  # division always returns a floating point number
1.6
```
The integer numbers (e.g. 2, 4, 20) have type `int`, the ones with a fractional part (e.g. 5.0, 1.6) have type `float`.
```python
>>> 17 // 3  # floor division discards the fractional part
5
```
```python
>>> 17 % 3  # the % operator returns the remainder of the division
2
```
With Python, it is possible to use the `**` operator to calculate powers
```python
>>> 5 ** 2  # 5 squared
25
```
```python
>>> 2 ** 7  # 2 to the power of 7
128
```
The equal sign (`=`) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
If a variable is not “defined” (assigned a value), trying to use it will give you an error:
```python
>>> variable_not_exists # try to access an undefined variable
---------------------------------------------------------------------------

NameError Traceback (most recent call last)

<ipython-input-11-087486976af0> in <module>
----> 1 variable_not_exists # try to access an undefined variable
NameError: name 'variable_not_exists' is not defined
```
In interactive mode, the last printed expression is assigned to the variable `_`. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:
```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax # Result is 12.5625
>>> price + _   # Result is 113.0625
>>> round(_, 2)
900
```
This variable should be treated as read-only by the user. Don’t explicitly assign a value to it `_` you would create an independent local variable with the same name masking the built-in variable with its magic behavior.
# Strings
Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 
`\` can be used to escape quotes:
```python
>>>'spam eggs'  # single quotes
'spam eggs'
```
```python
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
```
```python
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
```
```python
'"Yes," they said.'
>>> '"Yes," they said.'
```
```python
>>> "\"Yes,\" they said."
'"Yes," they said.'
```
```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```
The `print()` function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```
```python
>>> print('"Isn\'t," they said.')
"Isn't," they said.
```
```python
s = 'First line.\nSecond line.'  # \n means newline
```
```python
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
```
```python
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
```
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote:
```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
```
```python
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:
```python
>>> print("""\
...     Usage: thingy [OPTIONS]
...      -hDisplay this usage message
...      -H hostname   Hostname to connect to
...     """)
Usage: thingy [OPTIONS]
 -hDisplay this usage message
 -H hostname   Hostname to connect to
```
Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`:
```python
>>> 3 * 'un' + 'ium'
'unununium'
```
```python
>>> 'Py' 'thon' # Two or more string literals next to each other are automatically concatenated.
'Python'
```
```python
>>> text = ('Put several strings within parentheses '
...            'to have them joined together.')
>>> print(text)
Put several strings within parentheses to have them joined together.
```
```python
>>> prefix = 'Py'
>>> refix 'thon'  # can't concatenate a variable and a string literal
File "<ipython-input-30-7c051b293f22>", line 2
refix 'thon'  # can't concatenate a variable and a string literal
  ^
SyntaxError: invalid syntax
```
```python
>>> prefix = 'Py'
>>> prefix + 'thon' # If you want to concatenate variables or a variable and a literal, use +
'Python'
```
Strings can be indexed (subscripted), with the first character having index `0`. There is no separate character type; a character is simply a string of size one:
```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
```
```python
>>> word[-1]  # last character
'n'
```
```python
>>> word[-2]  # second-last character
'o'
```
Note that since -0 is the same as 0, negative indices start from -1.
```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
```
```python
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```
Note how the start is always included, and the end always excluded. This makes sure that `s[:i] + s[i:]` is always equal to s:
```python
>>> word[:2] + word[2:]
'Python'
```
```python
word[:4] + word[4:]
'Python'
```
```python
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
```
```python
>>> word[4:]   # characters from position 4 (included) to the end
'on'
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```python
>>> word[42]  # the word only has 6 characters
---------------------------------------------------------------------------

IndexErrorTraceback (most recent call last)

<ipython-input-41-469c6d99b5b2> in <module>
----> 1 word[42]  # the word only has 6 characters
IndexError: string index out of range
```
```python
word[4:42] # out of range slice indexes are handled gracefully when used for slicing
'on'
```
The built-in function `len()` returns the length of a string:
```python
>>> len(word)
6
```
# Lists
Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```
Like `strings` (and all other built-in sequence types), `lists` can be indexed and sliced:
```python
>>> squares[0]  # indexing returns the item
1
```
```python
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```
```python
>>> squares + [36, 49, 64, 81, 100]  # Lists also support operations like concatenation
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here\
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```
You can also add new items at the end of the list, by using the `append()` method:
```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
```python
>>> letters[2:5] = ['C', 'D', 'E']  # replace some values
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
```
```python
>>> letters[2:5] = [] # now remove them
>>> letters
['a', 'b', 'f', 'g']
```
```python
>>> letters[:] = [] # clear the list
>>> letters
[]
```
```python
# It is possible to nest lists (create lists containing other lists), for example:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x[0]
['a', 'b', 'c']
```
```python
>>> x[0][1]
'b'
```
```python
# Fibonacci series:
>>> a, b = 0, 1
... while a < 10:
... 	print(a)
... 	a, b = b, a+b
0
1
1
2
3
5
8
```
```python
>>> a, b = 0, 1
... while a < 20:
... 	print(a, end=',')
... 	a, b = b, a+b
0,1,1,2,3,5,8,13,
```