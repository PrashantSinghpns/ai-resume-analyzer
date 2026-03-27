# Import libraries
from pdfminer.high_level import extract_text
from preprocess import clean_text
from job_matcher import calculate_similarity


# Function to extract text from resume PDF
def extract_resume_text(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print("Error reading resume:", e)
        return ""


# Function to read job description file
def read_job_description(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print("Error reading job description:", e)
        return ""


# Main program
if __name__ == "__main__":

    resume_path = "data/Resume_sample.pdf"
    job_path = "data/job_description.txt"

    # Extract resume text
    resume_text = extract_resume_text(resume_path)

    if not resume_text:
        print("Resume text could not be extracted.")
        exit()

    # Clean resume text
    cleaned_resume = clean_text(resume_text)

    print("\nCleaned Resume Text:\n")
    print(cleaned_resume[:500])  # show first 500 characters only

    # Read job description
    job_text = read_job_description(job_path)

    if not job_text:
        print("Job description not found.")
        exit()

    # Calculate similarity score
    score = calculate_similarity(cleaned_resume, job_text)

    print("\nResume Match Score:", round(score * 100, 2), "%")