# import function to extract text from PDF
from pdfminer.high_level import extract_text


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

    # print extracted text
    print("Resume Text:\n")
    print(resume_text)