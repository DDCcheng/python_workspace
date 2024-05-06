from pyecharts.charts import Map
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts


map=Map()


data = [
    ("上海", 199),("北京", 99),("湖南", 299),("台湾", 399),("广东", 499),("111",222)]


map.add("测试地图",data,"china")


map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True
    )

)

map.render()