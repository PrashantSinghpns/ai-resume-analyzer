from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text, job_text):
    """
    Calculates similarity between resume and job description
    using sentence embeddings and cosine similarity.
    """

    # Convert texts into embeddings
    embeddings = model.encode([resume_text, job_text])

    # Extract embeddings
    resume_embedding = embeddings[0]
    job_embedding = embeddings[1]

    # Compute cosine similarity (reshape to 2D)
    similarity_score = cosine_similarity(
        resume_embedding.reshape(1, -1),
        job_embedding.reshape(1, -1)
    )[0][0]

    return similarity_score


# Example usage
if __name__ == "__main__":
    resume = "Python developer with machine learning experience"
    job = "Looking for ML engineer skilled in Python and AI"

    score = calculate_similarity(resume, job)
    print("Similarity Score:", score)