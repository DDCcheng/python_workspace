import json

data=[{"name":"张大仙","age":11},
      {"name":"王大锤","age":13},
      {"name":"赵小虎","age":16}]
json_str=json.dumps(data,ensure_ascii=False)
print(json_str)
print(type(json_str))


s='[{"name":"张大仙","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]'
json_str1=json.loads(s)
print(json_str1)
print(type(json_str1))

print(f"我是'cheng'")
print("i am")
print('i am')