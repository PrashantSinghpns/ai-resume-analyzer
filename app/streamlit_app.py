import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from pdfminer.high_level import extract_text
from preprocess import clean_text
from job_matcher import calculate_similarity


st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description.")

# upload resume
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# job description input
job_description = st.text_area("Paste Job Description")

if uploaded_resume is not None and job_description:

    # extract resume text
    resume_text = extract_text(uploaded_resume)

    # clean text
    cleaned_resume = clean_text(resume_text)

    # calculate similarity
    score = calculate_similarity(cleaned_resume, job_description)

    st.subheader("Match Score")
    st.write(str(round(score * 100, 2)) + "%")
