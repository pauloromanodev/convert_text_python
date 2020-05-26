import re
from html import unescape

def limpa_caracteres(text):
    return re.sub('[^A-Za-z0-9áéíóúÁÉÍÓÚãõÃÕàèìòùÀÈÌÒÙçÇüÜâêôÂÊÔ]+', ' ', text)

f = open("C:\\Users\\pcpereira\\Documents\\python\\arquivo_original.txt", "r", encoding="utf8")

contents = f.read()

contents = unescape(contents) #remove tags html
contents = limpa_caracteres(contents) #remove caracteres especiais, limpa espaços em brancos, linhas, etc

#print(contents)

file = open("C:\\Users\\pcpereira\\Documents\\python\\arquivo_final.txt", "w", encoding="utf8")

file.write(contents.lower()) #escreve no arquivo e coloca tudo em minúsculo

file.close()