'''
Library for input and output 
'''
import json

def saveOutput(fileName, jsonDic):
    with open(fileName, "w") as filehandle:
        json.dump(jsonDic, filehandle)

def readInput(fileName, jsonDic):
    with open(fileName) as filehandle:
        temp = json.load(filehandle)
    return temp

