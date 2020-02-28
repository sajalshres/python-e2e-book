"""A simple file-base contact manager module"""


__version__ = '1.0'
__author__ = 'Sajal N. Shrestha'
__email__ = 'sajal.shres@gmail.com'
__maintainer__ = 'Sajal N. Shrestha'
__status__ = 'development'

class Contacts(object):
    """
    Contact Manager object contact ia lot of contacts

    Args:

    Attributes:

    """
    def __init__(self):
        self._database_file = 'input-output/database.txt'
    
    def create(self, *args, **kwargs):
        contact = {}
        if args and len(args) == 4:
            contact['first_name'] = args[0]
            contact['last_name'] = args[1]
            contact['sex'] = args[2]
            contact['phone'] = args[3]
        elif kwargs and len(kwargs.keys()) == 4:
            contact = kwargs
        else:
            print('Argument is not in expected format, please try again')
            return False
        
        if not self.get(**contact):
            with open(self._database_file, 'a') as writer:
                writer.write("\n{first_name},{last_name},{sex},{phone}".format(**contact))
                print("Contact created successfully")
                return True
        else:
            print("Contact already found.")
            return False
        

    def get(self,*args, **kwargs):
        contacts = self.get_database()
        
        if args:
            # return next((contact for contact in contacts if all( value in contact.values() for value in args)), False)
            for contact in contacts:
                if set(args).issubset(contact.values()):
                    return contact
            return False
        elif kwargs:
            return next((contact for contact in contacts if 
                         all(contact[key] == kwargs[key] for key in kwargs.keys())), False)
        else:
            return self.get_database()
            

    def update(self):
        pass

    def delete(self):
        pass

    def get_database(self):
        contacts = []
        for contact_line in self.get_file_content():
            contact = contact_line.split(',')
            if len(contact) == 4:
                contacts.append({
                    'first_name': contact[0],
                    'last_name': contact[1],
                    'sex': contact[2],
                    'phone': contact[3],
                })
        if contacts:
            return contacts
        return False

    def get_file_content(self):
        with open(self._database_file, 'r') as contacts:
            return [contact.rstrip() for contact in contacts]


