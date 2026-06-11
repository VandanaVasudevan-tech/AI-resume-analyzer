import re

EDUCATION_KEYWORDS = {
    "bachelor of technology": "Bachelor of Technology",
    "b.tech": "Bachelor of Technology",
    "btech": "Bachelor of Technology",
    "master of computer applications": "Master of Computer Applications",
    "mca": "Master of Computer Applications",

    "bachelor of computer applications": "Bachelor of Computer Applications",
    "bca": "Bachelor of Computer Applications",

    "bachelor of engineering": "Bachelor of Engineering",
    "b.e": "Bachelor of Engineering",

    "bachelor of science": "Bachelor of Science",
    "bsc": "Bachelor of Science",
    "b.sc": "Bachelor of Science",

    "master of technology": "Master of Technology",
    "m.tech": "Master of Technology",
    "mtech": "Master of Technology",

    "master of science": "Master of Science",
    "msc": "Master of Science",
    "m.sc": "Master of Science",

    "master of business administration": "Master of Business Administration",
    "mba": "Master of Business Administration",

    "phd": "Doctor of Philosophy"
}


def extract_education(text):
    text = text.lower()

    found = []

    for keyword, degree in EDUCATION_KEYWORDS.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            found.append(degree)

    return sorted(list(set(found)))