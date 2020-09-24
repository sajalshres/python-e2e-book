# Time to debug

The module `pdb` defines an interactive source code debugger for Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.

Insert the following code at the location where you want to break into the debugger:

```python
import pdb; pdb.set_trace()
```

When the line above is executed, Python stops and waits for you to tell it what to do next. You’ll see a `(Pdb)` prompt. This means that you’re now paused in the interactive debugger and can enter a command.

Starting in Python 3.7, there’s another way to enter the debugger. PEP 553 describes the built-in function breakpoint(), which makes entering the debugger easy and consistent:

```python
breakpoint()
```

By default, `breakpoint()` will import `pdb` and call `pdb.set_trace()`, as shown above. However, using `breakpoint()` is more flexible and allows you to control debugging behavior via its API and use of the environment variable `PYTHONBREAKPOINT`. 

For example, setting `PYTHONBREAKPOINT=0` in your environment will completely disable `breakpoint()`, thus disabling debugging. If you’re using Python 3.7 or later, use `breakpoint()` instead of `pdb.set_trace()`.

You can also break into the debugger, without modifying the source and using `pdb.set_trace()` or `breakpoint()`, by running Python directly from the command-line and passing the option `-m pdb`. 

```shell
$ python3 -m pdb password_strength.py HelloPrashant1
```

Let’s look at the example. Here’s the `debug_1.py` source:

```python
#!/usr/bin/env python3

filename = __file__
import pdb; pdb.set_trace()
print(f'path = {filename}')
```

If you run this from your shell, you should get the following output:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_1.py 
> d:\repositories\python-e2e-book\2-automate\debugging\debug_1.py(5)<module>()
-> print(f'path = {filename}')
(Pdb) 
```

Now enter `p filename`. You should see:

```python
(Pdb) p filename
'.\\debug_1.py'
(Pdb)
```

Since you’re in a shell and using a CLI (command-line interface), pay attention to the characters and formatting. They’ll give you the context you need:

- `>` starts the 1st line and tells you which source file you’re in. After the filename, there is the current line number in parentheses. Next is the name of the function. In this example, since we’re not paused inside a function and at module level, we see `()`.
- `->` starts the 2nd line and is the current source line where Python is paused. This line hasn’t been executed yet. In this example, this is line `5` in `debug_1.py`, from the `>` line above.
- `(Pdb)` is pdb’s prompt. It’s waiting for a command.

Use the command `q` to quit debugging and exit.

## Print expressions

When using the print command `p`, you’re passing an expression to be evaluated by Python. If you pass a variable name, `pdb` prints its current value. 

```python
#!/usr/bin/env python3

import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    import pdb; pdb.set_trace()
    return head


filename = __file__
print(f'path = {get_path(filename)}')
```

If you run this from your shell, you should get the output:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_2.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_2.py(10)get_path()
-> return head
(Pdb) 
```

Where are we?

- `>`: We’re in the source file `debug_2.py` on line `10` in the function `get_path()`. This is the frame of reference the `p` command will use to resolve variable names, i.e. the current scope or context.
- `->`: Execution has paused at `return head`. This line hasn’t been executed yet. This is line `10` in `example2.py` in the function `get_path()`, from the `>` line above.

Let’s print some expressions to look at the current state of the application.

```python
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_2.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_2.py(10)get_path()
-> return head
(Pdb) p filename
'.\\debug_2.py'
(Pdb) p head, tail
('.', 'debug_2.py')
(Pdb) p 'filename: ' + filename
'filename: .\\debug_2.py'
(Pdb) p get_path
<function get_path at 0x000001C5C16C5160>
(Pdb) p getattr(get_path, '__doc__')
"Return file's path or empty string if no path."
(Pdb) p os.path.sys.path
['D:\\repositories\\python-e2e-book\\2-automate\\debugging', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\python38.zip', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\DLLs', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\lib', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\lib\\site-packages', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\lib\\site-packages\\win32', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\lib\\site-packages\\win32\\lib', 'D:\\applications\\winpython-3.8\\python-3.8.1.amd64\\lib\\site-packages\\Pythonwin']
(Pdb) p [os.path.split(p)[1] for p in os.path.sys.path]
['debugging', 'python38.zip', 'DLLs', 'lib', 'python-3.8.1.amd64', 'site-packages', 'win32', 'lib', 'Pythonwin']
(Pdb)
```

