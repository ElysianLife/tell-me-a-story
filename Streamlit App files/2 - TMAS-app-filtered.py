#To run this script: open terminal and conda activate stream
#Then navigate to folder of file
#Then streamlit run TMAS-app.py
import streamlit as st
import numpy as np 
import pandas as pd
import time

#Title of app:
st.title('Tell Me a Story...')

"""
### :book: A Content-Based Children's Book Recommender :book:
-----
"""

#Setting the cache before loading data
@st.cache

#Loading in and cleaning the data

#Originally loaded in a single file "books.csv" (10,980 rows)

#loading in infant/toddler books         
def load_inf_data(nrows):
    infbooks = pd.read_csv('data/infbooks.csv', nrows=nrows)
    return infbooks
infbooks = load_inf_data(2961)

#loading preschooler books
def load_preschool_data(nrows):
    preschoolbooks = pd.read_csv('data/preschoolbooks.csv', nrows=nrows)
    return preschoolbooks
preschoolbooks = load_preschool_data(7429)


"""
Select one of your child's favourite books from the dropdown list below and TMAS will recommend some similar titles for you to try out.
"""
#Creating the simple selectbox and giving the dropdown options to choose from name column (THIS ONE WORKS PERFECTLY)
#option = st.selectbox(
#   '',
#    books['name'])

#Creating more complex selectbox with filters for the two age groups

#set up radio buttons to select age group
agegroup = st.radio('What age is your child?', ('0-2 years old', '3+ years old') )

#create function to change book names in selectbox depending on agegroup filter option
def bookselections (agegroup):
    if (agegroup == '0-2 years old'):
        option1 = st.selectbox('', infbooks['name'])
        return option1
    'You selected: :green_book:', option1 , ":green_book: That's a good one! Now creating your recommendations list..."

    if (agegroup == '3+ years old'):
        option2 = st.selectbox('', preschoolbooks['name'])
        return option2
    'You selected: :blue_book:', option2 , ":blue_book: That's a good one! Now creating your recommendations list..."

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

"...your recommendations list is complete - get your library card ready!"


"""
-----
#### Titles Recommended for you:####
"""
# To calc cosine distance
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df_descriptions = books[['name','description', 'is_preschooler']]
df_descriptions.head(10)

#create tokenizer function to remove punctuation, split sentence, stem words, and remove stopwords
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

#for user ratings (set up)
for book in df_descriptions.itertuples() :
    key = book[1]
    keys[key] = index
    index += 1

#Fit the vectorizer to the data
vectorizer.fit(df_descriptions['description'].fillna(''))

#Transform the data
tfidf_scores = vectorizer.transform(df_descriptions['description'].fillna(''))

def content_recommender(name, tfidf_scores, book) :
    if is_preschooler==True:
        books = books['is_preschooler'== 1]
    else: 
        books = books['is_preschooler'==0]
        
    #Store the results in this DF
    similar_books = pd.DataFrame(columns = ["name","similarity"] )
    
    #The book we are finding books similar to
    book_1 = get_book_by_name(name, tfidf_scores, keys)
    
    #Go through ALL the books
    for book in books['name'] :
                
        #Find the similarity of the two books
        book_2 = get_book_by_name(book,tfidf_scores,keys)
        similarity = cosine_similarity(book_1,book_2)
        similar_books.loc[len(similar_books)] = [book, similarity[0][0]]

    return similar_books.sort_values(by=['similarity'],ascending=False)[1:]

similar_books = content_recommender("the boo boo book", tfidf_scores, books)
similar_books.head(5)
