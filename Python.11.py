import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Create a sample movie dataset (Fixed missing dictionary values)
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Dark Knight', 'Inception', 'Interstellar', 'Bloodline: Final Destination', 'Superbad'],
    'genres': ['Action Comic Dark Hero', 'Sci-Fi Dream Thriller Mind', 'Sci-Fi Space Time Drama',
               'Horror and Triller ', 'Comedy HighSchool Friends']
}

df = pd.DataFrame(data)

# 2. Convert text genres into numerical vectors using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])

# 3. Calculate similarity scores between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# 4. Recommendation Function
def get_recommendations(movie_title, cosine_sim=cosine_sim):
    # Extract integer index safely (Fixed missing index lookup)
    try:
        idx = df[df['title'] == movie_title].index[0]
    except IndexError:
        return f"Movie '{movie_title}' not found in the dataset."

    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort by the score value (Fixed lambda index mapping x[1])
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 2 closest matches (skipping itself at index 0)
    sim_scores = sim_scores[1:3]

    # Extract structural indices (Fixed mapping format)
    movie_indices = [i[0] for i in sim_scores]

    # Return the recommended movie titles
    return df['title'].iloc[movie_indices].tolist()


# 5. Test the Recommendation System
target_movie = "Inception"
recommendations = get_recommendations(target_movie)

print(f"Because you watched '{target_movie}', you might like:")
for movie in recommendations:
    print(f"- {movie}")