You can pass any valid Python expression to `p` for evaluation.

This is especially helpful when you are debugging and want to test an alternative implementation directly in the application at runtime.

## Stepping Through Code

There are two commands you can use to step through code when debugging:

| Command    | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| `n` (next) | Continue execution until the next line in the current function is reached or it returns. |
| `s` (step) | Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function). |

The difference between `n` (next) and `s` (step) is where pdb stops.

Use `n` (next) to continue execution until the next line and stay within the current function, i.e. not stop in a foreign function if one is called. Think of next as “staying local” or “step over”.

Use `s` (step) to execute the current line and stop in a foreign function if one is called. Think of step as “step into”. If execution is stopped in another function, `s` will print `--Call--`.

Both `n` and `s` will stop execution when the end of the current function is reached and print `--Return--` along with the return value at the end of the next line after `->`.

Lets look into debug_3.py

```python
#!/usr/bin/env python3

import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    return head


filename = __file__
import pdb; pdb.set_trace()
filename_path = get_path(filename)
print(f'path = {filename_path}')
```

If you run this from your shell and enter `n`, you should get the output:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) n
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(15)<module>()
-> print(f'path = {filename_path}')
(Pdb)
```

With `n` (next), we stopped on line `15`, the next line. We “stayed local” in `()` and “stepped over” the call to `get_path()`. The function is `()` since we’re currently at module level and not paused inside another function.

Let’s try `s`:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) s
--Call--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(6)get_path()
-> def get_path(filename):
(Pdb)
```

With `s` (step), we stopped on line `6` in the function `get_path()` since it was called on line `14`. Notice the line `--Call--` after the `s` command.

Below is an example of using both `s` and `n` to step through the code. I enter `s` initially because I want to “step into” the function `get_path()` and stop. Then I enter `n` once to “stay local” or “step over” any other function calls and just press Enter to repeat the `n` command until I get to the last source line.

```python
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) s
--Call--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(6)get_path()
-> def get_path(filename):
(Pdb) n
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(8)get_path()
-> head, tail = os.path.split(filename)
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(9)get_path()
-> return head
(Pdb)
--Return--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(9)get_path()->'.'
-> return head
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(15)<module>()
-> print(f'path = {filename_path}')
(Pdb)
path = .
--Return--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(15)<module>()->None
-> print(f'path = {filename_path}')
(Pdb)
PS D:\repositories\python-e2e-book\2-automate\debugging> 
```

Note the lines `--Call--` and `--Return--`. This is pdb letting you know why execution was stopped. `n` (next) and `s` (step) will stop before a function returns. That’s why you see the `--Return--` lines above.

### Listing Source Code

Don’t forget the command `ll` (longlist: list the whole source code for the current function or frame). It’s really helpful when you’re stepping through unfamiliar code or you just want to see the entire function for context.

Here’s an example:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) s
--Call--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(6)get_path()
-> def get_path(filename):
(Pdb) ll
  6  -> def get_path(filename):
  7         """Return file's path or empty string if no path."""
  8         head, tail = os.path.split(filename)
  9         return head
(Pdb)
```

To see a shorter snippet of code, use the command `l` (list). Without arguments, it will print 11 lines around the current line or continue the previous listing. Pass the argument `.` to always list 11 lines around the current line: `l .`

```python
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_3.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) l
  9         return head
 10
 11
 12     filename = __file__
 13     import pdb; pdb.set_trace()       
 14  -> filename_path = get_path(filename)
 15     print(f'path = {filename_path}')  
[EOF]
(Pdb) l
[EOF] 
(Pdb) l .
  9         return head
 10
 11
 12     filename = __file__
 13     import pdb; pdb.set_trace()
 14  -> filename_path = get_path(filename)
 15     print(f'path = {filename_path}')
