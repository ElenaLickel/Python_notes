from urllib.request import urlopen


def get_unique_words():
    punctuation = ",.?!-+"
    unique_words = {}
    word_count = 0
    with open(str(local_name)) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line.replace(p, " ")
            line = line.lower()
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1
                word_count += 1
    return unique_words, word_count

books = {
}

for local_name in range(9, 1000):
    print(local_name)
    with open(str(local_name), "w") as local_fp:
        try:
            with urlopen(f"https://www.gutenberg.org/files/{local_name}/{local_name}-h/{local_name}-h.htm") as fp:
                for line in fp:
                    line = line.decode().replace("\n", "")
                    local_fp.write(line)

                    if str(line[0:2]) == "The Project Gutenberg":
                        print("hello")
        except:
            print("error")
            continue

    #save_locally()
    unique_count = []
    unique_7 =[]
    unique_words, word_count = get_unique_words()
    most_frequent = list(unique_words.values())
    most_frequent.sort(reverse=True)
    print(most_frequent[:5])

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


