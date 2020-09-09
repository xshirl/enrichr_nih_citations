# Pubmed NIH grants of articles citing Enrichr articles

1. Article with pubmed id = 27141961
2. Article wtih pubmed id = 23586463

Goal of project is to find all articles that cites these two articles, and extract all of their NIH grants.
Then, plot the top ten highest frequencies of NIH institutions.

I did this by using the Pubmed API to find all articles citing these two articles. Then I use regex to find all NIH grants. Then I made a dictionary with the NIH institution as key and frequency as value. Then, I sorted these frequencies by most to least and plotted top ten.
