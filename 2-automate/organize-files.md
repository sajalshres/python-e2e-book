# Working with Files and Directories

Python has several built-in modules and functions for handling files and directories each with similar and specific use cases. Some of them are:

- `os`
- `os.path`
- `shutil`
- `pathlib`

## Before We Begin

All the examples are based on the root directory of this repository:

```bash
D:\REPOSITORIES\PYTHON-E2E-BOOK
│   .gitignore
│   debug.log
│   LICENSE
│   python-e2e-book.code-workspace
│   README.md
│
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
│   │   flow-control.ipynb
│   │   flow-control.md
│   │   functions.ipynb
│   │   functions.md
│   │   looping-techniques.ipynb
│   │   looping-techniques.md
│   │   modules.md
│   │   Monty-Python-Flying-Circus.jpg
│   │   package-management.ipynb
│   │   package-management.md
│   │   python-primer.ipynb
│   │   python-primer.md
│   │   python-qna.jpg
│   │   q-&-a.md
│   │   README.md
│   │   shell.jpg
│   │   virtual-environment.ipynb
│   │   virtual-environment.md
│
├───2-automate ----------------> WE ARE HERE
│   │   file-joke.png
│   │   file-parts.png
│   │   input-output.md
│   │   organize-files.md
│   │   README.md
│   │   regular-expressions.md
│   │   Untitled.ipynb
│   │
│   ├───input-output
│   │       contacts_manager.py
│   │       database.txt
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

## Listing Directories

### Get current working directory

```python
import os

os.getcwd()

# Output: 'D:\\repositories\\python-e2e-book\\2-automate'
```

### List directory

`os.listdir()` is the method to use to get a directory listing:

```python
import os

os.listdir('input-output/')

# Output: ['contacts_manager.py', 'database.txt']
```

`os.listdir()` returns a Python list containing the names of the files and subdirectories in the directory given by the path argument:

#### Iterate over directory

Printing out the output of a call to `os.listdir()` using a loop helps clean things up:

```python
for item in os.listdir('input-output/'):
    print(item)

'''
Output:
contacts_manager.py
database.txt
'''
```

#### Alternative modern Pythonic approach to listing directory

`os.scandir()` was introduced in Python 3.5. `os.scandir()` returns an iterator as opposed to a list when called:

```python
os.scandir('input-output/')

# Output: <nt.ScandirIterator at 0x13fc6ac63d0>
```

#### Loop over `scandir()`

The `ScandirIterator` points to all the entries in the current directory. You can loop over the contents of the iterator and print out the filenames:

```python
with os.scandir('input-output/') as items:
    for item in items:
        print(f'{item.name} with path {item.path}')
        
'''
Output:
contacts_manager.py with path input-output/contacts_manager.py
database.txt with path input-output/database.txt
'''
```

Here, `os.scandir()` is used in conjunction with the `with` statement because it supports the context manager protocol. Using a context manager closes the iterator and frees up acquired resources automatically after the iterator has been exhausted. 

#### Common listing functions

| Function                 | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `os.listdir()`           | Returns a list of all files and folders in a directory       |
| `os.scandir()`           | Returns an iterator of all the objects in a directory including file attribute information |
| `pathlib.Path.iterdir()` | Returns an iterator of all the objects in a directory including file attribute information |

## List all files in a directory

### Using `os.listdir()`

```python
import os

# List all files in a directory using os.listdir
basepath = '../'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

'''      
.gitignore
debug.log
LICENSE
python-e2e-book.code-workspace
README.md'''
```

Here, the call to `os.listdir()` returns a list of everything in the specified path, and then that list is filtered by `os.path.isfile()` to only print out files and not directories. 

### Using `os.scandir()`

```python
import os

# List all files in a directory using scandir()
basepath = '../'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
            
'''      
.gitignore
debug.log
LICENSE
python-e2e-book.code-workspace
README.md'''
```

Using `os.scandir()` has the advantage of looking cleaner and being easier to understand than using `os.listdir()`, even though it is one line of code longer. Calling `entry.is_file()` on each item in the `ScandirIterator` returns `True` if the object is a file. 

### Using `pathlib.Path()` [*Return Later*]

```python
from pathlib import Path

