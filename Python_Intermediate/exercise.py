from pprint import pprint

sentence = "This is a common interview question"

char_occurence = {}

for char in sentence:
    if not char in char_occurence:
        char_occurence[char] = 1
    else:
        char_occurence[char] += 1

most_repeated = sorted(char_occurence.items(), key=lambda kv: kv[1], reverse=True )
pprint(sorted(char_occurence.items(), key=lambda kv: kv[1] ), width=10)

print("Most repeated: ", most_repeated[0:1])
