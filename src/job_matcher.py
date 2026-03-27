from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_similarity(resume_text, job_text):
    # Convert both texts (resume & job description) into vector embeddings
    embeddings = model.encode([resume_text, job_text])

    # Extract individual embeddings
    resume_embedding = embeddings[0]
    job_embedding = embeddings[1]

    # Calculate cosine similarity between the two embeddings
    similarity = cosine_similarity(
        [resume_embedding],   # resume vector
        [job_embedding]       # job description vector
    )[0][0]  # Extract similarity score from matrix

    # Return similarity score (0 to 1)
    return similarity
