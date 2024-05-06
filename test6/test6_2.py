chinese_dic= {1: "壹", 2: "贰",3:"叁",4:"肆",5:"伍",6:"陆",7:"柒",8:"捌",9:"玖",0:"零"}
num_str=input("请输入一串数字\n")
chinese_str=""
for item in num_str:
    chinese_item=chinese_dic.get(int(item))
    chinese_str+=chinese_item
print(chinese_str)