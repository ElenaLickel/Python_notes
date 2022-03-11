from urllib.request import urlopen

books = {
    "Wealth:_of_Nations.txt": "https://www.gutenberg.org/files/3300/3300-h/3300-h.htm",
    "Communist_Manifesto.txt": "https://www.gutenberg.org/files/61/61-h/61-h.htm"
}

for local_name, url in books.items():
    print(local_name)
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode().replace("\n", "")
                local_fp.write(line)

    punctuation = ",.?!-+"

    def get_unique_words():
        unique_words = {}
        word_count = 0
        with open(local_name) as fp:
            for line in fp:
                # remove punctuation
                for p in punctuation:
                    line.replace(p, " ")
                line = line.lower()
                for word in line.split():
                    unique_words[word] = unique_words.get(word, 0) + 1
                    word_count += 1
        return unique_words, word_count

    #save_locally()
    unique_count = []
    unique_7 =[]
    unique_words, word_count = get_unique_words()
    most_frequent = list(unique_words.values())
    most_frequent.sort(reverse=True)
    print(most_frequent)

    unique_count.append(len(unique_words.keys()))

    print(unique_count)

    for i in unique_words.keys():
        if len(i) >= 7:
            unique_7.append(i)
    unique_7 = len(unique_7)
    print(unique_7)

    print(unique_count[0]/word_count)


#for word in most_frequent[0:10]:
    #for unique_word, value in unique_words.items():


