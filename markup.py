import re

dic = {"1#": "#", "2#": "##", "3#": "###", "4#": "####", "5#": "#####",
       "6#": "######", "*": "**", "/": "*", "~": "~~", "_": "__", "--": "----"} # {"Better Markdown": "Markdown"}

def replaceText(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    print(text)

fileName = input("Enter name of file to read (txt format) : ")
filename = filename + ".txt"
readFile = open(fileName, "r")

string = readFile.read()
splitString = string.split("\n")

for i in range(string.count("\n") + 1):
    replaceText(splitString[i], dic)

readFile.close()

end = input("Press enter to end the program: ")


