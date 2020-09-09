from urllib.request import urlopen
import xmltodict
import requests
import re
import time
import random

# first article
file = urlopen(
    'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id=27141961')
data = file.read()
file.close()

# convert xml to dictionary
data = xmltodict.parse(data)
ids = []
for id in data["eLinkResult"]["LinkSet"]["LinkSetDb"]["Link"]:
    for key, value in id.items():
        ids.append(value)
# extract ids of pubmed articles
print(ids)
# print(len(ids))

# second article
file2 = urlopen(
    'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id=23586463')
data2 = file2.read()
file2.close()

# convert xml to dictionary
data2 = xmltodict.parse(data2)

ids2 = []

for id2 in data2["eLinkResult"]["LinkSet"]["LinkSetDb"]["Link"]:
    for key2, value2 in id2.items():
        ids2.append(value2)
# extract ids of articles citing this article
# print(ids2)
# print(len(ids2))


total = []
for id in ids2:
    temp = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={}"
    url = temp.format(id)
    response = requests.get(url)
    time.sleep(2)
    html = response.text
    # find all NIH grants starting with two letters and ending with NIH
    start = re.findall("[A-Z][A-Z].*NIH", html)
    result = []
    for i in start:
        two = i[:2]
        result.append(two)
    print(result)
    total.append(result)
print(total)


total2 = []
for id in ids:
    temp = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={}"
    url = temp.format(id)
    response = requests.get(url)
    time.sleep(2)
    html = response.text
    start = re.findall("[A-Z][A-Z].*NIH", html)
    result = []
    for i in start:
        two = i[:2]
        result.append(two)
    print(result)
    total2.append(result)
print(total2)
