from urllib.request import urlopen

def get_unique_words():

    punctuation = ",.?!-"
    unique_words = {}
    word_count = 0
    with open(str(local_name)) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1
                word_count += 1
    return unique_words, word_count

books = {}
for local_name in range(10, 50):
    title = f"no title {local_name}"
    author = f"no author"
    start_book = False
    print(local_name)
    with open(str(local_name), "w") as local_fp:
        try:
            url = f"https://www.gutenberg.org/files/{local_name}/{local_name}-0.txt"
            with urlopen(url) as fp:
                for line in fp:
                    line = line.decode().replace("\n", "")
                    local_fp.write(line)
                    if start_book:
                        continue
                    elif line.find("***", 0) != -1:
                        start_book = True
                    elif line.find("Title: ", 0) != -1:
                        title = line[len("Title:"):].strip(", \r")
                        print(title)
                    elif line.find("Author: ", 0) != -1:
                        author = line[len("Author:"):].strip(", \r")
                        print(f"Written by: {author}\n")
        except:
            print("No book found for this index")
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

    books[title] = [url, author, word_count, unique_count, unique_7, unique_ratio]


print(f"we found {len(books.keys())} books in our search, here are the titles")
n = 0
for i in books.keys():
    n = n + 1
    print(f"{n}: {i}")

print('\nlets compare 2 specific books: ')
while True:
    try:
        book1 = list(books.keys())[int(input('pick book 1 by its rank'))-1]
        book2 = list(books.keys())[int(input('pick book 2 by its rank'))-1]
        break
    except ValueError:
        print(f"\nPlease write an integer between 1 and {len(books.keys())}!!!\n")
        continue
    except IndexError:
        print(f"\nPlease write an integer between 1 and {len(books.keys())}!!!\n")
        continue

print('The first book was written by', books[book1][1], 'and the second one by', books[book2][1], '.\n')
print('The first book has', books[book1][2], 'words, \nwhile the second book has', books[book2][2], 'words.\n')
print('The first book has', books[book1][3], 'unique words, \nwhile the second book has', books[book2][3], 'unique words.\n')
print('The first book has', books[book1][4], 'unique words with more than 7 letters, \nwhile the second book has', books[book2][4], 'unique words with more than 7 letters.\n')
print('The first book has unique words ratio of', books[book1][5], ', \nwhile the second book has unique words ratio of', books[book2][5], '.\n')

# for word in most_frequent[0:10]:
