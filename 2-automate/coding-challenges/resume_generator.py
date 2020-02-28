database = {
    'personal_info': {
        'name': 'Shilpa',
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

file_name = "{name}-resume.md".format(name=database['personal_info']['name'].split(' ')[0])
print(file_name)
file_entries='# Resume '+'\n'+database['personal_info']['name']
with open(file_name, 'w') as resume:
    resume.write(file_entries)

    
       
       
  
