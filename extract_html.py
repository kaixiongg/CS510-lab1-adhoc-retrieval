# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:21:57 2021

@author: 27183
"""

from bs4 import BeautifulSoup
import urllib
import re
import os         
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_p(file):
    return
    
def clean_file(file):
     return

file_name_pre = "/UIUC/CS510/CS510-lab/code/diabetes_cleaned/"
origin_name_pre = "/UIUC/CS510/CS510-lab/code/www.diabetes.org.uk/"
all_files = os.listdir("/UIUC/CS510/CS510-lab/code/www.diabetes.org.uk") 

stop_words = set(stopwords.words('english'))
i = 0
for file in all_files:
    
    f = open(origin_name_pre + file, encoding='utf8')
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    
    canonical = soup.find('link', {'rel': 'canonical'})
    
    table = soup.findAll('p')
    i += 1
    file_name = file_name_pre + str(i) +".txt"
    outF = open(file_name,"w", encoding='utf8')
    
    # hard code first line as URL
    if canonical and canonical['href']:
        print(canonical['href'])
        outF.write(canonical['href'])
        outF.write(" ")
        
    for x in table:
       #print (x.text)
       cur_text = x.text.lower()
       # clean punctation
       cur_text = re.sub(r'\d+', '', cur_text)

       cur_text = cur_text.translate(str.maketrans('', '', string.punctuation))
       cur_text = cur_text.strip()

       tokens = word_tokenize(cur_text)
       cur_text = [i for i in tokens if not i in stop_words]
       cur_text = [character for character in cur_text if character.isalnum()]
       outF.write(str(" ".join(cur_text)))
       outF.write(" ")
    outF.close()













