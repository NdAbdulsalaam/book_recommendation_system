# Import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import haversine_distances

def get_recommendation(df, target, user, method, obs = 100, num = 10):
    # The dataset is too big so I'll be using the n-observations as specified by the user
    df = df.head(obs)
    
    # Create the "Important-Features" the first time this fuction is run
    if "Bag-Of-Words" not in df.columns:
        imp_feat(df)
    
    # Create an instance of the class TfidfVectorizer()
    vectorizer = TfidfVectorizer()
    
    vector = vectorizer.fit_transform(df["Bag-Of-Words"].apply(lambda x: np.str_(x)))

# Select the similarity to use
    try: 
        if method == "cosine_similarity":
            similarity = cosine_similarity(vector)
        elif method == "cosine_distances":
            similarity = cosine_distances(vector)
        elif method == "manhattan":
            similarity = manhattan_distances(vector)
        elif method == "euclidean":
            similarity = euclidean_distances(vector)
        elif method == "haversine":
            similarity = haversine_distances(vector)
        else:
            print("Invalid option")
    except:
        return "Option not available"
    
    # Construct a reverse map of indices and User-ID / ISBN
    if user == "user":
        indices = pd.Series(df.index, index=df['User-ID'])
    else:
        indices = pd.Series(df.index, index=df['ISBN'])
    # Get the index of arguments
    try:
        idx = indices[target]
    except KeyError as e:
        return "Kindly check the parameters provided. It is also possible that you set user to be True while it's False or vice versa"
    
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(similarity[idx]))
    return sim_scores

#     # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the item indices
    item_indices = [i[0] for i in sim_scores]

    # Return the top 10 most items
    return df[target].iloc[item_indices]