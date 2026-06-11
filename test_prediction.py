from predict import predict_resume

sample_resume = """
Experienced Python Developer with 5 years of experience in
building REST APIs using FastAPI and Django.

Worked extensively with AWS Lambda,
API Gateway, S3, PostgreSQL and Docker.

Implemented microservices architecture,
CI/CD pipelines and cloud-native applications.
"""

category, confidence = predict_resume(sample_resume)

print("Category:", category)
print("Confidence:", confidence)