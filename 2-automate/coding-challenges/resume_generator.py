import os

class resumegenerator:
    def _init_(self):
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
    def getFileName(self):
            return os.getcwd() + r"\rashmi.md"
            
    def create(self):
        fileName = self.getFileName()
       
        with open(fileName, "w") as w:
            w.write("# Resume")
#             for header in self.getHeader():
#                 w.write("\r{header}".format(header=header))
#                 if ((type(self.getData(header)) == 'list')
abc = resumegenerator()
print(abc.getFileName())
abc.create()