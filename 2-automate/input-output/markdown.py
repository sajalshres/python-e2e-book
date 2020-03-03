def get_heading(message, level=1):
    if level in range(1,6):
        return "{0} {1} \n".format("#"*level, message)

def get_list(list_items, type = 'unordered'):
    """A method to return a markdown list
    """
    result = ""
    if type == 'unordered':
        result += "- {}\n".format(list_items)
       
    elif type == 'ordered':
         result += "1.{}\n".format(list_items)
    else:
        print('unexpected list type')

    return result     


if __name__ == '__main__':
    #Test get_heading
    print(get_heading("Basic Info",1))
    print(get_list("Name: Atul Shrestha"))#getting list
    print(get_list("Location: Okhaldhunga")) #getting list
    print(get_heading("Education",1))
    print(get_list("Bachelors in Computer Science"))#getting list
    print(get_list("Kathmandu University"))#getting list

      

   #Test get_list
   # print(get_list("this(*&^^%&)(*&)(***)is", "unordered"))
   # print(get_list("hello"))
   # print(get_list("", "ordered"))
   