[EOF]
(Pdb)
```

## Using Breakpoints

Breakpoints are very convenient and can save you a lot of time. Instead of stepping through dozens of lines you’re not interested in, simply create a breakpoint where you want to investigate. Optionally, you can also tell pdb to break only when a certain condition is true.

Use the command `b` (break) to set a breakpoint. You can specify a line number or a function name where execution is stopped.

The syntax for break is:

```
b(reak) [ ([filename:]lineno | function) [, condition] ]
```

If `filename:` is not specified before the line number `lineno`, then the current source file is used.

Note the optional 2nd argument to `b`: `condition`. This is very powerful. Imagine a situation where you wanted to break only if a certain condition existed. If you pass a Python expression as the 2nd argument, pdb will break when the expression evaluates to true. We’ll do this in an example below.

In this example, there’s a utility module `util.py`. Let’s set a breakpoint to stop execution in the function `get_path()`.

Here’s the source for the main script `debug_4.py`:

```python
#!/usr/bin/env python3

import util

filename = __file__
import pdb; pdb.set_trace()
filename_path = util.get_path(filename)
print(f'path = {filename_path}')
```

Here’s the source for the utility module `util.py`:

```
def get_path(filename):
    """Return file's path or empty string if no path."""
    import os
    head, tail = os.path.split(filename)
    return head
```

First, let’s set a breakpoint using the source filename and line number:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_4.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util:5
Breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:5
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\util.py(5)get_path()
-> return head
(Pdb) p filename, head, tail 
('.\\debug_4.py', '.', 'debug_4.py')
(Pdb)
```

The command `c` (continue) continues execution until a breakpoint is found.

Next, let’s set a breakpoint using the function name:

```
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_4.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util.get_path
Breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\util.py(3)get_path()
-> import os
(Pdb) p filename
'.\\debug_4.py'
```

Enter `b` with no arguments to see a list of all breakpoints:

```
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
        breakpoint already hit 1 time
(Pdb)
```

You can disable and re-enable breakpoints using the command `disable bpnumber` and `enable bpnumber`. `bpnumber` is the breakpoint number from the breakpoints list’s 1st column `Num`. Notice the `Enb` column’s value change:

```
(Pdb) disable 1
Disabled breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep no    at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
        breakpoint already hit 1 time
(Pdb) enable 1
Enabled breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
        breakpoint already hit 1 time
(Pdb)
```

To delete a breakpoint, use the command `cl` (clear):

```
cl(ear) filename:lineno
cl(ear) [bpnumber [bpnumber...]]
```

Now let’s use a Python expression to set a breakpoint. Imagine a situation where you wanted to break only if your troubled function received a certain input.

