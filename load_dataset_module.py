# Import libraries
import glob
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def load_dataset(dirpath):   
#     Read directory
    files = glob.glob(dirpath + "/*.csv")
#     print(f"Total datasets: {len(files)}")
#     Load datasets    
    for file in files:
        if file == f"{dirpath}/BX-Users.csv":
            df_user =  pd.read_csv(file, sep = ";", encoding='latin-1', on_bad_lines="skip")
        elif file == f"{dirpath}/BX-Books.csv":
            df_book =  pd.read_csv(file, sep = ";", encoding='latin-1', on_bad_lines="skip")
        else:
            df_rating =  pd.read_csv(file, sep = ";", encoding='latin-1', on_bad_lines="skip")
            
#            Merge dataFrames 
    df_temp = pd.merge(df_user, df_rating, on = "User-ID", how = "inner")
    df = pd.merge(df_temp, df_book, on = "ISBN", how = "inner")
    user_preference =  df[["User-ID", "ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Book-Rating"]]    

    return user_preference