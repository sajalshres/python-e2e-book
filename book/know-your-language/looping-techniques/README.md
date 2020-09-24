# How to Loop: Looping Techniques

## Lists and Sequences

### Looping through a sequence

**Example:**


```python
for item in ['This', 'class', 'is', 'awesome']:
    print(item)
```

*Output:*

    This
    class
    is
    awesome


### Loop through a sequence using `enumerate()`


```python
enumerate(['This', 'class', 'is', 'awesome'])
```

*Output:*


    <enumerate at 0x2ce369e9ac0>

*Output:*


```python
list(enumerate(['This', 'class', 'is', 'awesome']))
```

*Output:*


    [(0, 'This'), (1, 'class'), (2, 'is'), (3, 'awesome')]


```python
list(enumerate(['This', 'class', 'is', 'awesome'], start=1))
```

*Output:*


    [(1, 'This'), (2, 'class'), (3, 'is'), (4, 'awesome')]

**Example:**


```python
for iterator, value in enumerate(['This', 'class', 'is', 'awesome']):
    print(iterator, value)
```

*Output:*

    0 This
    1 class
    2 is
    3 awesome

### Loop through a sequence in reverse using `reversed()`

**Example:**


```python
for item in reversed(['This', 'class', 'is', 'awesome']):
    print(item)
```

*Output:*

    awesome
    is
    class
    This

### Looping through multiple sequences using `zip()`

**Example:**


```python
questions = ['sex', 'name', 'shape']
answers = ['Male', 'Pau', 'Orange in shape']

for question, answer in zip(questions, answers):
    print('What is your ' + str(question) + '?')
    print('I am ' + str(answer))
    print()
```

*Output:*

    What is your sex?
    I am Male
    
    What is your name?
    I am Pau
    
    What is your shape?
    I am Orange in shape    

## Dictionaries

### Looping though dictionary using `items()`

**Example:**


```python
contact = {
    'Ram Kasula': 9840298755,
    'Anu Pau': 98651201503,
    'Kade Hade': 9863331239
}

for name, number in contact.items():
    print(name, number)
```

*Output:*

    Ram Kasula 9840298755
    Anu Pau 98651201503
    Kade Hade 9863331239


## Looping though dictionary using `iteritems()`
This is depreciated in Python 3
