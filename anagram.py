fin=open("words.txt")
d=dict()
for l in fin:
    word=l.strip()
    t=tuple(word)
    if t not in d:
        d[t]=[word]
    else:
        d[t].append(word)
print(d)