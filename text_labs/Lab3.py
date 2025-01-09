'''Зчитати файл doc14. Вважати кожен рядок окремим документом
корпусу. Виконати попередню обробку корпусу.
1) Представити корпус як модель «Сумка слів». Вивести вектор для
слова juice.
2) Представити корпус як модель TD-IDF. Спробувати
кластеризувати документи за допомогою ієрархічної
агломераційної кластеризації.
3) Представити корпус як модель FastText. Знайти подібні слова до
слів fruit, chancellor.'''


import re
import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

with open('doc14.txt', 'r') as file:
    documents = file.readlines()

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
p_corpus = preproc_corpus(documents)
print(p_corpus)

labels = ['juice', 'juice', 'politics', 'juice',
'politics', 'juice']
corpus_df = pd.DataFrame({'Document': p_corpus, 'Category': labels})

'''Bag Of Words model'''
cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(p_corpus)
cv_matrix = cv_matrix.toarray()
vocab = cv.get_feature_names_out()
print(pd.DataFrame(cv_matrix, columns=vocab))
juice_index = np.where(vocab == 'juice')[0][0]
vector = [elem[juice_index] for elem in cv_matrix]
print("Vector for a word 'juice': ", vector)


'''TF-IDF model and clustering'''
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfTransformer
tt = TfidfTransformer(norm='l2', use_idf=True)
tt_matrix = tt.fit_transform(cv_matrix)
tt_matrix = tt_matrix.toarray()
vocab = cv.get_feature_names_out()
print(pd.DataFrame(np.round(tt_matrix, 2), columns=vocab))
clustering_model = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
clustering_model.fit(tt_matrix)
corpus_df['agg_cluster'] = clustering_model.labels_
print(corpus_df)
print()


'''FastText model and similar words'''
from gensim.models.fasttext import FastText
wpt = nltk.WordPunctTokenizer()
tokenized_corpus = [wpt.tokenize(document) for document in p_corpus]
ft_model = FastText(tokenized_corpus, vector_size=100,
window=50, min_count=5,sample=1e-3, sg=1)
similar_words = {search_term: [item[0] for item in
ft_model.wv.most_similar([search_term], topn=5)]
for search_term in ['fruit', 'chancellor']}
print("Similar words to 'fruit' and 'chancellor': ", similar_words)

