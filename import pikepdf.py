import pikepdf
import os
from PyPDF2 import PdfFileReader
from tqdm import tqdm
filename = "D:/rootchen/target.pdf" #pdf文件路径
wordlist = "D:/rootchen/密码字典.txt" #密码字典路径
n_words = len(list(open(wordlist, 'rb')))
fp = open(filename, "rb+")
pdfFile = PdfFileReader(fp)
filepath, tempfilename = os.path.split(filename)
with open(wordlist, "rb") as wordlist:
    if pdfFile.isEncrypted:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                pdf = pikepdf.open(filename, password=word.strip())
            except:
                continue
            else:
                print("[+] Password found:", word.decode().strip())
                exit(0)
        print("[!] Password not found, try other wordlist!")
