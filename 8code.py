import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

wordlist = "D:/rootchen/rockyou.txt" #密码字典路径
fileObject = open(wordlist, "r", errors="ignore")
newFile = "D:/rootchen/8code.txt"
f = open(newFile, "a+")

for line in fileObject:
    if 9 == len(line) and is_number(line[:8]) :
        f.write(line)
    else:
        continue    
