"""Main Test module for resume generator
"""

from markdown import get_heading, get_list, get_paragraphs
from resume import generate_resume

if __name__ == '__main__':
    print("######## Testing get_heading function ")
    print(get_heading("hello", 0))
    print(get_heading("hello", 1))
    print(get_heading("hello", 4))
    print(get_heading("hello", 100))

    # Test get_list
    print("######## Testing get_list function")
    print(get_list(list_items=['hello', 'world']))
    print(get_list(0))
    print(get_list(["hello", "world"], ordered=True))

    # Test get_paragraphs
    print("######## Testing get_paragraph function")
    print(get_paragraphs("This is a paragraph"))
    print(get_paragraphs(1))
    try:
        print(get_paragraphs())
    except Exception as error:
        print(f"Unexpected error happend: {error}")

    # Test generate_resume
    print("######## Testing generate_resume function")
    print(generate_resume())