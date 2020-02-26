# Input and Output

<img src="./file-joke.png" alt="File-Joke" style="zoom:80%;" />

There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. 

## Output Formatting

So far we’ve encountered two ways of writing values: *expression statements* and the `print()` function. Often you’ll want more control over the formatting of your output than simply printing space-separated values. 

There are several ways to format output.

### Formatted String Literals (f-strings)

Fromatted String Literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with `f` or `F` and writing expressions as `{expression}`.

To use formatted string literals, begin a string with `f` or `F` before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between `{` and `}` characters that can refer to variables or literal values.

```python
first_name = 'Rashmi'
last_name = 'Maharjan'
f'My name is {first_name} {last_name}'

# Output: My name is Rashmi Maharjan
```

The following example rounds pi to three places after the decimal:

```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# Output: The value of pi is approximately 3.142.
```

Passing an integer after the `':'` will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

```python
table = {'Bikash': 1212, 'Ram': 4112, 'Rabin': 7890}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    
# Output:
# Bikash     ==>       1212
# Ram        ==>       4112
# Rabin      ==>       7890
```

### String `format()` method

Basic usage of the `str.format()` method looks like this:

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# Output: We are the knights who say "Ni!"
```

A number in the brackets can be used to refer to the position of the object passed into the `str.format()` method.

```python
print('{0} {1}'.format('Hello', 'Pau'))
# Output: Hello Pau
print('{1} {0}'.format('Pau', 'Tori'))
# Output: Tori Pau
```

A keyword argument can also be used

```python
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# Output: This spam is absolutely horrible.
```

You can also use dict:

```python
table = {'Ram': 4127, 'Rashmi': 4098, 'Akshyata': 8637678}
print('Rashmi: {0[Rashmi]:d}; Ram: {0[Ram]:d}; '
      'Akshyata: {0[Akshyata]:d}'.format(table))

# Output: Rashmi: 4098; Ram: 4127; Akshyata: 8637678
```

An example of aligned columns:

```python
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# Output:
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000
```

### Old School string formatting

The `%` operator can also be used for string formatting.

```python
import math
print('The value of pi is approximately %5.3f.' % math.pi)

# Output: The value of pi is approximately 3.142.
```

Another example:

```python
print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})

# Output: Python has 002 quote types.
```

## Reading and Writing Files

### File: An Overview

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

- **Header**: metadata about the contents of the file (file name, size, type, and so on)
- **Data**: contents of the file as written by the creator or editor
- **End of file (EOF)**: special character that indicates the end of the file

<img src="./file-parts.png" alt="File Parts" style="zoom:80%;" />

### Paths

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

- **Folder Path**: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
- **File Name**: the actual name of the file
- **Extension**: the end of the file path pre-pended with a period (.) used to indicate the file type

Consider the file structure of this project:

```
│   .gitignore
│   debug.log
│   LICENSE
│   python-e2e-book.code-workspace
│   README.md
│
├───.ipynb_checkpoints
├───.vscode
│       settings.json
│
├───1-know-your-language
│   │   apply-primer.jpg
│   │   before-we-begin.md
│   │   classes-and-objects.ipynb
│   │   classes-and-objects.md
│   │   Client-server.jpg
│   │   data-structures.ipynb
│   │   data-structures.md
│   │   errors-and-exception.ipynb
│   │   errors-and-exception.md
│   │   flow-control.md
│   │   functions.ipynb
│   │   functions.md
│   │   looping-techniques.ipynb
│   │   looping-techniques.md
│   │   modules.md
│   │   package-management.ipynb
│   │   package-management.md
│   │   python-primer.ipynb
│   │   python-primer.md
│   │   python-qna.jpg
│   │   q-&-a.md
│   │   virtual-environment.ipynb
│   │   virtual-environment.md
│
├───2-automate
│   │   file-joke.png
│   │   file-parts.png
│   │   input-output.md
│   │   README.md
│   │   regular-expressions.md
│   │   Untitled.ipynb
│   │
│   ├───.ipynb_checkpoints
│   │       spreadsheet-whisperer-checkpoint.ipynb
│   │       Untitled-checkpoint.ipynb
│   │
│   └───regular-expressions
│           password_strength.py
│
├───3-web-and-beyond
│       README.md
│
├───4-rest-time
│       README.md
│
├───5-what-now
│       README.md
│
└───6-Miscellaneous
        container-vm.png
        docker-architecture.png
        docker-engine.png
        docker.md
        README.md