basepath = Path('../')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
        
'''      
.gitignore
debug.log
LICENSE
python-e2e-book.code-workspace
README.md'''
```

The call `.is_file()` on each entry yielded by `.iterdir()`

## List subdirectories

### Using `os.listdir()`

```python
import os

# List all subdirectories using os.listdir
basepath = '../'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)

'''
.git
.ipynb_checkpoints
.vscode
1-know-your-language
2-automate
3-web-and-beyond
4-rest-time
5-what-now
6-Miscellaneous
'''
```

### Using `os.scandir()`

```python
import os

# List all subdirectories using scandir()
basepath = '../'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

'''
.git
.ipynb_checkpoints
.vscode
1-know-your-language
2-automate
3-web-and-beyond
4-rest-time
5-what-now
6-Miscellaneous
'''
```

### Using `pathlib.Path()` [*Return Later*]

```python
from pathlib import Path

# List all subdirectory using pathlib
basepath = Path('../')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)

'''
.git
.ipynb_checkpoints
.vscode
1-know-your-language
2-automate
3-web-and-beyond
4-rest-time
5-what-now
6-Miscellaneous
'''
```

## Get file metadata/attributes

Python makes retrieving file attributes such as file size and modified times easy. This is done through `os.stat()`, `os.scandir()`, or `pathlib.Path()`.

```python
import os

with os.scandir('../') as dir_contents:
    print('{0:35s}{1:<10s}{2:<10s}{3:<8s}{4:<20s}'.format(
        'Name', 'UserID', 'GroupID', 'Mode', 'Modified'))
    for entry in dir_contents:
        info = entry.stat()
        print(f'{entry.name:35s}{info.st_uid:<10d}\
            {info.st_gid:<10d}{info.st_mode:<8d}{info.st_mtime:<20f}')

'''
Name                               UserID    GroupID   Mode    Modified            
.git                               0         0         16895   1582698009.583250   
.gitignore                         0         0         33206   1582606190.601146   
.ipynb_checkpoints                 0         0         16895   1580138522.330589   
.vscode                            0         0         16895   1582565352.059732   
1-know-your-language               0         0         16895   1582688743.341213   
2-automate                         0         0         16895   1582738816.884005   
3-web-and-beyond                   0         0         16895   1580228642.191034   
4-rest-time                        0         0         16895   1578136533.607883   
5-what-now                         0         0         16895   1578136542.003414   
6-Miscellaneous                    0         0         16895   1580232203.811131   
debug.log                          0         0         33206   1579507956.837189   
LICENSE                            0         0         33206   1578136002.648941   
python-e2e-book.code-workspace     0         0         33206   1582605928.260975   
README.md                          0         0         33206   1582632397.891731  
'''
```

After date conversion:

```python
from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir('../')
    print('{0:35s}{1:<10s}{2:<10s}{3:<8s}{4:<20s}'.format(
        'Name', 'UserID', 'GroupID', 'Mode', 'Modified'))
    for entry in dir_entries:
        info = entry.stat()
        print(f'{entry.name:<35s}{info.st_uid:<10d}\
{info.st_gid:<10d}{info.st_mode:<8d}{convert_date(info.st_mtime):<20}')
            
get_files()

