import re

file = open("text3.txt", "r")
text = file.read()
file.close()

print("Slice of text 3:")
print()
slice = text[56:304]
print(slice)
print()
print("Number of occurences of letter 's' : ", slice.count("s"))
print("Index of first letter 's' : ", slice.find("s"))
print("Starting index of word 'out' : ", slice.index("out"))
print()
print("Uppercase string : ", slice.upper())
print()
print("Lowercase string : ", slice.lower())
print()
print("Capitalized string : ", slice.capitalize())
print()
print("Titled string : ", slice.title())
print()
print("Join method : ", "!".join(slice))
print()

print("Method text.isalnum(): ", slice.isalnum())
print("Method text.isalpha(): ", slice.isalpha())
print("Method text.isdigit(): ", slice.isdigit())
print("Method text.istitle(): ", slice.istitle())
print("Method text.isspace(): ", slice.isspace())
print("Method text.endswith(): ", slice.endswith(' '))
print("Method text.startswith(): ", slice.startswith('a'))
print()

print("Method text.replace(): ", slice.replace("the", "ABC"))
print()
print("Method text.split(): ", slice.split('o'))
print()


'''Regular expression'''
my_regex = re.compile(r'\s\d+[a-z.]')
housenumbers = re.findall(my_regex, text)
onlynumbers = []
for num in housenumbers:
    if num[-1].isalnum() == False:
        num = num[:-1]
    onlynumbers.append(num[1:])
print("House Numbers: ", onlynumbers)
print()
for i in range(0, len(onlynumbers)):
    text = text.replace(onlynumbers[i], onlynumbers[i][0]+"&")
print(text)