```

Suppose, we want to access `password_strength.py` from root folder. The path can be broken into:

- **Folder Path**: `2-automate/regular-expressions`
- **File Name**: `password_strength.py`
- **Extension**: `.py`

So, full path is `2-automate/regular-expressions/password_strength.py `

Let's say, we want to access `README.md` in root folder from `2-automate/regular-expressions`. In that case, we can use special double-dot `..` to move one director up. So we'll have to use path `../../README.md` 

### Line Endings

One problem often encountered when working with file data is the representation of a new line or line ending. 

American Standards Association (ASA) states that line endings should use the sequence of the Carriage Return (`CR` or `\r`) *and* the Line Feed (`LF` or `\n`) characters (`CR+LF` or `\r\n`). 

The International Organization  (ISO) standard however allowed for either the `CR+LF` characters or just the `LF` character.

Note: **Windows** uses the `CR+LF` characters to indicate a new line, while **Unix** and the newer **Mac** versions use just the `LF` character. This can cause some complications when you’re processing files on an operating system that is different than the file’s source.

### Character Encoding

Another common problem that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. 

The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

Note: ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values.

It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character. 

For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.

### Opening and Closing a File

To open a file, we invoke `open()` built-in function. `open()` has a single required argument that is path to the file and returns the file object.

```python
file = open('contacts.txt')
```

you should call `f.close()` to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times.

```python
file.close()
```

When manipulating a file, we've to ensure the file have been closes, even when an error is encountered.

```python
file = open('contacts.txt')

try:
    # Do something with file
finally:
    file.close()
```

#### Alternative Method

An alternative way of closing a file would be to use `with` statement.

```python
with open('contacts.txt') as file:
    # Do something with wile
```

The `with` statement automatically takes care of closing the file once it leaves the `with` block, even in cases of error. 

#### The file mode

You’ll also want to use the second positional argument, `mode`. This argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is `'r'`, which represents opening the file in read-only mode as a text file:

```python
with open('contacts.txt', 'r') as file:
    # Further file processing goes here
```

Most common file modes are:

| Character        | Meaning                                                   |
| ---------------- | --------------------------------------------------------- |
| `'r'`            | Open for reading (default)                                |
| `'w'`            | Open for writing, truncating (overwriting) the file first |
| `'rb'` or `'wb'` | Open in binary mode (read/write using byte data)          |

#### File Object

A file object is:

> An object exposing a file-oriented API (with methods such as `read()` or `write()`) to an underlying resource.

There are three different categories of file objects:

- Text files
- Buffered binary files
- Raw binary files

##### Text files

A text file is the most common file that you’ll encounter. Here are some examples of how these files are opened:

```python
open('contacts.txt')

open('contacts.txt', 'r')

open('contacts.txt', 'w')
```

##### Buffered binary files

A buffered binary file type is used for reading and writing binary files. Here are some examples of how these files are opened:

```python
open('contacts.txt', 'rb')

open('contacts.txt', 'wb')
```

#####  Raw binary files

A raw file generally used as a low-level building-block for binary and text streams.

It is generally not used.

```python
open("contacts.jpg", "rb", buffering=0)
```

### Reading and Writing files

Once you’ve opened up a file, you’ll want to read or write to the file. First off, let’s cover reading a file.

| Method               | What It Does                                                 |
| -------------------- | ------------------------------------------------------------ |
| `.read(size=-1)`     | This reads from the file based on the number of `size` bytes. If no argument is passed or `None` or `-1` is passed, then the entire file is read. |
| `.readline(size=-1)` | This reads at most `size` number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or `None` or `-1` is passed, then the entire line (or rest of the line) is read. |
| `.readlines()`       | This reads the remaining lines from the file object and returns them as a list. |

#### `.read()` Method

```python
with open('contacts.txt', 'r') as reader:
    # Read & print the entire file
    print(reader.read())
```

#### `.readline()` Method

Here’s an example of how to read 5 bytes of a line each time using the Python `.readline()` method:

```python
with open('contacts.txt', 'r') as reader:
    # Read & print the first 5 characters of the line 5 times
    print(reader.readline(5))
    # Notice that line is greater than the 5 chars and continues
    # down the line, reading 5 chars each time until the end of the
    # line and then "wraps" around
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
```

#### `.readlines()` Method

Here’s an example of how to read the entire file as a list using the Python `.readlines()` method:

```python
f = open('contacts.txt')
f.readlines()  # Returns a list object or use list(f)
```

#### Iterating over each line

##### Using `readline()`

```python
with open('contacts.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
```

##### Using `readlines()`

```python
with open('contacts.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')
```

##### Using file object

```python
with open('contacts.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')
```

Now let’s dive into writing files. As with reading files, file objects have multiple methods that are useful for writing to a file:

| Method             | What It Does                                                 |
| ------------------ | ------------------------------------------------------------ |
| `.write(string)`   | This writes the string to the file.                          |
| `.writelines(seq)` | This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s). |

#### `.write()` Method

```python
with open('contacts.txt', 'w') as writer:
    contacts = ['Ram Kasula', 'Bikram Manandhar', 'Mooool Shreya']
    for contact in contacts:
        writer.write(contacts)
```

#### `.writelines(seq)` Method

```python
with open('dog_breeds_reversed.txt', 'w') as writer:
    contacts = ['Ram Kasula', 'Bikram Manandhar', 'Mooool Shreya']
    writer.writelines(contacts)
```

