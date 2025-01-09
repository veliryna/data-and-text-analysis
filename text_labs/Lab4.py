'''Файл science.csv. В якості текстової моделі використати TD-IDF.
Виконати класифікацію за допомогою алгоритмів наївний байєсів
класифікатор та логістичну регресію, порівняти їх точність.
Спробувати покращити модель логістичної регресії за допомогою
GridSearchCV.'''

import pandas as pd
import numpy as np
import nltk
import re

data = pd.read_csv('science.csv')
data_df = pd.DataFrame({'Article': data['Comment'], 'Target Name': data['Topic']})

def preproc_doc(doc):
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words('english')
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    tokens = wpt.tokenize(doc)
    filtered_tokens = [token for token in tokens if token
    not in stop_words]
    doc = ' '.join(filtered_tokens)
    return doc

preproc_corpus = np.vectorize(preproc_doc)
p_corpus = preproc_corpus(data_df['Article'])
data_df['Clean Article'] = p_corpus
labels = data_df['Target Name']
ids = []
for elem in labels:
    if elem == 'Biology': ids.append(1)
    elif elem == 'Chemistry': ids.append(2)
    elif elem == 'Physics': ids.append(3)
    else: ids.append(" ")
data_df['Target Label'] = pd.Series(ids)
print(data_df.head(10))

data_df = data_df.replace(r'^(\s?)+$', np.nan, regex=True)
data_df.info()
data_df = data_df.dropna().reset_index(drop=True)
data_df.info()
print()

from sklearn.model_selection import train_test_split
X = data_df['Clean Article']
y = data_df['Target Name']
train_corpus, test_corpus, train_labels, test_labels = train_test_split(np.array(X), np.array(y), test_size=0.3, random_state=0)

from collections import Counter
trd = dict(Counter(train_labels))
tsd = dict(Counter(test_labels))
print(pd.DataFrame([[key, trd[key],
tsd[key]] for key in trd],columns=
['Target Label', 'Train Count', 'Test Count']).sort_values(by=['Train Count', 'Test Count'], ascending=False))



from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_score

tt = TfidfVectorizer(use_idf=True, min_df=0.0, max_df=1.0)
tt_train_features = tt.fit_transform(train_corpus)
tt_test_features = tt.transform(test_corpus)

mnb = MultinomialNB(alpha=1)
mnb.fit(tt_train_features, train_labels)
mnb_bow_tt_scores = cross_val_score(mnb, tt_train_features, train_labels, cv=5)
mnb_bow_tt_mean_score = np.mean(mnb_bow_tt_scores)
print("\nNaive Bayes: ")
print('Accuracy (5-fold):', mnb_bow_tt_scores)
print('Mean Accuracy:', mnb_bow_tt_mean_score)
mnb_bow_test_score = mnb.score(tt_test_features, test_labels)
print('Test Accuracy:', mnb_bow_test_score)
print()

lr = LogisticRegression(penalty='l2', max_iter=200, C=1, random_state=0)
lr.fit(tt_train_features, train_labels)
lr_bow_tt_scores = cross_val_score(lr, tt_train_features, train_labels, cv=5)
lr_bow_tt_mean_score = np.mean(lr_bow_tt_scores)
print("Logistic Regression: ")
print('Accuracy (5-fold):', lr_bow_tt_scores)
print('Mean Accuracy:', lr_bow_tt_mean_score)
lr_bow_test_score = lr.score(tt_test_features, test_labels)
print('Test Accuracy:', lr_bow_test_score)
print()


from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
lr_pipeline = Pipeline(steps=[('tfidf', TfidfVectorizer()),('model', LogisticRegression())])
param_grid = {'tfidf__ngram_range': [(1, 2)], 'model__C':[5], 'model__penalty':['l2'], 'model__max_iter':[500]}
gs_lr = GridSearchCV(lr_pipeline, param_grid, cv=5, verbose=2)
gs_lr = gs_lr.fit(train_corpus, train_labels)
best_lr_test_score = gs_lr.score(test_corpus, test_labels)
print('Test Accuracy with GridSearchCV for LR:', best_lr_test_score)

#print("Best: {0}, using {1}".format(gs_lr.best_score_, gs_lr.best_params_))