In this example scenario, the `get_path()` function is failing when it receives a relative path, i.e. the file’s path doesn’t start with `/`. I’ll create an expression that evaluates to true in this case and pass it to `b` as the 2nd argument:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_4.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util.get_path, not filename.startswith('/')
Breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:1
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\util.py(3)get_path()
-> import os
(Pdb) a
filename = '.\\debug_4.py'
(Pdb)
```

After you create the breakpoint above and enter `c` to continue execution, pdb stops when the expression evaluates to true. The command `a` (args) prints the argument list of the current function.

In the example above, when you’re setting the breakpoint with a function name rather than a line number, note that the expression should use only function arguments or global variables that are available at the time the function is entered. Otherwise, the breakpoint will stop execution in the function regardless of the expression’s value.

If you need to break using an expression with a variable name located inside a function, i.e. a variable name not in the function’s argument list, specify the line number:

```
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_4.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util:5, not head.startswith('/')
Breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\util.py:5
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\util.py(5)get_path()
-> return head
(Pdb) p head
'.'   
(Pdb) a
filename = '.\\debug_4.py'
(Pdb) 
```

You can also set a temporary breakpoint using the command `tbreak`. It’s removed automatically when it’s first hit. It uses the same arguments as `b`.

## Continuing Execution

So far, we’ve looked at stepping through code with `n` (next) and `s` (step) and using breakpoints with `b` (break) and `c` (continue).

There’s also a related command: `unt` (until).

Use `unt` to continue execution like `c`, but stop at the next line greater than the current line. Sometimes `unt` is more convenient and quicker to use and is exactly what you want. I’ll demonstrate this with an example below.

Let’s first look at the syntax and description for `unt`:

| Command | Syntax           | Description                                                  |
| ------- | ---------------- | ------------------------------------------------------------ |
| `unt`   | unt(il) [lineno] | Without `lineno`, continue execution until the line with a number greater than the current one is reached. With `lineno`, continue execution until a line with a number greater or equal to that is reached. In both cases, also stop when the current frame returns. |

Depending on whether or not you pass the line number argument `lineno`, `unt` can behave in two ways:

- Without `lineno`, continue execution until the line with a number greater than the current one is reached. This is similar to `n` (next). It’s an alternate way to execute and “step over” code. The difference between `n` and `unt` is that `unt` stops only when a line with a number greater than the current one is reached. `n` will stop at the next logically executed line.
- With `lineno`, continue execution until a line with a number greater or equal to that is reached. This is like `c` (continue) with a line number argument.

In both cases, `unt` stops when the current frame (function) returns, just like `n` (next) and `s` (step).

The primary behavior to note with `unt` is that it will stop when a line number **greater or equal** to the current or specified line is reached.

Use `unt` when you want to continue execution and stop farther down in the current source file. You can treat it like a hybrid of `n` (next) and `b` (break), depending on whether you pass a line number argument or not.

In the example below, there is a function with a loop. Here, you want to continue execution of the code and stop after the loop, without stepping through each iteration of the loop or setting a breakpoint:

Here’s the example source for `debug_5.py`:

```python
#!/usr/bin/env python3

import os


def get_path(fname):
    """Return file's path or empty string if no path."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(fname)
    for char in tail:
        pass  # Check filename char
    return head


filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')
```

And the console output using `unt`:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_5.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(9)get_path()
-> head, tail = os.path.split(fname)
(Pdb) ll
  6     def get_path(fname):
  7         """Return file's path or empty string if no path."""
  8         import pdb; pdb.set_trace()
  9  ->     head, tail = os.path.split(fname)
 10         for char in tail:
 11             pass  # Check filename char
 12         return head
(Pdb) unt
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(10)get_path()
-> for char in tail:
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(12)get_path()
-> return head
(Pdb)
--Return--
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(12)get_path()->'.'      
-> return head
(Pdb) p char, tail
('y', 'debug_5.py')
(Pdb)
```

The `ll` command was used first to print the function’s source, followed by `unt`. pdb remembers the last command entered, so I just pressed Enter to repeat the `unt` command. This continued execution through the code until a source line greater than the current line was reached.

Note in the console output above that pdb stopped only once on lines `10` and `11`. Since `unt` was used, execution was stopped only in the 1st iteration of the loop. However, each iteration of the loop was executed. This can be verified in the last line of output. The `char` variable’s value `'y'` is equal to the last character in `tail`’s value `'debug_5.py'`.

## Displaying Expressions

Similar to printing expressions with `p` and `pp`, you can use the command `display [expression]` to tell pdb to automatically display the value of an expression, if it changed, when execution stops. Use the command `undisplay [expression]` to clear a display expression.

Here’s the syntax and description for both commands:

| Command     | Syntax                 | Description                                                  |
| ----------- | ---------------------- | ------------------------------------------------------------ |
| `display`   | display [expression]   | Display the value of `expression` if it changed, each time execution stops in the current frame. Without `expression`, list all display expressions for the current frame. |
| `undisplay` | undisplay [expression] | Do not display `expression` any more in the current frame. Without `expression`, clear all display expressions for the current frame. |

Below is an example, `debug_5.py`, demonstrating its use with a loop:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_5.py
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(9)get_path()
-> head, tail = os.path.split(fname)
(Pdb) ll
  6     def get_path(fname):
  7         """Return file's path or empty string if no path."""
  8         import pdb; pdb.set_trace()
  9  ->     head, tail = os.path.split(fname)
 10         for char in tail:
 11             pass  # Check filename char
 12         return head
(Pdb) b 11
Breakpoint 1 at d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py:11
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
(Pdb) display char
display char: 'd'
(Pdb) c
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
display char: 'e'  [old: 'd']
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
display char: 'b'  [old: 'e']
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
display char: 'u'  [old: 'b']
(Pdb)
> d:\repositories\python-e2e-book\2-automate\debugging\debug_5.py(11)get_path()
-> pass  # Check filename char
display char: 'g'  [old: 'u']
(Pdb)
```

