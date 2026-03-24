# import function to extract text from PDF
from pdfminer.high_level import extract_text
from preprocess import clean_text
from job_matcher import calculate_similarity


# function to read resume PDF and return text
def extract_resume_text(pdf_path):
    text = extract_text(pdf_path)   # extract all text from the pdf
    return text


# main program
if __name__ == "__main__":

    # path to the sample resume
    resume_path = "data/Resume_sample.pdf"

    # call the function
    resume_text = extract_resume_text(resume_path)

    # clean the resume text
    cleaned = clean_text(resume_text)

    print("\nCleaned Resume Text:\n")
    print(cleaned)

    # read job description
    with open("data/job_description.txt", "r") as f:
        job_text = f.read()

    # calculate similarity
    score = calculate_similarity(cleaned, job_text)

    print("\nResume Match Score:", round(score * 100, 2), "%")