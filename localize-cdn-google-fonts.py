#This script basically takes a css folder (usually for a google font) containing a bunch of links to a bunch of fonts,
#downloads these fonts, and changes the reference to the local files instead of the CDN.

#To use, make sure the script is in the same location as the css file, and run it with the filename.

import os

def getName(line):
    name = ""
    if ("local('" in line):
        start = line.rindex("local('") + 7
        end = line[start:].index("'") + start
        name = line[start: end]
    return name

def getFormat(line):
    fformat = ""
    if ("format('" in line):
        start = line.index("format('") + 8
        end = line[start:].index("'") + start
        fformat = line[start:end]
    return fformat

def getUrl(line):
    start = line.index("url(") + 4
    end = line[start:].index(")") + start
    return line[start:end]
    

file = open("filename.css", "r+")

lines = file.readlines()

for i in range (0,len(lines)):
    if ("src" in lines[i] and lines[i].find("src") == 2):
        name = getName(lines[i])
        fformat = getFormat(lines[i])
        fullName = name+"."+fformat
        url = getUrl(lines[i])
        command = "wget -O "+fullName+" "+url
        newLine = "  src: url("+fullName+") format('"+fformat+"');\n"
        os.system(command)
        lines[i] = newLine
file.seek(0)
file.truncate()
file.writelines(lines)
file.close()
