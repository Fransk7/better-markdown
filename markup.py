import re

dic = {"1#": "#", "2#": "##", "3#": "###", "4#": "####", "5#": "#####",
       "6#": "######", "*": "**", "/": "*", "~": "~~", "_": "__"} # {"Better Markdown": "Markdown"}

def replaceText(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    print(text)

fileName = input("Enter name of file to read (include extension: \'.md\' or \'.txt\'): ")
readFile = open(fileName, "r")

string = readFile.read()
splitString = string.split("\n")

for i in range(string.count("\n") + 1):
    replaceText(splitString[i], dic)

readFile.close()

'''
1# = h1
2# = h2
3# = h3
4# = h4
5# = h5
6# = h6
* = bold
/ = italic
~ = strike
_ = underline
'''

