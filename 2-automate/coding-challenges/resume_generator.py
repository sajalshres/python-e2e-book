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
    f.write('# Resume\n')
    for first_header in database.keys():
        # print(first_header)
        f.writelines(f'## {first_header}\n')

    # f.write('abc')
    