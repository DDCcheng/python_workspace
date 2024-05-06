import json

from data_define import Record

class FileReader:

    def read_data(self)->list[Record]:
        "读取文件数据，并将每一条数据都转换为Record对象，并存到一个list里"
        pass


class TextFileReader(FileReader):
    def __init__(self,path):
        self.path=path

    def read_data(self) ->list[Record]:
       f= open(self.path,"r",encoding="UTF-8")

       Record_list: list[Record] = []

       for line in f.readlines():
           line=line.strip()
           data_list=line.split(",")
           record=Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
           Record_list.append(record)
       f.close()
       return Record_list

class JsonFileReader():
    def __init__(self,path):
        self.path=path

    def read_data(self) ->list[Record]:
       f= open(self.path,"r",encoding="UTF-8")

       Record_list: list[Record] = []

       for line in f.readlines():
           dict_date=json.loads(line)
           record=Record(dict_date["date"],dict_date["order_id"],int(dict_date["money"]),dict_date["province"])
           Record_list.append(record)
       f.close()
       return Record_list







if __name__ == '__main__':
    textFileReader_list=TextFileReader("E:/Desktop/python/2011年1月销售数据.txt").read_data()
    jsonFileReader_list=JsonFileReader("E:/Desktop/python/2011年2月销售数据JSON.txt").read_data()
    for l in textFileReader_list:
        print(l)
    print()
    for l in jsonFileReader_list:
        print(l)

