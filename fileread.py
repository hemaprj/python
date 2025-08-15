d_word={}
f=open("P:\\AI_Learn\\Hello\\poem.txt","r")
print(f)
for l in f:
    words=l.split()
    for word in words:
        if word in d_word:
            d_word[word]+=1
        else:
            d_word[word]=1

f.close()
print(d_word)

wordoccur=list(d_word.values())
maxcount=max(wordoccur)
print("Maxcount is " , maxcount)
print("Words with max occurances are:")
for k,v in d_word.items():
    if v==maxcount:
        print(k + " Count " + str(v))
