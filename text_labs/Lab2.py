'''1. Зчитати файл text4. а) Порахувати кількість речень в тексті; б)
вивести 10 слів, які зустрічаються найчастіше; в) провести
лематизацію слів другого речення.
2. Використати корпус Brown, сьомий текст категорії adventure. а)
Видалити стоп-слова; б) Вивести 8 іменників, що зустрічаються
найчастіше.'''

import nltk
from nltk.tokenize import regexp_tokenize
from nltk.corpus import wordnet
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wlem = WordNetLemmatizer()

file = open("text4.txt", "r")
text = file.read()
file.close()

sentences = nltk.sent_tokenize(text)
print("The number of sentences in text: ", len(sentences))

tkn = nltk.word_tokenize(text)
words = [item for item in tkn if item.isalnum()]
freq = dict()
for i in words:
    freq[i] = freq.get(i, 0) + 1
wordsort = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
print("The 10 most frequent words: ", list(wordsort.keys())[0:10])
print()

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

second = sentences[1]
tokens=regexp_tokenize(second, pattern='\w+')
lemmatized=[]
for item in tokens:
    lemmatized.append(wlem.lemmatize(item, get_wordnet_pos(item)))
print("Lemmatized words of 2nd sentense: ", lemmatized)
print()

textid = brown.fileids(categories='adventure')[6]
words7 = brown.tagged_words(textid)
words7 = [(token.lower(), tag) for token, tag in words7]
cleanwords = [(word, tag) for word, tag in words7 if word not in stopwords.words('english')]

nouns = [(word, tag) for word, tag in cleanwords if
any(noun_tag in tag for noun_tag in ['NP', 'NN'])]
nouns_freq = nltk.FreqDist([word for word, tag in nouns])
print("8 most frequent nouns: ", nouns_freq.most_common(8))