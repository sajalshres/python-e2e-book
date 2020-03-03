def get_heading(message, level=1):
    if level in range(1,6):
        return "{0} {1} \n".format("#"*level, message)

def get_list(list_items, ordered=False):
    """A method to return a markdown list
    """
    result = ""
    if isinstance(list_items,(list,tuple,set)):
        if not ordered:
            return "\n".join([f"-{item}" for item in list_items])
        else:
            return "\n".join([f"{item[0]+1}. {item[1]}" for item in enumerate(list_items)])
    else:
        print('unexpected list type')

    return result     

def get_paragraph(message):
    return f"{message}\n\n"

# def generate_resume:
#     resume = []
#     resume.append(get_heading("Resume"))
    

if __name__ == '__main__':
    #Test get_heading
    # print(get_heading("Resume",1))
    # print(get_list("Name: Atul Shrestha"))#getting list
    # print(get_list("Location: Okhaldhunga")) #getting list
    # print(get_heading("Education",1))
    # print(get_list("Bachelors in Computer Science"))#getting list
    # print(get_list("Kathmandu University"))#getting list

    # print(get_list(["abinay","shakya"]))#getting list
    # print(get_list(["a","b","c"],"ordered"))#getting list

    print(get_paragraph("this is testing"))




   #Test get_list
   # print(get_list("this(*&^^%&)(*&)(***)is", "unordered"))
   # print(get_list("hello"))
   # print(get_list("", "ordered"))
   