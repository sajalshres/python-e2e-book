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

def writeToFile(content):
    with open("binayshakya-resume.md", 'a') as binay:
        binay.write(content)

PERSONAL_INFO = "personal_info"
OBJECTIVE = "objective"
EDUCATION = "education"
EMPLOYMENT = "employment"


for key, value in database.items():
    if key == PERSONAL_INFO:
        personal_info = database.get(PERSONAL_INFO)
        name = personal_info.get("name")
        location = personal_info.get("location")
        phone = personal_info.get("phone")
        email = personal_info.get("email")
        writeToFile("# Resume")
        writeToFile("\n")
        writeToFile("\n{0}".format(name))
        writeToFile("\n{0}".format(location))
        writeToFile("\n{0}".format(phone))
        writeToFile("\n{0}\n".format(email))
    elif key == OBJECTIVE:
        objective = database.get(OBJECTIVE)
        writeToFile("\n## Objective")
        writeToFile("\n")
        writeToFile("\n{0}\n".format(objective))
    elif key == EDUCATION:
        education_list = database.get(EDUCATION)
        writeToFile("\n## Education\n")
        for education in education_list:
            institution = education.get("institution")
            location = education.get("location")
            year = education.get("year")
            degree = education.get("degree")
            description = education.get("description")
            writeToFile("\n#### {0}, {1}, {2}".format(institution,location,year))
            writeToFile("\n-{0}".format(description))
    elif key == EMPLOYMENT:
        employment_list = database.get(EMPLOYMENT)

            
                

        





    
