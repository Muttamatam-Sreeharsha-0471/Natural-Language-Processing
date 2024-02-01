import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_coherence(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')

    # Compute TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Compute cosine similarity between sentences
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Calculate coherence score
    coherence_score = similarity_matrix.mean()

    return coherence_score

if __name__ == "__main__":
    # Example text
    input_text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. It involves the development of algorithms and models that enable machines to understand, interpret, and generate human-like text. NLP has applications in various domains, including chatbots, sentiment analysis, and language translation.

    Coherence in a text refers to the logical connection and smooth flow of ideas between sentences and paragraphs. A coherent text is easier to understand and retains the reader's attention. Evaluating coherence is crucial in assessing the quality of written communication.

    This program computes the coherence of a given text by analyzing the similarity between sentences using TF-IDF vectors. The higher the coherence score, the more connected and coherent the text is considered.

    Feel free to replace this example text with your own to evaluate the coherence of different texts.
    """

    # Compute coherence score
    coherence_score = compute_coherence(input_text)

    # Display the coherence score
    print(f"Coherence Score: {coherence_score}")