In the output above, pdb automatically displayed the value of the `char` variable because each time the breakpoint was hit its value had changed. Sometimes this is helpful and exactly what you want, but there’s another way to use `display`.

You can enter `display` multiple times to build a watch list of expressions. This can be easier to use than `p`. After adding all of the expressions you’re interested in, simply enter `display` to see the current values:

```powershell
(Pdb) display
Currently displaying:
char: 'g'
(Pdb) display fname
display fname: '.\\debug_5.py'
(Pdb) display fname
display fname: '.\\debug_5.py'
(Pdb) display head
display head: '.'
(Pdb) display tail
display tail: 'debug_5.py'
(Pdb)
```

## Python Caller ID

In this last section, we’ll build upon what we’ve learned so far and finish with a nice payoff. I use the name “caller ID” in reference to the phone system’s caller identification feature. That is exactly what this example demonstrates, except it’s applied to Python.

Here’s the source for the main script `debug_6.py`:

```python
#!/usr/bin/env python3

import fileutil


def get_file_info(full_fname):
    file_path = fileutil.get_path(full_fname)
    return file_path


filename = __file__
filename_path = get_file_info(filename)
print(f'path = {filename_path}')
```

Here’s the utility module `fileutil.py`:

```python
def get_path(fname):
    """Return file's path or empty string if no path."""
    import os
    import pdb; pdb.set_trace()
    head, tail = os.path.split(fname)
    return head
```

In this scenario, imagine there’s a large code base with a function in a utility module, `get_path()`, that’s being called with invalid input. However, it’s being called from many places in different packages.

**How do you find who the caller is?**

Use the command `w` (where) to print a stack trace, with the most recent frame at the bottom:

```powershell
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_6.py
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) w
  d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(12)<module>()
-> filename_path = get_file_info(filename)
  d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(7)get_file_info()       
-> file_path = fileutil.get_path(full_fname)
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb)
```

Don’t worry if this looks confusing or if you’re not sure what a stack trace or frame is. I’ll explain those terms below. It’s not as difficult as it might sound.

Since the most recent frame is at the bottom, start there and read from the bottom up. Look at the lines that start with `->`, but skip the 1st instance since that’s where `pdb.set_trace()` was used to enter pdb in the function `get_path()`. In this example, the source line that called the function `get_path()` is:

```
-> file_path = fileutil.get_path(full_fname)
```

The line above each `->` contains the filename, line number (in parentheses), and function name the source line is in. So the caller is:

```
  d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(7)get_file_info()       
-> file_path = fileutil.get_path(full_fname)
```

That’s no surprise in this small example for demonstration purposes, but imagine a large application where you’ve set a breakpoint with a condition to identify where a bad input value is originating.

Now we know how to find the caller.

**But what about this stack trace and frame stuff?**

A stack trace is just a list of all the frames that Python has created to keep track of function calls. A frame is a data structure Python creates when a function is called and deletes when it returns. The stack is simply an ordered list of frames or function calls at any point in time. The (function call) stack grows and shrinks throughout the life of an application as functions are called and then return.

When printed, this ordered list of frames, the stack, is called a stack trace. You can see it at any time by entering the command `w`, as we did above to find the caller.

