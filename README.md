<h1 align = 'center', style="font-size:50px"> Book Recommendation System</h1>


# Overview
We now routinely share and consume content on the Web due to the overwhelming amount of online content and the rising availability of devices with Internet access. However, the amount of information available online is making it more and more difficult for users to find material or objects of interest. Choosing from the glut of available content what to consume or purchase options becomes more and more challenging. In this sense, a corporation that sells books online does so to millions of internet users.

# Modules
- **Load_dataset_module:** The user pereference function, which returns a dictionary, is implemented in this module. User identifiers, ISBNs, book titles, authors, publication years, and corresponding ratings are all included in the user preference dictionary.
  
- **Similarity_module:** Implements five functions, each of which has a function for calculating user and book similarity. These three parameters, the user preference dictionary, two user ids, and the ISBN of the book, are accepted by each of these functions. The services will seek up books that both users have frequently rated before returning a similarity score between the two users based on these frequently rated books. It also include a function for comparing similarity between two books in addition to computing similarity between users.
  
- **Recommendation_module:** A program that makes book recommendations to users based on their reading tastes and history. The algorithms consider things like the user's prior ratings of books, their preferred authors and genres, and the ratings and reviews of other users who share their reading tastes.
   
- **Test_module:** A test or entry module with functionality for user inputs such user ids, ISBNs, etc. The module offers a text-based menu functionality for using your system, as well as the ability to show how similar a target user is to any other user in the dataset. Users ought to be able to query similarity between a target book and another book as well. Finally, the module enables users to terminate the program whenever they are finished with

