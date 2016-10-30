fin=open('words.txt')
c=0
for line in fin:
    word=line.strip()
    if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
        print(word)
        c=c+1
print(c)