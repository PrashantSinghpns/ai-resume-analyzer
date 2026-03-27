from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = None


def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def calculate_similarity(resume_text, job_text):

    # convert texts to embeddings
    embeddings = get_model().encode([resume_text, job_text])

    resume_embedding = embeddings[0]
    job_embedding = embeddings[1]

    # calculate similarity
    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    return similarity