'''
Name                               UserID    GroupID   Mode    Modified            
.git                               0         0         16895   26 Feb 2020         
.gitignore                         0         0         33206   25 Feb 2020         
.ipynb_checkpoints                 0         0         16895   27 Jan 2020         
.vscode                            0         0         16895   24 Feb 2020         
1-know-your-language               0         0         16895   26 Feb 2020         
2-automate                         0         0         16895   26 Feb 2020         
3-web-and-beyond                   0         0         16895   28 Jan 2020         
4-rest-time                        0         0         16895   04 Jan 2020         
5-what-now                         0         0         16895   04 Jan 2020         
6-Miscellaneous                    0         0         16895   28 Jan 2020         
debug.log                          0         0         33206   20 Jan 2020         
LICENSE                            0         0         33206   04 Jan 2020         
python-e2e-book.code-workspace     0         0         33206   25 Feb 2020         
README.md                          0         0         33206   25 Feb 2020 
'''
```

`convert_date()` makes use of `.strftime()` to convert the time in seconds into a string.

The arguments passed to `.strftime()` are the following:

- **`%d`:** the day of the month
- **`%b`:** the month, in abbreviated form
- **`%Y`:** the year

## Creating Directories

Sooner or later, the programs you write will have to create directories in order to store data in them.

| Function               | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `os.mkdir()`           | Creates a single subdirectory                                |
| `pathlib.Path.mkdir()` | Creates single or multiple directories                       |
| `os.makedirs()`        | Creates multiple directories, including intermediate directories |

### Create single directories

To create a single directory, pass a path to the directory as a parameter to `os.mkdir()`:

```python
# Using os
import os

os.mkdir('example_directory/')

# Using pathlib
from pathlib import Path

p = Path('example_directory/')
p.mkdir()
```

If a directory already exists, `os.mkdir()` raises `FileExistsError`.  To avoid errors like this, catch the error when it happens and let your user know:

```python
from pathlin Path

p = Path('example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)
```

Alternatively, you can ignore the `FileExistsError` by passing the `exist_ok=True` argument to `.mkdir()`:

```python
from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True)
```

### Create multiple directories

`os.makedirs()` is similar to `os.mkdir()`. The difference between the two is that not only can `os.makedirs()` create individual directories, it can also be used to create directory trees. 

```python
import os

os.makedirs('Hello\\World')

'''
├───.ipynb_checkpoints
├───Hello
│   └───World
├───input-output
└───regular-expressions
'''
```

## Pattern Matching

### Using string method

```python
import os

# Get .txt files
for f_name in os.listdir('.'):
    if f_name.endswith('.md'):
        print(f_name)
        
'''
input-output.md
organize-files.md
README.md
regular-expressions.md
'''
```

### Using `fnmatch`

`fnmatch.fnmatch()` is a function that supports the use of wildcards such as `*` and `?` to match filenames. For example, in order to find all `.md` files in a directory using `fnmatch`, you would do the following:

```python
import os
import fnmatch

for file_name in os.listdir('.'):
    if fnmatch.fnmatch(file_name, '*.md'):
        print(file_name)
        
'''
input-output.md
organize-files.md
README.md
regular-expressions.md
'''
```

Another example:

```python
for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*-*.md'):
        print(filename)

'''
input-output.md
organize-files.md
regular-expressions.md
'''
```

### Using glob

`.glob()` in the `glob` module works just like `fnmatch.fnmatch()`, but unlike `fnmatch.fnmatch()`, it treats files beginning with a period (`.`) as special.

UNIX and related systems translate name patterns with wildcards like `?` and `*` into a list of files. This is called globbing.

For example, typing `mv *.py python_files/` in a UNIX shell moves (`mv`) all files with the `.py` extension from the current directory to the directory `python_files`. The `*` character is a wildcard that means “any number of characters,” and `*.py` is the glob pattern. This shell capability is not available in the Windows Operating System. The `glob` module adds this capability in Python, which enables Windows programs to use this feature.

```python
import glob
glob.glob('*.md')

# ['input-output.md', 'organize-files.md', 'README.md', 'regular-expressions.md']
```

`glob.glob('*.md')` searches for all files that have the `.md` extension in the current directory and returns them as a list.

## Traversing

A common programming task is walking a directory tree and processing files in the tree. Let’s explore how the built-in Python function `os.walk()` can be used to do this. `os.walk()` is used to generate filename in a directory tree by walking the tree either top-down or bottom-up. 

```python
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
        