> See this [call stack article on Wikipedia](https://en.wikipedia.org/wiki/Call_stack) for details.

To understand better and get more out of pdb, let’s look more closely at the help for `w`:

```
(Pdb) h w
w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands. 'bt' is an alias for this command.
```

**What does pdb mean by “current frame”?**

Think of the current frame as the current function where pdb has stopped execution. In other words, the current frame is where your application is currently paused and is used as the “frame” of reference for pdb commands like `p` (print).

`p` and other commands will use the current frame for context when needed. In the case of `p`, the current frame will be used for looking up and printing variable references.

When pdb prints a stack trace, an arrow `>` indicates the current frame.

**How is this useful?**

You can use the two commands `u` (up) and `d` (down) to change the current frame. Combined with `p`, this allows you to inspect variables and state in your application at any point along the call stack in any frame.

Here’s the syntax and description for both commands:

| Command | Syntax         | Description                                                  |
| ------- | -------------- | ------------------------------------------------------------ |
| `u`     | u(p) [count]   | Move the current frame `count` (default one) levels up in the stack trace (to an older frame). |
| `d`     | d(own) [count] | Move the current frame `count` (default one) levels down in the stack trace (to a newer frame). |

Let’s look at an example using the `u` and `d` commands. In this scenario, we want to inspect the variable `full_fname` that’s local to the function `get_file_info()` in `debug_6.py`. In order to do this, we have to change the current frame up one level using the command `u`:

```python
PS D:\repositories\python-e2e-book\2-automate\debugging> python .\debug_6.py
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) w
  d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(12)<module>()
-> filename_path = get_file_info(filename)
  d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(7)get_file_info()       
-> file_path = fileutil.get_path(full_fname)
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) h w
w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the  
        context of most commands.  'bt' is an alias for this command. 
(Pdb) u
> d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(7)get_file_info()
-> file_path = fileutil.get_path(full_fname)
(Pdb) p full_fname
'.\\debug_6.py'
(Pdb) d
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) p fname
'.\\debug_6.py'
(Pdb)
```

The call to `pdb.set_trace()` is in `fileutil.py` in the function `get_path()`, so the current frame is initially set there. You can see it in the 1st line of output above:

```python
> d:\repositories\python-e2e-book\2-automate\debugging\fileutil.py(5)get_path()
```

To access and print the local variable `full_fname` in the function `get_file_info()` in `example5.py`, the command `u` was used to move up one level:

```
(Pdb) u
> d:\repositories\python-e2e-book\2-automate\debugging\debug_6.py(7)get_file_info()
-> file_path = fileutil.get_path(full_fname)
```

Note in the output of `u` above that pdb printed the arrow `>` at the beginning of the 1st line. This is pdb letting you know the frame was changed and this source location is now the current frame. The variable `full_fname` is accessible now. Also, it’s important to realize the source line starting with `->` on the 2nd line has been executed. Since the frame was moved up the stack, `fileutil.get_path()` has been called. Using `u`, we moved up the stack (in a sense, back in time) to the function `debug_6.get_file_info()` where `fileutil.get_path()` was called.

Continuing with the example, after `full_fname` was printed, the current frame was moved to its original location using `d`, and the local variable `fname` in `get_path()` was printed.

If we wanted to, we could have moved multiple frames at once by passing the `count` argument to `u` or `d`. For example, we could have moved to module level in `debug_6.py` by entering `u 2`:

```
$ ./example5.py 
> /code/fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) u 2
> /code/example5.py(12)<module>()
-> filename_path = get_file_info(filename)
(Pdb) p filename
'./example5.py'
(Pdb) 
```

It’s easy to forget where you are when you’re debugging and thinking of many different things. Just remember you can always use the aptly named command `w` (where) to see where execution is paused and what the current frame is.

## Essential pdb Commands

Once you’ve spent a little time with pdb, you’ll realize a little knowledge goes a long way. Help is always available with the `h` command.

Just enter `h` or `help ` to get a list of all commands or help for a specific command or topic.

For quick reference, here’s a list of essential commands:

| Command | Description                                                  |
| ------- | ------------------------------------------------------------ |
| `p`     | Print the value of an expression.                            |
| `pp`    | Pretty-print the value of an expression.                     |
| `n`     | Continue execution until the next line in the current function is reached or it returns. |
| `s`     | Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function). |
| `c`     | Continue execution and only stop when a breakpoint is encountered. |
| `unt`   | Continue execution until the line with a number greater than the current one is reached. With a line number argument, continue execution until a line with a number greater or equal to that is reached. |
| `l`     | List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing. |
| `ll`    | List the whole source code for the current function or frame. |
| `b`     | With no arguments, list all breaks. With a line number argument, set a breakpoint at this line in the current file. |
| `w`     | Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands. |
| `u`     | Move the current frame count (default one) levels up in the stack trace (to an older frame). |
| `d`     | Move the current frame count (default one) levels down in the stack trace (to a newer frame). |
| `h`     | See a list of available commands.                            |
| `h `    | Show help for a command or topic.                            |
| `h pdb` | Show the full pdb documentation.                             |
| `q`     | Quit the debugger and exit.                                  |

