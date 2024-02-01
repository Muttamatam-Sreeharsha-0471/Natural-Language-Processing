from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog chased the fox",
    "The fox is quick and the dog is lazy",
    "The cat is sitting on the windowsill",
]
# Query
query = "The quick fox"
def tfidf_search(query, documents):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    # Calculate TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    # Calculate cosine similarity between the query and each document
    cosine_similarities = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    # Rank documents based on cosine similarities
    ranked_documents = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)
    return ranked_documents
# Perform TF-IDF-based document ranking
results = tfidf_search(query, documents)
# Print the ranked documents
print("Ranked Documents:")
for index, similarity in results:
    print(f"Document {index + 1}: Similarity = {similarity:.4f}")
    print(f"   '{documents[index]}'\n")
