fin=open("words.txt")
a=[]
for line in fin:
    word=line.strip()
    for l in word:
        a.append(l)
print(a)
        