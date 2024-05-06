

from pyspark import SparkConf,SparkContext

#创建SparkConf类对象
con=SparkConf().setMaster("local[*]").setAppName("test_spark_app")


#基于SparkConf类对象创建SparkContest类对象
sc = SparkContext(conf=con)
# sc=SparkContext("local[*]","firstapp")
#打印Pyspark的运行版本

print(sc.version)

#停止SparkContext对象的运行
sc.stop()