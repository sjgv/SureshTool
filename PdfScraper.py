import itertools
from tika import parser
#from PyPDF2 import PdfFileReader
import random
import string
import json
import os

'''
Relates index of listOfVectors items to a numeric key in a dictionary returned.
Dictionary contains numeric key reated to a list of numeric keys and similarity
an item of listOfVectors looks like: <int,<int>list> (indexNumberForPaths,vector)
'''
def compareHashVectors(listOfVectors):
    matlabDic = {}
    comparisonDic = {}
    for a,b in itertools.combinations(listOfVectors, 2):
            zum = 0
            #k = listOfVectors.index(a)
            #v = listOfVectors.index(b)
            for el in a[1]:
                if el in b[1]:
                    zum +=1

            try:
                matlabDic[a[0]].append((b[0],zum/len(a[1])))
            except:
                matlabDic[a[0]] = []
                matlabDic[a[0]].append((b[0],zum/len(a[1])))
              

            try:
                comparisonDic[a[0]].append((b[0],zum/len(a[1])))
                ##put b 
                try:
                    comparisonDic[b[0]].append((a[0], zum/len(a[1])))
                except:
                    comparisonDic[b[0]] = []
                    comparisonDic[b[0]].append((a[0], zum/len(a[1])))
            except:
                comparisonDic[a[0]] = []
                comparisonDic[a[0]].append((b[0],zum/len(a[1])))
                ##put b 
                try:
                    comparisonDic[b[0]].append((a[0], zum/len(a[1])))
                except:
                    comparisonDic[b[0]] = []
                    comparisonDic[b[0]].append((a[0], zum/len(a[1])))

    return (comparisonDic,matlabDic)


#########################################
# MIN HASH FN'S
#########################################
def get_hash_fn(num):
    salts = []
    for i in range(0, num):
        rand = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(5)])
        salts.append(rand)
    return salts

def hashify(some_set, salts):
    meen = []
    for i in range(0,len(salts)):
        minimum = 100000000000000000
        for element in some_set:
            s = salts[i] + element
            digest = hash(s)
            if digest < minimum:
                minimum = digest
        meen.append(minimum)
    return meen

#########################################
# K-GRAMS 
#########################################

def getKGrams(text, length):
    counter = 0
    nu_window_length = length
    kgrams = []
    u_kgrams = set([])
    temp = []
    for i in range(0, len(text)):
        if i < len(text)-length:
            while(counter < nu_window_length):
                #check if it's a whitespace char
                if text[i+counter].isspace():
                    counter += 1
                    nu_window_length += 1
                    #check if at the end of body text
                    if (i+nu_window_length > len(text)):
                        break
                else: 
                    temp.append(text[i+counter])
                    counter += 1
            u_kgrams.add(''.join(temp))
            temp = []
            counter = 0
            nu_window_length = length
    return(u_kgrams)

#########################################
# ACCESSOR FN'S
#########################################

def getAllText(path):
    txt = parser.from_file(path)
    #print(txt['metadata'])
    return txt['content']

'''
Input: a folder path
Output: text

def getFirstPage(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        firstPage = pdf.getPage(0)
        secondPage = pdf.getPage(1)
        text = firstPage.extractText() + secondPage.extractText()
        print("----------PDF--------------------")
        print(path)
        print(text)
        print("======================================")
        return text
'''

'''
Iterate through directories to
check for .pdf files 
'''
def getFilePaths(dir):
    paths = []
    listOfDirs = os.listdir(dir)
    #For every dir in this path
    for d in listOfDirs:
        fullpath = os.path.join(dir, d)
        #For file in directory
        for f in os.listdir(fullpath):
            if f.endswith(".pdf"):
                paths.append((fullpath+'/'+f, f))
    return paths


