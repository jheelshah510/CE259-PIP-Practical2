n_ish = int(input())
counter_dict = {}
words_list = []
foriinrange(n_ish):
word = input()words_list.append(word)
if wordincounter_dict:
    counter_dict[word] += 1
    else:
        counter_dict[word] = 1
print(len(counter_dict))
print(' '.join([str(counter_dict[word]) forwordincounter_dict]))