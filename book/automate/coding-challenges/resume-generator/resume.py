"""A script to generate resume
"""

from markdown import get_heading, get_list, get_paragraphs
from database import DATABASE

def generate_resume():
    """Generates a resume in markdown
    """
    resume = []
    # Generate heading
    resume.append(get_heading("Resume"))
    # Generate personal information
    resume.append(get_paragraphs(DATABASE['personal_info']['name']))

    return resume