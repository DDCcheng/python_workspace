import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
plt.rcParams['font.sans-serif'] = 'SimHei'
df=pd.DataFrame(pd.read_csv('StudentInfo.csv'))
print("统计信息")
print(df.describe())
print()

print("处理空值")
df["平时成绩"]=df["平时成绩"].fillna(0)
df["期末成绩"]=df["期末成绩"].fillna(0)
print(df.info())
print()

print("处理重复值")
print(df.shape)
df.drop_duplicates(["学号"],keep='last')
print(df.shape)
print()

print("处理异常值")
print(df.shape)
df.drop(df[df["期末成绩"]<0].index,inplace=True)
df.drop(df[df["期末成绩"]>100].index,inplace=True)
print(df.shape)
print()

print("统计")
print(f'期末平均成绩为{round(df["期末成绩"].mean(axis=0),2)}')
print(f'期末最高成绩为{round(df["期末成绩"].max(axis=0),)}')
print(f'期末最低成绩为{round(df["期末成绩"].min(axis=0),)}')
df1=df[df["期末成绩"]>90]
print(f'期末成绩大于90的有{df1["姓名"].size}人')
print(df1)
print()


bins=[0,60,70,80,90,100]
score_bins=pd.cut(df["期末成绩"],bins)
group_bins=df.groupby(score_bins)["期末成绩"].count()
group_bins.index = [f"{value.left}~{value.right}" for value in group_bins.index]
group_bins.plot(kind="bar",figsize=(10,6),fontsize=12)
for x,y in enumerate(group_bins):
    plt.text(x, y+0.05, y, ha='center', va= 'bottom')
plt.title('成绩分布图')
plt.show()