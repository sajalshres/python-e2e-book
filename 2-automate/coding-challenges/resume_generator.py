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
from pprint import pprint


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
    
    def __init__(self, database):
        self._database = database

    def extract_personal_info(self, **kwargs):
        text = '# Personal Information\n'
        pprint(self._database)
        pprint(self._database['personal_info'])
        for key, value in kwargs.items():
            # print('{} : {}'.format(key.title(),value.title()))
            text = text + '{} : {}'.format(key.title(),value.title()) + '\n'
        return text

    def extract_objective(self):
        text = '# Objective\n'
        # pprint(self._database)
        pprint(self._database['objective'])
        text = text + self._database['objective'] +'\n'
        return text


if __name__ == '__main__':
    prabin=ResumeGenerator(database)
    # print(**database['personal_info'])
    print(prabin.extract_personal_info(**database['personal_info']))
    # print(database['objective'])
    print(prabin.extract_objective())