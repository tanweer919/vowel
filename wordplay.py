fin=open('words.txt')
c=0
for line in fin:
    word=line.strip()
    if(len(word)>=20):
        print(word)
        
        
