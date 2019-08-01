dictionary = {
    "malawa":"weird",
    "booboo":"mistake",
    "Yumma":"what-the-heck"
}
#print(dictionary["malawa"])
#print(dictionary["booboo"])
#print(dictionary[""])

# print(dictionary.values())

sentence = "This is so malawa"
wordList = sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary: # same as if word in dictionary;
        print(dictionary[word])

sentence = "You guys did a booboo"
wordList = sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary: # same as if word in dictionary;
        print(dictionary[word])

sentence = "Yumma what are you doing"
wordList = sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary: # same as if word in dictionary;
        print(dictionary[word])