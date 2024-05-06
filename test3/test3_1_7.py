def long_sub_str(my_str):
    lst_all = []
    for i in range(len(my_str)):
        lst_all = lst_all + [my_str[j:i + j + 1] for j in range(len(my_str))]  # 获得全部子串
    lst = sorted(set(lst_all), key=len, reverse=True)  # 去重，按长度降序排序
    filter_lst = [s1 for s1 in lst if s1 == s1[::-1]]
    answer = [x for x in filter_lst if len(x) == max(map(len, filter_lst))]
    answer.sort()
    return answer

print(long_sub_str("abawdad"))