'''
Found directory: .
file-joke.png
file-parts.png
input-output.md
organize-files.md
README.md
regular-expressions.md
Untitled.ipynb
Found directory: .\.ipynb_checkpoints
spreadsheet-whisperer-checkpoint.ipynb
Untitled-checkpoint.ipynb
Found directory: .\input-output
contacts_manager.py
database.txt
Found directory: .\regular-expressions
password_strength.py
'''
```

`os.walk()` returns three values on each iteration of the loop:

1. The name of the current folder
2. A list of folders in the current folder
3. A list of files in the current folder

To traverse the directory tree in a bottom-up manner, pass in a `topdown=False` keyword argument to `os.walk()`:

```python
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
        
'''
Found directory: .\.ipynb_checkpoints
spreadsheet-whisperer-checkpoint.ipynb
Untitled-checkpoint.ipynb
Found directory: .\input-output
contacts_manager.py
database.txt
Found directory: .\regular-expressions
password_strength.py
Found directory: .
file-joke.png
file-parts.png
input-output.md
organize-files.md
README.md
regular-expressions.md
Untitled.ipynb
'''
```

Passing the `topdown=False` argument will make `os.walk()` print out the files it finds in the *subdirectories* first.

## Deleting Files and Directories

### Deleting Files

To delete a single file, use `pathlib.Path.unlink()`, `os.remove()`. or `os.unlink()`.

`os.remove()` and `os.unlink()` are semantically identical. To delete a file, do the following:

```python
import os

data_file = 'D:\\tmp\\file.txt'
# Using remove
os.remove(data_file)
# Using unlink
os.unlink(data_file)
```

#### Deleting files with exception handling:

```python
import os

data_file = 'D:\\tmp\\file.txt'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}')
```

### Deleting Directories

The standard library offers the following functions for deleting directories:

- `os.rmdir()`
- `pathlib.Path.rmdir()`
- `shutil.rmtree()`

To delete a single directory or folder, use `os.rmdir()` or `pathlib.rmdir()`. These two functions only work if the directory you’re trying to delete is empty. If the directory isn’t empty, an `OSError` is raised. Here is how to delete a folder:

```python
import os

trash_dir = 'D:\\tmp\\'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

### Deleting Directories Tree

To delete non-empty directories and entire directory trees, Python offers `shutil.rmtree()`:

```python
import shutil

trash_dir =  'D:\\tmp\\'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

Everything in `trash_dir` is deleted when `shutil.rmtree()` is called on it. 

#### Common delete functions

| Function                | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `os.remove()`           | Deletes a file and does not delete directories               |
| `os.unlink()`           | Is identical to `os.remove()` and deletes a single file      |
| `pathlib.Path.unlink()` | Deletes a file and cannot delete directories                 |
| `os.rmdir()`            | Deletes an empty directory                                   |
| `pathlib.Path.rmdir()`  | Deletes an empty directory                                   |
| `shutil.rmtree()`       | Deletes entire directory tree and can be used to delete non-empty directories |

## Copying Files and Directories

### Copying Files

`shutil` offers a couple of functions for copying files. The most commonly used functions are `shutil.copy()` and `shutil.copy2()`.

```python
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)
```

### Copying Directories

`shutil.copytree()` will copy an entire directory and everything contained in it. `shutil.copytree(src, dest)` takes two arguments: a source directory and the destination directory where files and folders will be copied to.

```python
import shutil
shutil.copytree('data_1', 'data1_backup')

# 'data1_backup'
```

In this example, `.copytree()` copies the contents of `data_1` to a new location `data1_backup` and returns the destination directory. The destination directory must not already exist. It will be created as well as missing parent directories. `shutil.copytree()` is a good way to back up your files.

## Moving Files and Directories

o move a file or directory to another location, use `shutil.move(src, dst)`.

`src` is the file or directory to be moved and `dst` is the destination:

```python
import shutil
shutil.move('dir_1/', 'backup/')

# 'backup'
```

`shutil.move('dir_1/', 'backup/')` moves `dir_1/` into `backup/` if `backup/` exists. If `backup/` does not exist, `dir_1/` will be renamed to `backup`.

## Renaming Files and Directories

Python includes `os.rename(src, dst)` for renaming files and directories:

```python
os.rename('first.zip', 'first_01.zip')
```

The line above will rename `first.zip` to `first_01.zip`. If the destination path points to a directory, it will raise an `OSError`.

