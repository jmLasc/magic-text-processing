# magic-text-processing
CSCI2349 Semester Project: Group 9
Topic: Magic the Gathering cards

# Obtaining the Data

This project analyzes the properties of *Magic: The Gathering* Cards. Data was obtained from [Scryfall](https://scryfall.com/docs/api/bulk-data). 

In order to properly use the dataset, download "Oracle Cards" from the above hyperlink and drop it in the project folder. Rename this data file to "cards.json" in order to work with the code. It is too large to upload to github. 

# Repo Contents
`basic.ipynb`
- Commented notebook that uses json to extract the data and make initial cleaning steps. Defines a few essential functions for the other notebooks. 

`basic.py`
- Script version of `basic.ipynb` for imports.

`wordclouds.ipynb`
- Makes the wordclouds of the data. Creates them in the base directory, but you can skip the code and see them in the folder `wordclouds_pics`.

`ngrams_colloc_tfidf.ipynb`
- Finds the most frequent desired ngrams (presentation used 6grams)
- Finds bigram collocations and filters through some of the unuseful results
- Notably: also creates a text file for each card. If ran, you will have a folder, `cards`, that has each card saved as a txt file.
- Creates a tf-idf model with pandas and runs a few queries based on it

`word2vec.ipynb`
- Makes a w2v model of the data and runs a few queries.