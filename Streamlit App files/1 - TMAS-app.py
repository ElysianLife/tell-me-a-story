#To run this script: open terminal and conda activate stream
#Then navigate to folder of file
#Then streamlit run TMAS-app.py
import streamlit as st
import numpy as np 
import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Title of app:
st.title('Tell Me a Story...')

"""
### :book: A Content-Based Children's Book Recommender :book:
-----
"""

#Setting the cache before loading data
@st.cache

#loading in all books         
def load_data(nrows):
    books = pd.read_csv('data/books.csv', nrows=nrows)
    return books

books = load_data(10981)

"""
Select one of your child's favourite books from the drop down list below and TMAS will recommend some similar titles for you to try out.
"""

#Creating the simple selectbox and giving the dropdown options to choose from name column 
option = st.selectbox(' ', books['name'].sort_values())

':green_book: That\'s a good one! :green_book:'  



#start of content recommender section
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 

#remove english stop words like the, and, if, a, etc. 
ENGLISH_STOP_WORDS = stopwords.words('english')
stemmer = nltk.stem.PorterStemmer()

def my_tokenizer(sentence):
    for punctuation_mark in string.punctuation:
        # Remove punctuation and re-set to lower case
        sentence = sentence.replace(punctuation_mark,'').lower() #includes !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~             
    # split sentence into words
    listofwords = sentence.split(' ')
    listofstemmed_words = []     
    # Remove stopwords and any tokens that are just empty strings
    for word in listofwords:
        if (not word in ENGLISH_STOP_WORDS) and (word!='') and (len(word)>2):
            # Stem words
            stemmed_word = stemmer.stem(word)
            listofstemmed_words.append(stemmed_word)
    return listofstemmed_words

#Need this helper function to look up a book TFIDF by its name.
def get_book_by_name(name, tfidf_scores, keys):
    row_id = keys[name]
    row = tfidf_scores[row_id,:]
    return row

#Instantiating the TFIDF Vectorizer
vectorizer = TfidfVectorizer(stop_words = "english", min_df=5, tokenizer=my_tokenizer)

index = 0
keys = {}
df_descriptions = books[['name','description', 'is_preschooler']]

#for user ratings (set up)
for book in df_descriptions.itertuples() :
    key = book[1]
    keys[key] = index
    index += 1

#Fit the vectorizer to the data
vectorizer.fit(df_descriptions['description'].fillna(''))

#Transform the data
tfidf_scores = vectorizer.transform(df_descriptions['description'].fillna(''))

def content_recommender(name, is_preschooler, tfidf_scores, bookdf=df_descriptions) :
    
    if is_preschooler==True:
        bookdf = bookdf[bookdf['is_preschooler']== 1]
    else: 
        bookdf = bookdf[bookdf['is_preschooler']== 0]
        
    #Store the results in this DF
    similar_books = pd.DataFrame(columns = ["name","similarity"] )
    
    #The book we are finding books similar to
    book_1 = get_book_by_name(name, tfidf_scores, keys)
    
    #Go through ALL the books
    for book in bookdf['name'] :
                
        #Find the similarity of the two books
        book_2 = get_book_by_name(book,tfidf_scores,keys)
        similarity = cosine_similarity(book_1,book_2)
        similar_books.loc[len(similar_books)] = [book, similarity[0][0]]

    return similar_books.sort_values(by=['similarity'],ascending=False)[1:10]

similar_books = content_recommender(option, True, tfidf_scores)

#need a trigger to start the recommender?
if st.button('Show me Similar Books'):
    """
    -----
    #### Titles Recommended for you:####
    """
    similar_books.sort_values(by=['similarity'],ascending=False)[1:10]

"""
-----
"""
"Want to see the the entire dataframe behind TMAS?"
if st.checkbox('Give me the whole library!'):
    st.write(books)