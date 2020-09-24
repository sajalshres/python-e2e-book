"""A python based markdown module
"""

def get_heading(message, level=1):
    """Return a markdown heading
    """
    if level in range(1,6):
        return "{0} {1}".format("#"*level, message)

    return None

def get_list(list_items, ordered=False):
    """ A method to return a markdown list
    """
    if isinstance(list_items, (list, tuple, set)):
        if not ordered :
           return "\n".join([f"* {item}" for item in list_items])
        else:
            return "\n".join([f"{item[0]+1}. {item[1]}"
            for item in enumerate(list_items)])
    else:
        print("Unexpected list type")
        return None

def get_paragraphs(message):
    """ A method to get a markdown paragrah
    """
    return f"{message}\n\n"