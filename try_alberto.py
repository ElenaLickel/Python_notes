from urllib.request import urlopen

url_1 = "https://www.gutenberg.org/files/1342/1342-0.txt"
url_2 = "https://www.gutenberg.org/files/11/11-0.txt"

local_name_1 = "pride_and_prejudice.txt"
local_name_2 = "alice_adventure_in_wonderland.txt"


def save_locally_1():

    with open(local_name_1, "w") as local_fp_1:
        with urlopen(url_1) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp_1.write(line)


punctuation = ",!.?-+"
def get_unique_words_1():

    unique_words_1 = {}
    with open(local_name_1) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words_1[word] = unique_words_1.get(word, 0) + 1

    return unique_words_1

unique_words_1 = get_unique_words_1()
print(sum(unique_words_1.values()))
most_frequent_1 = list(unique_words_1.values())
most_frequent_1.sort(reverse=True)
sum_1 = sum(most_frequent_1)
# print (most_frequent_1)
len_1 = len(unique_words_1.keys())

def save_locally_2():

    with open(local_name_2, "w") as local_fp_2:
        with urlopen(url_2) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp_2.write(line)

save_locally_1()
save_locally_2()

def get_unique_words_2():

    unique_words_2 = {}
    with open(local_name_2) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words_2[word] = unique_words_2.get(word, 0) + 1

    return unique_words_2

unique_words_2 = get_unique_words_2()
most_frequent_2 = list(unique_words_2.values())
most_frequent_2.sort(reverse=True)
sum_2 = sum(most_frequent_2)
# print (most_frequent_2)
len_2 = len(unique_words_2.keys())

more_than_7_1 = []
for i in unique_words_1.keys():
    if len(i) >= 7:
        more_than_7_1.append(i)

more_than_7_1 = len(more_than_7_1)

more_than_7_2 = []
for j in unique_words_2.keys():
    if len(j) >= 7:
        more_than_7_2.append(j)

more_than_7_2 = len(more_than_7_2)

ratio_1 = len_1 / sum_1
ratio_2 = len_2 / sum_2


print (f"Pride and Prejudice has {sum_1} words, and {len_1} unique words, and {more_than_7_1} words with more than 7 characters.")
print (f"Alice's Adventure in Wonderland has {sum_2} words, and {len_2} unique words, and {more_than_7_2} words with more than 7 characters.")
print (f"The first book has a ratio between unique words and total words of {ratio_1}, while the second book has a ratio of {ratio_2}.")
