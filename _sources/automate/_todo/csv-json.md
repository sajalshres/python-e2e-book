# Manipulating CSV and JSON Data

## Introduction

### CSV

A CSV file has a fairly simple structure. It’s a list of data separated by commas. For example, let’s say you have a few contacts in a contact manager, and you export them as a CSV file. You’d get a file containing text like this:

```
Name,Email,Phone Number,Address
Bob Smith,bob@example.com,123-456-7890,123 Fake Street
Mike Jones,mike@example.com,098-765-4321,321 Fake Avenue
```

That’s all a CSV file really is. They can be more complicated than that, and can contain thousands of lines, more entries on each line, or long strings of text. Some CSV files may not even have the headers at the top, and some may use quotation marks to surround each bit of data, but that’s the basic format.

### JSON

JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).

**JSON supports mainly 6 data types:**

1. string
2. number
3. boolean
4. null
5. object
6. array

```json
{
    "firstName": "Bikash", // string
    "lastName": "Adhikari",
    "age": 35, // number
    "married": true, // boolean
    "phone": null // null
    "job": {	// object
    	"titile": "Software Engineer",
    	"company": "Cotiviti"
	}
    "hobbies": ["python", "singing"], // array
}
```

## Manipulating CSV Files

### Sample Dataset

```
first_name,last_name,sex,phone 
Atul,Shrestha,Male,9843434323
Prashant,Paudel,Male,98732423423
Ram,Kasula,Male,32324324324
Sajal,Shrestha,Male,9840274974
Resa,Manandhar,Female,23432423
Rashmi,Maharjan,Female,2423423423
Prabin,Kayastha,Male,23423432423
Bikram,Manandhar,Male,98221312
```

### Reading CSV files

Reading from a CSV file is done using the `reader` object. The CSV file is opened as a text file with Python’s built-in `open()` function, which returns a file object. This is then passed to the `reader`, which does the heavy lifting.

```python
import csv

with open('./input-output/database.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} is {row[2]} and can be reached at {row[3]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
    
"""
Column names are first_name, last_name, sex, phone
	Atul Shrestha is Male and can be reached at 9843434323.
	Prashant Paudel is Male and can be reached at 98732423423.
	Ram Kasula is Male and can be reached at 32324324324.
	Sajal Shrestha is Male and can be reached at 9840274974.
	Resa Manandhar is Female and can be reached at 23432423.
	Rashmi Maharjan is Female and can be reached at 2423423423.
	Prabin Kayastha is Male and can be reached at 23423432423.
	Bikram Manandhar is Male and can be reached at 98221312.
Processed 9 lines.
"""
```

### Reading CSV files into dictionary

Rather than deal with a list of individual `String` elements, you can read CSV data directly into a dictionary.

```python
import csv

with open('./input-output/database.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f"\t{row['first_name']} {row['last_name']} is {row['sex']} and can be reached at {row['phone']}.")
        line_count += 1
    print(f'Processed {line_count} lines.')
    
"""
Column names are first_name, last_name, sex, phone
	Atul Shrestha is Male and can be reached at 9843434323.
	Prashant Paudel is Male and can be reached at 98732423423.
	Ram Kasula is Male and can be reached at 32324324324.
	Sajal Shrestha is Male and can be reached at 9840274974.
	Resa Manandhar is Female and can be reached at 23432423.
	Rashmi Maharjan is Female and can be reached at 2423423423.
	Prabin Kayastha is Male and can be reached at 23423432423.
	Bikram Manandhar is Male and can be reached at 98221312.
Processed 9 lines.
"""
```

### Writing CSV files

You can also write to a CSV file using a `writer` object and the `.write_row()` method:

```python
import csv

with open('database.csv', mode='w') as database:
    database_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    database_writer.writerow(['Shilpa', 'Gorkhali', 'Female', 908990790])
    database_writer.writerow(['Shreya', 'Mool', 'Female', 983234])
```

The `quotechar` optional parameter tells the `writer` which character to use to quote fields when writing. Whether quoting is used or not, however, is determined by the `quoting` optional parameter:

- If `quoting` is set to `csv.QUOTE_MINIMAL`, then `.writerow()` will quote fields only if they contain the `delimiter` or the `quotechar`. This is the default case.
- If `quoting` is set to `csv.QUOTE_ALL`, then `.writerow()` will quote all fields.
- If `quoting` is set to `csv.QUOTE_NONNUMERIC`, then `.writerow()` will quote all fields containing text data and convert all numeric fields to the `float` data type.
- If `quoting` is set to `csv.QUOTE_NONE`, then `.writerow()` will escape delimiters instead of quoting them. In this case, you also must provide a value for the `escapechar` optional parameter.

### Writing CSV files from dictionary

```python
with open('database.csv', mode='w') as csv_file:
    fieldnames = ['first_name', 'last_name', 'sex', 'phone']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Rabin', 'last_name': 'Dahal', 'sex': 'Male', 'phone': 909809})
    writer.writerow({'first_name': 'Pabin', 'last_name': 'Kayastha', 'sex': 'Male', 'phone': 909809})
```

Unlike `DictReader`, the `fieldnames` parameter is required when writing a dictionary. 

## Manipulating JSON Data

Python comes with a built-in package called json for encoding and decoding JSON data.

### Reading(Deserialize) JSON Data from file

```python
import json

with open("database.json", "r") as database_file:
    data = json.load(database_file)
```

### Reading(Deserialize) JSON Data from string

```python
json_data = """
{
    "firstName": "Bikash", // string
    "lastName": "Adhikari",
    "age": 35, // number
    "married": true, // boolean
    "phone": null // null
    "job": {	// object
    	"titile": "Software Engineer",
    	"company": "Cotiviti"
	}
    "hobbies": ["python", "singing"], // array
}
"""

data = json.loads(json_data)
```

### Witing(Serialize) JSON Data to file

```python
import json

data = {
    "firstName": "Bikash", // string
    "lastName": "Adhikari",
    "age": 35, // number
    "married": true, // boolean
    "phone": null // null
    "job": {	// object
    	"titile": "Software Engineer",
    	"company": "Cotiviti"
	}
    "hobbies": ["python", "singing"], // array
}

with open("database.json", "w") as write_file:
    json.dump(data, write_file)
```

Note that `dump()` takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.

### JSON Data to String

```python
import json

json_string = json.dumps(data)
```

