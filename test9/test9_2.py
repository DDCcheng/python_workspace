import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
plt.rcParams['font.sans-serif'] = 'SimHei'
df=pd.DataFrame(pd.read_csv("staff.csv"))
print(df)

print("清洗数据")
print(df.shape)
df.dropna(inplace=True)
print(df.shape)
print("清洗完成")
print()

print(f"平均计分为{round(df['计分'].mean(),2)}")
print(df[df["计分"]>90]["姓名"].size)
group_name=df.groupby("姓名")["计分"].max()
print(group_name)
group_name.plot(kind="bar")
for x,y in enumerate(group_name):
    plt.text(x, y+0.05, y, ha='center', va= 'bottom')
plt.title('成绩分布图')
plt.ylabel("计分")
plt.subplots_adjust(bottom=0.2)
plt.show()