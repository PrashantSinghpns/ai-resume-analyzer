import streamlit as st
import sys
import os

# fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pdfminer.high_level import extract_text
from src.preprocess import clean_text
from src.job_matcher import calculate_similarity


st.title("🤖 AI Resume Analyzer")
st.write("Analyze your resume against a job description using AI.")

# upload resume
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# job description input
job_description = st.text_area("Paste Job Description")


if uploaded_resume is not None and job_description:

    st.subheader("Resume Uploaded ✅")

    # 🔥 ONLY ONE processing block (inside spinner)
    with st.spinner("Analyzing resume..."):

        # extract text
        resume_text = extract_text(uploaded_resume)

        # clean text
        cleaned_resume = clean_text(resume_text)

        # similarity
        score = calculate_similarity(cleaned_resume, job_description)

    # show score
    st.subheader("📊 Match Score")
    st.success(str(round(score * 100, 2)) + "%")

    # feedback
    if score > 0.7:
        st.success("✅ Good match! You are suitable for this role.")
    elif score > 0.4:
        st.warning("⚠️ Average match. Try improving your skills.")
    else:
        st.error("❌ Low match. Consider improving your resume.")