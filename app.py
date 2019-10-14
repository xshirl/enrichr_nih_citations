from urllib.request import urlopen
import xmltodict
import requests
import re
from bs4 import BeautifulSoup
import time
import random


file = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id=27141961')
data = file.read()
file.close()

data = xmltodict.parse(data)
ids = []
for id in data["eLinkResult"]["LinkSet"]["LinkSetDb"]["Link"]:
    for key, value in id.items():
        ids.append(value)

print(ids)
# print(len(ids))

# file2 = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pmc_refs&id=23586463&tool=my_tool&email=my_email@example.com')
file2 = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id=23586463')
data2 = file2.read()
file2.close()

data2 = xmltodict.parse(data2)

ids2 = []

for id2 in data2["eLinkResult"]["LinkSet"]["LinkSetDb"]["Link"]:
    for key2, value2 in id2.items():
        ids2.append(value2)

# print(ids2)
# print(len(ids2))





total = []
for id in ids2:
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
    total.append(result)
print(total)
    
# site3 = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31537853"
# response = requests.get(site3)
# html = response.text
# # print(html)
# start = re.findall("[A-Z][0-9][0-9].*NIH", html)
# result = []
# for i in start:
#     if i[3] == " ":
#         two = i[4:6]
#         result.append(two)
#     else:
#         two = i[3:5]
#         result.append(two)
# print(result)

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