import re

SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "fast api",
    "sqlalchemy",
    "pycharm",
    "bootstrap",
    "jquery",
    "dynamodb",
    "html",
    "css",
    "svn",
    "requests",
    "pytest",
    "tox",
    "nginx",
    "gunicorn",
    "sonarqube",
    "visual studio",
    "selenium",
    "putty",
    "github desktop"

    # Backend Frameworks
    "django",
    "fastapi",
    "flask",

    # Frontend
    "react",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",

    # Cloud & DevOps
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "linux",
    "git",
    "github",
    "jenkins",
    "ci/cd",

    # Data Science & Analytics
    "data science",
    "data analysis",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",

    # AI & NLP
    "tensorflow",
    "pytorch",
    "nlp",
    "computer vision",

    # Data Engineering
    "spark",
    "hadoop",
    "kafka",
    "airflow",

    # AWS Services
    "lambda",
    "s3",
    "api gateway",
    "cloudwatch",
    "ec2",
    "rds",

    # Backend Concepts
    "rest api",
    "microservices",
    "api development",

    # Tools
    "jupyter notebook",
    "vscode",
    "postman",
    "excel",

    # ML Concepts
    "regression",
    "classification",
    "clustering",
    "feature engineering",
    "data preprocessing",
    "exploratory data analysis",
    "eda"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if re.search(
            r'\b' + re.escape(skill.lower()) + r'\b',
            text
        ):
            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )