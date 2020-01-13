# Functions

* Functions are named blocks of statements.
* Reusable piece of code.
* Already used built-in functions like `len()`, `type()`, `int()` etc.

Example:


```python
def greet(name):
    print("Hi,", name)

# Let's call the function we just defined:
name = 'Prashant'
greet(name)
```

    Hi, Prashant
    


```python
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
```

    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
    

Keyword `def` introduces a function definition. It must be followed by the function name and the parenthesized list of parameters. The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. There are tools which use these docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; 

it’s good practice to include docstrings in code that you write, so make a habit of it.

The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names.

Function definition introduces the function name in the current symbol table. The value of the function name has a type that is recognized by the interpreter as a user-defined function.


```python
fib

f = fib
f(100)
```

    0 1 1 2 3 5 8 13 21 34 55 89 
    

Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it’s a built-in name). 


```python
fib(0)
print(fib(0))
```

    
    
    None
    

## Defining Functions
It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined

### Default Argument Values
The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:


```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

This function can be called in several ways:


```python
ask_ok('Do you really want to quit?')
```

    Do you really want to quit?y
    




    True




```python
ask_ok('OK to overwrite the file?', 2)
```

    OK to overwrite the file?nope
    




    False




```python
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
```

    OK to overwrite the file?haha
    Come on, only yes or no!
    OK to overwrite the file?hoho
    Come on, only yes or no!
    OK to overwrite the file?no
    




    False



### Keyword Arguments
Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:


```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:


```python
parrot(1000)                                          # 1 positional argument
```

    -- This parrot wouldn't voom if you put 1000 volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's a stiff !
    


```python
parrot(voltage=1000)                                  # 1 keyword argument
```

    -- This parrot wouldn't voom if you put 1000 volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's a stiff !
    


```python
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
```

    -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's a stiff !
    


```python
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
```

    -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's a stiff !
    


```python
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
```

    -- This parrot wouldn't jump if you put a million volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's bereft of life !
    


```python
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

    -- This parrot wouldn't voom if you put a thousand volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's pushing up the daisies !
    

but all the following calls would be invalid:
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
When a final formal parameter of the form `**name` is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form `*name` (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (`*name` must occur before `**name`.) For example, if we define a function like this:


```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

It could be called like this:


```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

    -- Do you have any Limburger ?
    -- I'm sorry, we're all out of Limburger
    It's very runny, sir.
    It's really very, VERY runny, sir.
    ----------------------------------------
    shopkeeper : Michael Palin
    client : John Cleese
    sketch : Cheese Shop Sketch
    

### Special parameters
By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

A function definition may look like:
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
where `/` and `*` are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

 #### Positional-or-Keyword Arguments
If `/` and `*` are not present in the function definition, arguments may be passed to a function by position or by keyword.

#### Positional-Only Parameters
The `/` is used to logically separate the positional-only parameters from the rest of the parameters. If there is no `/` in the function definition, there are no positional-only parameters.

#### Keyword-Only Arguments
To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an `*` in the arguments list just before the first keyword-only parameter.

#### Examples:


```python
def standard_arg(arg):
    print(arg)
```

The first function definition, `standard_arg`, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:


```python
standard_arg(2)
```

    2
    


```python
standard_arg(arg=2)
```

    2
    


```python
def pos_only_arg(arg, /):
    print(arg)
```

The second function pos_only_arg is restricted to only use positional parameters as there is a `/` in the function definition:


```python
pos_only_arg(1)
```

    1
    


```python
pos_only_arg(arg=1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-29-434db44f4ff9> in <module>
    ----> 1 pos_only_arg(arg=1)
    

    TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'



```python
def kwd_only_arg(*, arg):
    print(arg)
```

The third function kwd_only_args only allows keyword arguments as indicated by a `*` in the function definition:


```python
kwd_only_arg(3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-896c53ef896c> in <module>
    ----> 1 kwd_only_arg(3)
    

    TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given



```python
kwd_only_arg(arg=3)
```

    3
    


```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

And the last uses all three calling conventions in the same function definition:


```python
combined_example(1, 2, 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-35-037a05a37207> in <module>
    ----> 1 combined_example(1, 2, 3)
    

    TypeError: combined_example() takes 2 positional arguments but 3 were given



```python
combined_example(1, 2, kwd_only=3)
```

    1 2 3
    


```python
combined_example(1, standard=2, kwd_only=3)
```

    1 2 3
    


```python
combined_example(pos_only=1, standard=2, kwd_only=3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-39-cb7e0b67eae9> in <module>
    ----> 1 combined_example(4, pos_only=1, standard=2, kwd_only=3)
    

    TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


### Lambda Expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:


```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
```




    42




```python
f(1)
```




    43



## Documentation Strings


```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
```

    Do nothing, but document it.
    
        No, really, it doesn't do anything.
        
    

## Coding Style
For Python, PEP 8 has emerged as the style guide that most projects adhere to; it promotes a very readable and eye-pleasing coding style. Every Python developer should read it at some point; here are the most important points extracted for you:

* Use 4-space indentation, and no tabs.
* 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
* Wrap lines so that they don’t exceed 79 characters.
* This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
* Use blank lines to separate functions and classes, and larger blocks of code inside functions.
* When possible, put comments on a line of their own.
* Use docstrings.
* Use spaces around operators and after commas, but not directly inside bracketing constructs: `a = f(1, 2) + g(3, 4)`.
* Name your classes and functions consistently; the convention is to use `UpperCamelCase` for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument
* Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
* Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.
