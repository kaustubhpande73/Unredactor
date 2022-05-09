import pandas as pd
import re
import warnings
from warnings import filterwarnings
filterwarnings("ignore")
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import tree
import scipy
from scipy.sparse import hstack
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

def get_data(file): 
        df = pd.read_csv(file,sep='\t',header=None,error_bad_lines=False,names=['username','file_type','names','redacted_text'])
        return df

df=get_data('unredactor.tsv')

def process(dat1,dat2):
    a = []
    label = []
    
    
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

label,a = process(df['redacted_text'],df['names'])
# label = process(df['names'])
df['clean_text'] = a
df['redacted_names'] = label


del df['username']
del df['names']
del df['redacted_text']

def letter_count(data): #counts letters in redacted names
    b = data.str.len()
    return b

d = letter_count(df['redacted_names'])
df['letter_count'] = d

def space_count(data):#counts number of spaces in redacted names
    a=data.str.count('\s+')
#     a = df['letter_count']
    return a

c = space_count(df['redacted_names'])
df['space_count'] = c

training_df = df[df['file_type']=='training']

validation_df = df[df['file_type']=='validation']

testing_df = df[df['file_type']=='testing']

def split(data): # function for separating labels and main data
    y=data['redacted_names'].values
    y = pd.Series(y)
    X=data.drop(['redacted_names'],axis=1)
    return X,y

X_train,y_train = split(training_df)
X_val,y_val = split(validation_df)
X_test,y_test = split(testing_df)

y_train

def vect(data): 
    vectorizer=CountVectorizer(max_features=3000)
    data=vectorizer.fit_transform(data.values)
    return data

X_tr_text = vect(X_train['clean_text'])
X_val_text = vect(X_val['clean_text'])
X_test_text = vect(X_test['clean_text'])

def letter_features(d1):
#     v = CountVectorizer(ngram_range=(2,2),max_features=2000)
    X_let = d1.values
    X_let_train=X_let.reshape(-1,1)
    return X_let_train

X_let_train= letter_features(X_train['letter_count'])
X_let_validate = letter_features(X_val['letter_count'])
X_let_test = letter_features(X_test['letter_count'])

def space_features(d1):
#     vect = TfidfVectorizer()
    X_spc = d1.values
    X_spc_train=X_spc.reshape(-1,1)

    return X_spc_train

X_spc_train= space_features(X_train['space_count'])

X_spc_validate= space_features(X_val['space_count'])

X_spc_test= space_features(X_test['space_count'])

def merge(d1,d2,d3):
    data_stack= hstack((d1,d2,d3))
    data= data_stack.tocsr()
    return data

merge_train = merge(X_tr_text,X_let_train,X_spc_train)
merge_validate = merge(X_val_text,X_let_validate,X_spc_validate)
merge_test = merge(X_test_text, X_spc_test, X_spc_test)

df

def create_model(train_X,train_y):
    clf = KNeighborsClassifier()
    model = clf.fit(train_X,train_y)
    return model 

model = create_model(merge_train,y_train)

def prediction(model,train_X, validation_X, test_X):
    predict_y_train = model.predict(train_X)
    predict_y_val = model.predict(validation_X)
    predict_y_test = model.predict(test_X)
    return predict_y_train,predict_y_val,predict_y_test

predict_y_train,predict_y_val,predict_y_test = prediction(model,merge_train, merge_validate, merge_test)

def evaluate(model,predict_y_train,predict_y_val,y_train,y_val):
    train_precision_score = precision_score(y_train,predict_y_train,average='weighted')
    val_precision_score = precision_score(y_val,predict_y_val,average='weighted')
    train_recall_score = recall_score(y_train,predict_y_train,average='weighted')
    val_recall_score = recall_score(y_val,predict_y_val,average='weighted')
    train_f1_score = f1_score(y_train,predict_y_train,average='weighted')
    val_f1_score = f1_score(y_val,predict_y_val,average='weighted')
    return train_precision_score, val_precision_score, train_recall_score, val_recall_score, train_f1_score, val_f1_score

train_precision_score, val_precision_score, train_recall_score, val_recall_score, train_f1_score, val_f1_score = evaluate(model,predict_y_train,predict_y_val,y_train,y_val)

val_precision_score

train_precision_score

train_recall_score

val_recall_score

train_f1_score

val_f1_score

output = predict_y_test

output