# VS Code Debugging

The Python extension supports debugging of a number of types of Python applications. 

## Initialize configurations

A configuration drives VS Code's behavior during a debugging session. Configurations are defined in a `launch.json` file that's stored in a `.vscode` folder in your workspace.

> **Note** In order to change debugging configuration, your code must be stored in a folder.

### Example Configuration

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "args": ["HelloWorld"],
            "console": "integratedTerminal"
        }
    ]
}
```

## Set configuration options

When you first create `launch.json`, there are two standard configurations that run the active file in the editor in either the integrated terminal (inside VS Code) or the external terminal (outside of VS Code):

```json
{
    "name": "Python: Current File (Integrated Terminal)",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal"
},
{
    "name": "Python: Current File (External Terminal)",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "externalTerminal"
}
```

The specific settings are described in the following sections. You can also add other settings, such as `args`, that aren't included in the standard configurations.

> **Tip**: It's often helpful in a project to create a configuration that runs a specific startup file. For example, if you want to always launch `startup.py` with the arguments `--port 1593` when you start the debugger, create a configuration entry as follows:
>
> ```json
> {
>     "name": "Python: startup.py",
>     "type": "python",
>     "request": "launch",
>     "program": "${workspaceFolder}/startup.py",
>     "args" : ["--port", "1593"]
> },
> ```

### `name`

Provides the name for the debug configuration that appears in the VS Code drop-down list.

### `type`

Identifies the type of debugger to use; leave this set to `python` for Python code.

### `request`

Specifies the mode in which to start debugging:

- `launch`: start the debugger on the file specified in `program`
- `attach`: attach the debugger to an already running process.

### `program`

Provides the fully qualified path to the python program's entry module (startup file). The value `${file}`, often used in default configurations, uses the currently active file in the editor. By specifying a specific startup file, you can always be sure of launching your program with the same entry point regardless of which files are open. For example:

```
"program": "/Users/Me/Projects/PokemonGo-Bot/pokemongo_bot/event_handlers/__init__.py",
```

You can also rely on a relative path from the workspace root. For example, if the root is `/Users/Me/Projects/PokemonGo-Bot` then you can use the following:

```
"program": "${workspaceFolder}/pokemongo_bot/event_handlers/__init__.py",
```

### `pythonPath`

Points to the Python interpreter to be used for debugging, which can be a folder containing a Python interpreter. The value can use variables like `${workspaceFolder}` and `${workspaceFolder}/.venv`.

If not specified, this setting defaults to the interpreter identified in the `python.pythonPath` setting, which is equivalent to using the value `${config:python.pythonPath}`. To use a different interpreter, specify its path instead in the `pythonPath` property of a debug configuration.

You can specify platform-specific paths by placing `pythonPath` within a parent object named `osx`, `windows`, or `linux`. For example, the configuration for PySpark uses the following values:

```
"osx": {
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit\""
},
"windows": {
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit.cmd\""
},
"linux": {
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit\""
},
```

Alternately, you can use a custom environment variable that's defined on each platform to contain the full path to the Python interpreter to use, so that no additional folder paths are needed.

### `args`

Specifies arguments to pass to the Python program. Each element of the argument string that's separated by a space should be contained within quotes, for example:

```
"args": ["--quiet", "--norepeat", "--port", "1593"],
```

### `stopOnEntry`

When set to `true`, breaks the debugger at the first line of the program being debugged. If omitted (the default) or set to `false`, the debugger runs the program to the first breakpoint.

### `console`

Specifies how program output is displayed.

| Value                            | Where output is displayed   |
| :------------------------------- | :-------------------------- |
| `"internalConsole"`              | VS Code debug console       |
| `"integratedTerminal"` (default) | VS Code Integrated Terminal |
| `"externalTerminal"`             | Separate console window     |

### `cwd`

Specifies the current working directory for the debugger, which is the base folder for any relative paths used in code. If omitted, defaults to `${workspaceFolder}` (the folder open in VS Code).

As an example, say `${workspaceFolder}` contains a `py_code` folder containing `app.py`, and a `data` folder containing `salaries.csv`. If you start the debugger on `py_code/app.py`, then the relative paths to the data file vary depending on the value of `cwd`:

| cwd                             | Relative path to data file |
| :------------------------------ | :------------------------- |
| Omitted or `${workspaceFolder}` | `data/salaries.csv`        |
| `${workspaceFolder}/py_code`    | `../data/salaries.csv`     |
| `${workspaceFolder}/data`       | `salaries.csv`             |

### `redirectOutput`

When omitted or set to `true` (the default), causes the debugger to print all output from the program into the VS Code debug output window. If set to `false`, program output is not displayed in the debugger output window.

This option is typically disabled when using `"console": "integratedTerminal"` or `"console": "externalTerminal"` because there's no need to duplicate the output in the debug console.

### `justMyCode`

When omitted or set to `true` (the default), restricts debugging to user-written code only. Set to `false` to also enable debugging of standard library functions.

### `django`

When set to `true`, activates debugging features specific to the Django web framework.

### `sudo`

When set to `true` and used with `"console": "externalTerminal"`, allows for debugging apps that require elevation. Using an external console is necessary to capture the password.

### `pyramid`

When set to `true`, ensures that a Pyramid app is launched with [the necessary `pserve` command](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/startup.html?highlight=pserve).

### `env`

Sets optional environment variables for the debugger process beyond system environment variables, which the debugger always inherits. The values for these variables must be entered as strings.

### `envFile`

Optional path to a file that contains environment variable definitions. See [Configuring Python environments - environment variable definitions file](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file).

### `gevent`

If set to `true`, enables debugging of [gevent monkey-patched code](http://www.gevent.org/intro.html).

## Invoking a breakpoint in code

In your Python code, you can call `breakpoint()` at any point where you want to pause the debugger during a debugging session.

## Breakpoint validation

The Python extension automatically detects breakpoints that are set on non-executable lines, such as `pass` statements or the middle of a multiline statement. In such cases, running the debugger moves the breakpoint to nearest valid line to ensure that code execution stops at that point.

## Attach to a local script

In some scenarios, you need to debug a Python script that's invoked locally by another process. For example, you may be debugging a web server that runs different Python scripts for specific processing jobs. In such cases, you need to attach the VS Code debugger to the script once it's been launched:

1. Run VS Code, open the folder or workspace containing the script, and create a `launch.json` for that workspace if one doesn't exist already.

2. In the script code, add the following and save the file:

   ```
   import ptvsd
   
   # 5678 is the default attach port in the VS Code debug configurations
   print("Waiting for debugger attach")
   ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
   ptvsd.wait_for_attach()
   breakpoint()
   ```

3. Open a terminal using **Terminal: Create New Integrated Terminal**, which activates the script's selected environment.

4. In the terminal, install the ptvsd package with `python -m pip install --upgrade ptvsd`.

5. In the terminal, start Python with the script, for example, `python3 myscript.py`. You should see the "Waiting for debugger attach" message that's included in the code, and the script halts at the `ptvsd.wait_for_attach()` call.

6. Switch to the Debug view, select **Python: Attach** from the debugger drop-down list, and start the debugger.

7. The debugger should stop on the `breakpoint()` call, from which point you can use the debugger normally. You can, of course, set other breakpoints in the script code instead of using `breakpoint()`.