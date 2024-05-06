
from file_define import TextFileReader,JsonFileReader,FileReader
from data_define import Record
from pyecharts.charts import  Bar
from pyecharts.options import  *
from pyecharts.globals import ThemeType





textFileReader = TextFileReader("E:/Desktop/python/2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("E:/Desktop/python/2011年2月销售数据JSON.txt")

jan_data=textFileReader.read_data()

feb_data=jsonFileReader.read_data()

all_data:list[Record]=jan_data+feb_data

date_dic={}

for record in all_data:
    if record.date in date_dic.keys():
        date_dic[record.date]+=record.money
    else:
        date_dic[record.date]=record.money

# print(date_dic)



#可视化开发
bar =Bar(init_opts=InitOpts(theme=ThemeType.WONDERLAND))

bar.add_xaxis(list(date_dic.keys()))
bar.add_yaxis("销售额",list(date_dic.values()),label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")



