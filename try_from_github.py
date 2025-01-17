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


def save_locally_1():

    with open(local_name_1, "w") as local_fp_1:
        with urlopen(url_1) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp_1.write(line)


books = {}

for local_name in range(9, 15):
    title = f"no title {local_name}"
    author = f'no author mentioned {local_name}'
    print(local_name)
    with open(str(local_name), "w") as local_fp:
        try:
            url = f"https://www.gutenberg.org/files/{local_name}/{local_name}-0.txt"
            with urlopen(url) as fp:
                for line in fp:
                    line = line.decode('utf-8-sig').replace("\n", "")
                    local_fp.write(line)
                    if line.find("The Project Gutenberg e", 0) != -1:
                        title = line[len("The Project Gutenberg ebook of "):].strip(" ")
                        if line.find("by", 0) != -1:
                            author = line[line.find('by'):]
                            print(f'author: {author}')
                        title = title.strip(author).strip(',')
                        print(f'title: {title}')

        except:
            continue

    unique_words, word_count = get_unique_words()
    unique_count = len(unique_words.keys())

    unique_7 =[]
    for o in unique_words.keys():
        if len(o) >= 7:
            unique_7.append(o)
    unique_7 = len(unique_7)
    unique_ratio = unique_count/word_count

    # print(f"word count {word_count}, unique_7 {unique_7},unique_ratio {unique_ratio}")
    books[title] = [url, author, word_count, unique_count, unique_7, unique_ratio]

print(books)
print(books.keys())