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

books = {}

for local_name in range(9, 100):
    title = f"no title {local_name}"
    print(local_name)
    with open(str(local_name), "w") as local_fp:
        try:
            url = f"https://www.gutenberg.org/files/{local_name}/{local_name}-0.txt"
            with urlopen(url) as fp:
                for line in fp:
                    line = line.decode().replace("\n", "")
                    local_fp.write(line)
                    if line.find("The Project Gutenberg e", 0) != -1:
                        title = line[len("The Project Gutenberg ebook of "):].strip(" ")
                        print(title)
        except:
            # print("error")
            continue

    # save_locally()
    unique_7 =[]
    unique_words, word_count = get_unique_words()

    # most_frequent = list(unique_words.values())
    # most_frequent.sort(reverse=True)
    # print(most_frequent[:5])

    unique_count = len(unique_words.keys())

    # print(unique_count)

    for o in unique_words.keys():
        if len(o) >= 7:
            unique_7.append(o)

    unique_7 = len(unique_7)
    unique_ratio = unique_count/word_count

    # print(f"word count {word_count}, unique_7 {unique_7},unique_ratio {unique_ratio}")
    books[title] = [url, word_count, unique_count, unique_7, unique_ratio]

print(books)
print(books.keys())
# for word in most_frequent[0:10]:
# for unique_word, value in unique_words.items():
