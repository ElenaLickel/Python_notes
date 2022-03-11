from urllib.request import urlopen

url = "https://www.gutenberg.org/files/14/14-0.txt"
local_name = "frankenstein.txt"
with open(local_name, "w") as local_fp:
    with urlopen(url) as fp:
        for line in fp:
            line = line.decode().replace("\n", "")
            local_fp.write(line)
punctuation = ",.?!-+"
def get_unique_words():
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line.replace(p, " ")
            line = line.lower()
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1
    return unique_words

#save_locally()
unique_words= get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
print(most_frequent)
for word in most_frequent[0:10]:
    for unique_word, value in unique_words.items():
        if word == value:
            print(f"common word {unique_word} appears {value} times")
            break
