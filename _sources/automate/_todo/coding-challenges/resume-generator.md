# Coding Challenge

## Resume Generator

Write a resume generator module that will generate a resume based on a data structure mentioned below.

The resume generator should read the data structure and generate a resume like [sample-resume.md](./coding-challenges/sample-resume.md). The resume should save in current directory or the desired output directory if mentioned. The output should be in the filename `name-resume.md` 

```python
database = {
    'personal_info': {
        'name': 'Your Name',
        'location': 'Your Location',
        'phone': 'Your phone number',
        'email': 'email address'
    },
    'objective': "Your objective",
    "education": [
        {
            "institution": "University Name",
            "location": "Location",
            "year": 1990,
            "degree": "degree name",
            "description": "your grade description"
        },
        {
            "institution": "University Name",
            "location": "Location",
            "year": 1990,
            "degree": "degree name",
            "description": "your grade description"
        }
    ],
    "employment": [
        {
            "role": "role name",
            "year": 1990,
            "company": "company name",
            "location": "location",
            "description": [
                "description 1",
                "description 2",
            ]
        },
        {
            "role": "role name",
            "year": 1990,
            "company": "company name",
            "location": "location",
            "description": [
                "description 1",
                "description 2",
            ]
        }
    ],
    "skills": [
        "Sample skills and abilities 1",
        "Sample skills and abilities 2"
    ],
    "activities": [
        "Sample activity 1",
        "Sample activity 2"
    ],
    "hobbies": [
        "Sample hobby 1",
        "Sample hobby 2"
    ]
}
```

## Mark Down file cheat sheet

## Basic Syntax

These are the elements outlined in John Gruber’s original design document. All Markdown applications support these elements.

| Element                                                      | Markdown Syntax                            |
| ------------------------------------------------------------ | ------------------------------------------ |
| [Heading](https://www.markdownguide.org/basic-syntax/#headings) | `# H1## H2### H3`                          |
| [Bold](https://www.markdownguide.org/basic-syntax/#bold)     | `**bold text**`                            |
| [Italic](https://www.markdownguide.org/basic-syntax/#italic) | `*italicized text*`                        |
| [Blockquote](https://www.markdownguide.org/basic-syntax/#blockquotes-1) | `> blockquote`                             |
| [Ordered List](https://www.markdownguide.org/basic-syntax/#ordered-lists) | `1. First item2. Second item3. Third item` |
| [Unordered List](https://www.markdownguide.org/basic-syntax/#unordered-lists) | `- First item- Second item- Third item`    |
| [Code](https://www.markdownguide.org/basic-syntax/#code)     | ``code``                                   |
| [Horizontal Rule](https://www.markdownguide.org/basic-syntax/#horizontal-rules) | `---`                                      |
| [Link](https://www.markdownguide.org/basic-syntax/#links)    | `[title](https://www.example.com)`         |
| [Image](https://www.markdownguide.org/basic-syntax/#images-1) | `![alt text](image.jpg)`                   |

## Extended Syntax

These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements.

| Element                                                      | Markdown Syntax                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Table](https://www.markdownguide.org/extended-syntax/#tables) | `| Syntax | Description || ----------- | ----------- || Header | Title || Paragraph | Text |` |
| [Fenced Code Block](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) | ````{ "firstName": "John", "lastName": "Smith", "age": 25}```` |
| [Footnote](https://www.markdownguide.org/extended-syntax/#footnotes) | `Here's a sentence with a footnote. [^1][^1]: This is the footnote.` |
| [Heading ID](https://www.markdownguide.org/extended-syntax/#heading-ids) | `### My Great Heading {#custom-id}`                          |
| [Definition List](https://www.markdownguide.org/extended-syntax/#definition-lists) | `term: definition`                                           |
| [Strikethrough](https://www.markdownguide.org/extended-syntax/#strikethrough) | `~~The world is flat.~~`                                     |
| [Task List](https://www.markdownguide.org/extended-syntax/#task-lists) | `- [x] Write the press release- [ ] Update the website- [ ] Contact the media` |