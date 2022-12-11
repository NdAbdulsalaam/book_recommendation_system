# Import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import haversine_distances

import warnings
warnings.filterwarnings("ignore")

# Generate the bag_of_words column
def imp_feat(df):
    # Ensure all columns are object
    for col in df.columns:
        df[col] = df[col].astype(str)
        
    # Convert each year(int) to string
    df["Year-Of-Publication"] = df["Year-Of-Publication"].apply(lambda x: str(x))
            
    # Create important features column
    for i in range(0, df.shape[0]):
        df["Bag-Of-Words"] = (
            df[["User-ID", "ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Book-Rating"]]
            .apply("".join, axis = 1)
                )
           
    return df

# Calculate similarity using cosine method
def Similarity(df, arg1, arg2, user, method, obs = 100):
    
    # The dataset is too big so I'll be using the n-observations as specified by the user
    df = df.head(obs)
    
    # Create the "Important-Features" the first time this fuction is run
    if "Bag-Of-Words" not in df.columns:
        imp_feat(df)
    
    # Create a class of cosine_similarity
    vectorizer = TfidfVectorizer()
    
    vector = vectorizer.fit_transform(df["Bag-Of-Words"].apply(lambda x: np.str_(x)))
#     similarity = cosine_similarity(vector)
# NEW CHANGE
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
        idx1 = indices[arg1]
        idx2 = indices[arg2]
    except KeyError as e:
        return "Kindly check the parameters provided. It is also possible that you set user to be True while it's False or vice versa" 
    
    # Calcuate score for various arg occurences
    scores = []
    len1 = [1 if len(str(idx1)) == 1 else idx1.shape[0]][0]
    len2 = [1 if len(str(idx2)) == 1 else idx2.shape[0]][0]
    
    if len1 == 1 & len2 == 1:
        score = similarity[idx1][idx2]
    elif len1 == 1 & len2 > 1:
        for i in range(len2):
            sim_score = similarity[idx1][idx2[i]]
            scores.append(sim_score)
            score =   np.mean(scores)
    elif len1 > 1 & len2 == 1:
        for i in range(len1):
            sim_score = similarity[idx1[i]][idx2]
            scores.append(sim_score)
            score =   np.mean(scores)
    else:
        for i in range(len1):
            for j in range(len2):
                sim_score = similarity[idx1[i]][idx2[j]]
                scores.append(sim_score)
                score =   np.mean(scores)
    
    return score