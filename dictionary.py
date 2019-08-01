dictionary = {
    "wanker":"jerk",
    "knackered":"tired",
    "chuffed":"pleased"
}
#print(dictionary["wanker"])
#print(dictionary["knackered"])
#print(dictionary["chuffed"])

# print(dictionary.values())

sentence = "This is a sentence wanker ."
wordList = sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary: # same as if word in dictionary;
        print(dictionary[word])