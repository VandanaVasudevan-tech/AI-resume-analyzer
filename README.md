# AI-resume-analyzer


# AI Resume Analyzer using DistilBERT

## Overview

AI Resume Analyzer is a deep learning-based web application that analyzes resumes and predicts the most suitable job category. The system uses the DistilBERT transformer model to classify resumes into multiple job domains and provides detailed insights such as ATS matching, resume scoring, skill extraction, experience analysis, and education detection.

The application is built using Python, Hugging Face Transformers, PyTorch, and Streamlit.

---

## Features

* Resume Classification using DistilBERT
* Prediction Confidence Score
* ATS (Applicant Tracking System) Match Analysis
* Resume Quality Scoring
* Skill Extraction
* Experience Detection
* Education Extraction
* Downloadable Resume Analysis Report
* Interactive Streamlit Dashboard
* PDF Resume Upload Support

---

## Dataset

* Total Resumes: 10,035
* Categories: 99 Job Categories
* Data Source: Public Resume Dataset
* Preprocessed using text cleaning and normalization techniques

---

## Deep Learning Workflow

### 1. Data Collection

Collected over 10,000 resumes belonging to 99 different job categories.

### 2. Data Preprocessing

* Text Cleaning
* Lowercasing
* Removal of Special Characters
* Handling Missing Values
* Label Encoding

### 3. Train-Test Split

* Training Data: 80%
* Testing Data: 20%

### 4. Model Selection

* DistilBERT Transformer Model
* Hugging Face Transformers Library
* PyTorch Framework

### 5. Model Training

* Epochs: 4
* Maximum Sequence Length: 256
* Batch Size: 8

### 6. Model Evaluation

Metrics Used:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Model Performance

| Metric       | Value          |
| ------------ | -------------- |
| Accuracy     | 66.97%         |
| Classes      | 99             |
| Dataset Size | 10,035 Resumes |

The confusion matrix and classification report were generated to evaluate model performance across all categories.

---

## Technologies Used

* Python
* Streamlit
* PyTorch
* Hugging Face Transformers
* DistilBERT
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* PyPDF2

---

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── artifacts/
│   └── label_encoder.pkl
│
├── resume_classifier/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
├── utils/
│   ├── pdf_extractor.py
│   ├── skill_extractor.py
│   ├── experience_extractor.py
│   ├── education_extractor.py
│   ├── ats_matcher.py
│   └── scoring.py
│
└── notebooks/
    ├── resume.ipynb
    ├── evaluate.ipynb
    └── resume_analyzer.ipynb
```


Run the application:

```bash
streamlit run app.py
```

---

## Usage

1. Upload a PDF resume.
2. View predicted job category.
3. Check prediction confidence.
4. Review resume score.
5. Analyze ATS match against a job description.
6. Download the generated report.

---

## Future Enhancements

* Resume Recommendation System
* Job Matching Engine
* LLM-based Resume Improvement Suggestions
* Multi-language Resume Support
* Advanced ATS Optimization

---

Model file omitted due to GitHub size limits.
Download from:
https://drive.google.com/drive/folders/1tMoupvBT2jv6SR88Je4jyoSODXOLxbbl?usp=drive_link


---

## Screenshots

<img width="1797" height="702" alt="image" src="https://github.com/user-attachments/assets/a5d9516d-3ce8-488f-9a1e-a439e5759769" />


<img width="1822" height="846" alt="image" src="https://github.com/user-attachments/assets/5337329e-82f2-41a4-913e-914d7864e84b" />

<img width="1877" height="641" alt="image" src="https://github.com/user-attachments/assets/df158ea0-41a6-448d-967e-239e6d4e1837" />

<img width="1852" height="892" alt="image" src="https://github.com/user-attachments/assets/17a38991-8e6d-4c7c-ab18-f20e107d3a0c" />

<img width="1837" height="801" alt="image" src="https://github.com/user-attachments/assets/d23d6662-0ee0-4d96-a2be-10ed221a8314" />
<img width="1702" height="107" alt="image" src="https://github.com/user-attachments/assets/1eb8d9b4-2947-41bc-90c1-38ea48a84941" />


<img width="1855" height="732" alt="image" src="https://github.com/user-attachments/assets/6dbb509d-22a3-4bd5-8927-df3d7f13d4dd" />









---
