database = {
    'personal_info': {
        'name': 'Prabin Kayastha',
        'location': 'Bhaktapur',
        'phone': '984156213213',
        'email': 'prabin.kayastha@cotiviti.com'
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

import os


resume_path = r"2-automate\coding-challenges\Resume-{}.md".format(database['personal_info']['name'].title().replace(' ',  ''))
with open(resume_path, 'w') as f:
    f.write('# Resume\n\n')
    for first_header in database.keys():
        # print(first_header)
        f.writelines(f'## {first_header}\n')
        if isinstance(database[first_header], dict):
            for second_header in database[first_header].keys():
                f.writelines(f'### {second_header}\n')
        elif isinstance(database[first_header], list):
            for second_header in database[first_header]:
                f.writelines(f'### {second_header}\n')
                for i in second_header:
                    f.writelines(i)
                

    # f.write('abc')
    

class ResumeGenerator:
    
    def __init__(self, *args, **kwargs):
        self._resume_contents = kwargs
        print

    def print_personal_info(self):
        for i in self._resume_contents['personal_info']:
            print('i')


prabin=ResumeGenerator(database.items())
prabin.print_personal_info()