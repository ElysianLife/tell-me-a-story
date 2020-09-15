README.txt

Tell Me a Story (TMAS) - A Content-Based Children's Book Recommender
TMAS is a content-based child book recommender system that takes in a book input by the user and recommends similar books based on similarities in the book description text using natural language processing (NLP); ranked by similarity scores. 

Documents in this project folder (excluding this README) include:

Project Summary Documents:
1 - ElyseRenouf_Capstone_Findings.pdf - This is the final report that summarizes the project
2 - ElyseRenouf_Capstone_Presentation.pdf - This was the capstone slide deck as presented to the data science cohort in July 2020
3 - TMAS Demo.pdf - This was the slide deck as presented during the initial TMAS demo video

The process in Jupyter Notebooks:
4 - Loading_Merging_Datasets.ipynb
5 - Cleaning & EDA.ipynb
6 - Vectorizing & Modelling.ipynb

Then there are two versions of the Streamlit app:
7 - TMAS-app.py - This is version one of the TMAS StreamLit app
8 - TMAS-app-filtered.py - This is version two of the TMAS StreamLit app is still a work in progress

The data files included in the data folder are:
9 - RAW DATA: Note: this raw data folder could not be included in SYNAPSE submission due to file size please see original Kaggle dataset at: https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m
10 - kidsbooks.csv - csv of all merged kids books .csv files, before cleaning
11 - master.csv - csv of cleaned, finalised kids books data and all columns 
12 - books.csv - csv of cleaned kids books data with only columns needed for recommender
13 - infbooks.csv - books filtered by is_preschooler column as 0 (30+ pages for kids aged 0-2 years old)
14 - preschoolbooks.csv - books filtered by is_preschooler column as 1 (31-38 pages for kids aged 3-6 years old)