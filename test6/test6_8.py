import re
content="who have an apple apple is free free is money you know"

words_list=re.findall(r'\w{2,5}',content)
words_set={}
for item in words_list:
    if item not in words_set.keys():
        words_set[item]=words_list.count(item)


print(words_set)