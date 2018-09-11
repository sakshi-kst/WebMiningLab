from glob import glob

f1=open("input1.txt","w+")
f1.write("Corruption results in black money generation")
f1.close()
f2=open("input2.txt","w+")
f2.write("Excessive cash transactions result in non-payment of tax and creation of black money")
f2.close()
f3=open("input3.txt","w+")
f3.write("Black money is usually stored in high denomination currency")
f3.close()

def parsetexts(fileglob='input*.txt',recursive=True):
    texts,words={},set()
    for txtfile in glob(fileglob):
        with open(txtfile,'r') as f:
            for line in f:
                line=line.lower()
            txt=line.split()
            words|=set(txt)
            texts[txtfile.split('\\')[-1]]=txt
    return texts,words 
texts,words=parsetexts()

finvindex={word:set((txt,wrdindx)
                      for txt,wrds in texts.items()
                      for wrdindx in (i for i,w in enumerate(wrds) if word==w)
                      if word in wrds)
             for word in words}
    
f4=open("index.txt","w+")
for k,v in finvindex.items():
    f4.write(k)
    f4.write('\t\t[')
    count=0
    for item in sorted(v):
        count+=1
        if(count>1):
            f4.write(', ')
        f4.write(''.join('(\'%s\', %s)' % item))
    f4.write(']\n')
f4.close()
