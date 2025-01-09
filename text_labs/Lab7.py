import spacy
from spacy.matcher import Matcher

file = open("text3.txt", "r")
text = file.read()
file.close()

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
matcher = Matcher(nlp.vocab)
print("Found House Numbers:")
pattern1 = [{"IS_DIGIT": True},{"TEXT": "."}]
pattern2 = [{"TEXT": {"REGEX": "\d+[a-z]"}}]
housenumbers = []

matcher.add("findHouseNumber1", [pattern1])
matches = matcher(doc)
for match_id, start, end in matches:
    m_span = doc[start:end]
    print(start, end, m_span.text)
    housenumbers.append(m_span.text[:-1])

matcher.remove("findHouseNumber1")
matcher.add("findHouseNumber2", [pattern2])
matches = matcher(doc)
for match_id, start, end in matches:
    m_span = doc[start:end]
    print(start, end, m_span.text)
    housenumbers.append(m_span.text)
print()

for i in range(0, len(housenumbers)):
    text = text.replace(housenumbers[i], housenumbers[i][0]+"&")
print(text)
print()

'''а) Знайти та вивести всі слова з тексту, які не є стоп-
словами. б) Знайти та вивести всі прикметники, які присутні у тексті.
в) Знайти та вивести організації та дати, які присутні у тексті.'''

print("Second task:")
file = open("lab7-1.txt", "r")
text = file.read()
file.close()

doc = nlp(text)
print("Not stop-words:")
for token in doc:
    if token.is_stop is not True and token.text.isalpha():
        print(token)
print()
print("Adjectives from text:")
for token in doc:
    if token.pos_ == "ADJ":
        print(token)
print()

ner_tagged = [(word.text, word.ent_type_) for word in doc]
named_entities = []
temp_entity_name = ""
temp_named_entity = None
for term, tag in ner_tagged:
    if tag:
        temp_entity_name = ' '.join([temp_entity_name, term]).strip()
        temp_named_entity = (temp_entity_name, tag)
    else:
        if temp_named_entity:
            named_entities.append(temp_named_entity)
            temp_entity_name = ""
            temp_named_entity = None

print("Dates in text:")
for tupl in named_entities:
    if tupl[1] == "DATE":
        print(tupl[0])
print()
print("Organizations in text:")
for tupl in named_entities:
    if tupl[1] == "ORG":
        print(tupl[0])