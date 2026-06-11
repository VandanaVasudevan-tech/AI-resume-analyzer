import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.experience_extractor import extract_experience
from utils.education_extractor import extract_education
from utils.scoring import calculate_resume_score
from utils.ats_matcher import calculate_ats_score

from predict import predict_resume

# =========================
# CUSTOM CSS DESIGN
# =========================

st.markdown("""
<style>

.main-title {
    text-align:center;
    color:#1E88E5;
    font-size:40px;
    font-weight:bold;
}

div[data-testid="metric-container"]{
    background-color:#ffffff;
    border:2px solid #1E88E5;
    padding:10px;
    border-radius:10px;
}

.stButton > button {
    width:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.markdown(
    "Upload a resume and get AI-powered analysis."
)

# --------------------------------------------------
# Education Mapping
# --------------------------------------------------

education_mapping = {
    "be": "Bachelor of Engineering",
    "b.e": "Bachelor of Engineering",
    "b.tech": "Bachelor of Technology",
    "btech": "Bachelor of Technology",
    "bsc": "Bachelor of Science",
    "b.sc": "Bachelor of Science",
    "m.tech": "Master of Technology",
    "mtech": "Master of Technology",
    "mba": "Master of Business Administration",
    "msc": "Master of Science",
    "m.sc": "Master of Science",
    "phd": "Doctor of Philosophy",
    "bca": "Bachelor of Computer Applications",
    "mca": "Master of Computer Applications"
}

# --------------------------------------------------
# Upload Resume
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description (Optional)",
    height=200
)
ats_score = 0
matched_skills = []
missing_skills = []
# --------------------------------------------------
# Main Processing
# --------------------------------------------------

if uploaded_file:

    try:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        if not resume_text.strip():
            st.error(
                "No text could be extracted from this PDF."
            )
            st.stop()

    except Exception as e:

        st.error(
            f"Error reading PDF: {e}"
        )
        st.stop()

    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    category, confidence = predict_resume(
        resume_text
    )

    category = category.replace(
        " resumes",
        ""
    )

    category = category.replace(
        "Developer",
        " Developer"
    )

    # --------------------------------------------------
    # Extract Information
    # --------------------------------------------------

    skills = extract_skills(
        resume_text
    )

    experience = extract_experience(
        resume_text
    )

    education = extract_education(
        resume_text
    )

    education = [
        education_mapping.get(
            item.lower(),
            item
        )
        for item in education
    ]

    score = calculate_resume_score(
        len(skills),
        experience,
        education
    )

    ats_score, matched_skills, missing_skills = (
        calculate_ats_score(
            skills,
            job_description
        )
    )

    # --------------------------------------------------
    # Resume Analysis
    # --------------------------------------------------

    st.subheader(
        "Resume Analysis"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Predicted Role",
            category
        )

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with col3:
        st.metric(
            "Resume Score",
            f"{score}/100"
        )

    st.progress(
        confidence / 100
    )

    if confidence >= 80:
        st.success(
            "High confidence prediction"
        )
    elif confidence >= 60:
        st.info(
            "Moderate confidence prediction"
        )
    else:
        st.warning(
            "Low confidence prediction"
        )

    if score >= 80:
        st.success(
            "🌟 Excellent Resume"
        )
    elif score >= 60:
        st.info(
            "👍 Good Resume"
        )
    else:
        st.warning(
            "⚠️ Needs Improvement"
        )

    # --------------------------------------------------
    # ATS Match Analysis
    # --------------------------------------------------

    if job_description.strip():

        st.subheader(
            "🎯 ATS Match Analysis"
        )

        st.metric(
            "ATS Match Score",
            f"{ats_score}%"
        )

        st.write(
            "### ✅ Matched Skills"
        )

        if matched_skills:

            st.success(
                ", ".join(
                    matched_skills
                )
            )

        else:

            st.warning(
                "No matching skills found"
            )

        st.write(
            "### ❌ Missing Skills"
        )

        if missing_skills:

            st.error(
                ", ".join(
                    missing_skills
                )
            )

        else:

            st.success(
                "No missing skills"
            )

        if missing_skills:

            st.subheader(
                "💡 Suggestions"
            )

            for skill in missing_skills:

                st.write(
                    f"• Consider adding experience with {skill}"
                )
    # --------------------------------------------------
    # Download Report
    # --------------------------------------------------

    report_text = f"""
    AI Resume Analyzer Report
    =========================

    Predicted Role:
    {category}

    Confidence:
    {confidence:.2f}%

    Resume Score:
    {score}/100

    Skills Found:
    {', '.join(skills)}

    Experience:
    {experience} Years

    Education:
    {', '.join(education)}

    ATS Score:
    {ats_score}%

    Matched Skills:
    {', '.join(matched_skills)}

    Missing Skills:
    {', '.join(missing_skills)}
    """

    st.download_button(
        label="📥 Download Analysis Report",
        data=report_text,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )
    # --------------------------------------------------
    # Resume Statistics
    # --------------------------------------------------

    st.subheader(
        "Resume Statistics"
    )

    stat1, stat2, stat3 = st.columns(3)

    with stat1:
        st.metric(
            "Skills Found",
            len(skills)
        )

    with stat2:
        st.metric(
            "Education Entries",
            len(education)
        )

    with stat3:
        st.metric(
            "Characters",
            len(resume_text)
        )

    # --------------------------------------------------
    # Skills
    # --------------------------------------------------

    st.subheader(
        "Skills Found"
    )

    if skills:

        st.success(
            ", ".join(skills)
        )

    else:

        st.warning(
            "No skills detected"
        )

    # --------------------------------------------------
    # Experience
    # --------------------------------------------------

    st.subheader(
        "Experience"
    )

    if experience and experience > 0:

        st.success(
            f"{experience} Years"
        )

    else:

        st.warning(
            "Experience not detected"
        )

    # --------------------------------------------------
    # Education
    # --------------------------------------------------

    st.subheader(
        "Education"
    )

    if education:

        for degree in education:

            st.success(
                degree
            )

    else:

        st.warning(
            "Education not detected"
        )

    # --------------------------------------------------
    # Extracted Resume Text
    # --------------------------------------------------

    with st.expander(
        "View Extracted Resume Text"
    ):

        st.text_area(
            "",
            resume_text[:10000],
            height=400
        )