fin=open('words.txt')
c=0
for line in fin:
    word=line.strip()
    if ('a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word and 'y' not in word):
        print(word)
        c=c+1
print(c)