README.md

<h2> Tell Me a Story (TMAS) - A Content-Based Children's Book Recommender </h2>
TMAS is a content-based child book recommender system that takes in a book input by the user and recommends similar books based on similarities in the book description text using natural language processing (NLP); ranked by similarity scores. 
<br>
Documents in this project folder (excluding this README) include:
<br>
<h4> Project Summary Documents: </h4>
  <ul>
    <li> 1 - ElyseRenouf_Capstone_Findings.pdf - This is the final report that summarizes the project
    <li> 2 - ElyseRenouf_Capstone_Presentation.pdf - This was the capstone slide deck as presented to the data science cohort in July 2020
    <li> 3 - TMAS Demo.pdf - This was the slide deck as presented during the initial TMAS demo video
  </ul>

<h4> The process in Jupyter Notebooks: </h4>
  <ul>
    <li> 4 - Loading_Merging_Datasets.ipynb
    <li> 5 - Cleaning & EDA.ipynb
    <li> 6 - Vectorizing & Modelling.ipynb
  </ul>
  
<h4> Then there are two versions of the Streamlit app: </h4>
   <ul>
    <li> 7 - TMAS-app.py - This is version one of the TMAS StreamLit app where the user can select a book from the dropdown list to get reccommendations
    <li> 8 - TMAS-app-filtered.py - This is version two of the TMAS StreamLit app is still a work in progress to filter the book lists by age group
   </ul>

<h4> And Finally, the data files included in the data folder are: </h4>
  <ul>
    <li> 9 - RAW DATA: Note: this raw data folder could not be included in SYNAPSE submission due to file size please see the <a href="https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m" target="_blank">Original Kaggle Dataset</a>
    <li> 10 - kidsbooks.csv - csv of all merged kids books .csv files, before cleaning
    <li> 11 - master.csv - csv of cleaned, finalised kids books data and all columns 
    <li> 12 - books.csv - csv of cleaned kids books data with only columns needed for recommender
    <li> 13 - infbooks.csv - books filtered by is_preschooler column as 0 (30+ pages for kids aged 0-2 years old)
    <li> 14 - preschoolbooks.csv - books filtered by is_preschooler column as 1 (31-38 pages for kids aged 3-6 years old)
    <li> 15 - README_ENVS.txt - a document which details the packages imported to create the environment used to run my ipynb files (BASE) and the streamlit app (STREAM)
  </ul>
