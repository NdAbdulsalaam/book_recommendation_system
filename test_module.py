# Import previous modules
import load_dataset_module as load_dataset
import similarity_module as Similarity
import recommendation_module as get_recommendation

# test_module
# Function to verify input
def verify_input(message):
     while True:
        response = input(message)
        if len(response) < 1:
            print("Input cannot be empty")
            continue
        else:
            return response
    

def test_module():
    print("Welcome")
    while True:
        response = verify_input("Press 1 to check for user preference, 2 for similarity, 3 to for recommendation or  'q' to quit: ")
        if response.lower() == "q":
            return "Bye-bye!"
        try:
            num = int(response)
        except:
            print("Input must be an integer")
            continue
        
        if not 0 < num < 4:
            print("Invalid response")
            continue
            
        num =   str(num)  
        if num == "1":
            dir = verify_input("Paste dataset directory path: ")
            try: 
                print("Working on your input")
                user_preference = load_dataset(dir)
                return user_preference
            except:
                print("Invalid path")
                continue
        elif num == "2":
            dir = verify_input("Paste dataset directory path: ")
            try: 
                print("Working on your input")
                user_preference = load_dataset(dir)
            except:
                print("Invalid path")
                continue
                
            try:
                user = verify_input("What are you comparing? user/book: ")
                if user == "user":
                    target = verify_input("Target user's id: ")
                    other = verify_input("Other user's id: ")
                elif user == "book": 
                    target = verify_input("Target book's ISBN: ")
                    other = verify_input("Other book's ISBN: ")
                else:
                    print("Invalid options")
                    continue
                try:    
                    obs = int(verify_input("Kindly indicate the number of observation to include. This process is time consuming as observation increases: "))
                except:
                    print("Number of observations can only be an integer")
                    continue
                # Print available methods for the user to chose from
                print("""Options include:
                1. cosine_similarity
                2. cosine_distances
                3. manhattan_distances
                4. euclidean_distances
                5. haversine_distances""")
                method = verify_input("Select method: ")
                try:
                    if method.lower() in ["cosine_similarity", "cosine_distances", "manhattan_distances","euclidean_distances", "haversine_distances"]:
                        pass
                    else: int(method)
                except:
                    print("Invalid response")
                    continue
                similarity = Similarity(user_preference, target, other, user, method, obs)
                try:
                    similarity = round(similarity, 2)
                    return f"{method} score: {similarity}"
                except:
                    print(similarity)
                    continue
            except:
                print("Make sure to enter all the inputs correctly")
                continue
                
        # Recommendation        
        else:
            dir = verify_input("Paste dataset directory path: ")
            try: 
                print("Working on your input")
                user_preference = load_dataset(dir)
            except:
                print("Invalid path")
                continue
                
            try:
                user = verify_input("What are you recommending? user/book: ")
                if user == "user":
                    target = verify_input("Target user's id: ")
                elif user == "book": 
                    target = verify_input("Target book's ISBN: ")
                else:
                    print("Invalid option")
                    continue
                # Get total observations to include
                obs = int(verify_input("Kindly indicate the number of observation to include. This process is time consuming as observation increases: "))
                print("""Options include:
                1. cosine_similarity
                2. cosine_distances
                3. manhattan_distances
                4. euclidean_distances
                5. haversine_distances""")
                # Select an option
                method = verify_input("Select method: ")
                try:
                    if method.lower() in ["cosine_similarity", "cosine_distances", "manhattan_distances","euclidean_distances", "haversine_distances"]:
                        pass
                    else: int(method)
                except:
                    print("Invalid response")
                    continue
                try:
                    obs = int(verify_input("How many items should i recommend?"))
                except:
                    print("Number of observations can only be an integer")
                    continue
                # Call recommendation function
                recommendations =  get_recommendation(user_preference, target, user, method, obs, num)
                return recommendations
            except:
                print("Make sure to enter all the inputs correctly")
                continue