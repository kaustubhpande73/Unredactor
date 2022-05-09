import pandas as pd
import re
import unredactor
from unredactor import get_data



df=get_data('unredactor.tsv')
dat1=df['redacted_text']
dat2=df['names']
def process():
  
    a = []
    label = []
#     label,a = process(df['redacted_text'],df['names'])
    for i in dat2.values:
        i=re.sub(r"can't"," can not",i)
        i=re.sub(r'n\'t',' not',str(i))
        i=re.sub("n\'t","not",i)
#         i=re.sub(r'[$-_@.&+]','',i) 
        i=re.sub(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*','',i)
        i=re.sub("\'m"," am",i)
        i = i.replace('<br>','')
        i = i.replace('</br>','')
        i = i.replace('-',' ')
        i = i.replace('?','')
        i = i.replace('!','')
        i = i.replace('.','')
        i = i.replace(',','')
        i = i.replace(')|(','')
#         i = ' '.join(e for e in i.split())    
        a.append(i)
    for j in dat1.values: 
        j=re.sub("\'s"," ",str(j))
        j=j.replace('.','')
        label.append(j)
    return a,label 
    assert a,label != None
#     assert len(processed)!=0  
