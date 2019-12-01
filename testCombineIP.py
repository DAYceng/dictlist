import xlrd
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def func1(path):
    # 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)

    # 创建最终返回的空字典
    # df_dict = {}
    # 读取Excel文件
    df = pd.read_excel(path)

    # 替换Excel表格内的空单元格，否则在下一步处理中将会报错
    df.fillna("", inplace=True)

    df_list = []
    corpus = []
    listIP = []
    for i in df.index.values:
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[i, ['IP', 'DNS']].to_list()
        # print(df_line)
        GetdictDNSvalue = df_line[1]
        # print(GetdictDNSvalue)
        listDNS = re.sub("A", " ", GetdictDNSvalue, 5)
        # print(listDNS) #正则后的dns
        GetdictIPvalue = df_line[0]
        df_line[1] = listDNS
        # print(df_line) #IP+DNS的列表（字典）
        # print(GetdictIPvalue) #上述字典中的每个ip

        # 将每一行转换成字典后添加到列表
        df_list.append(df_line)
        listIP.append(GetdictIPvalue)
        # listIP.append(listDNS)
        corpus.append(listDNS)
    df_dict = df_list
    print(df_dict)

    # df = pd.DataFrame(df_dict)
    # result = df.groupby(['IP']).sum()
    # instanceLS = []
    # instanceLS.append(result)

    # print(instanceLS)

    newlistip = list(set(listIP))
    newlistip.sort(key=listIP.index)
    # print(listIP)
    # print(newlistip)  # 去重ip

    instanceSL = {}
    for i in df_dict:
        ip = i[0]
        if ip not in instanceSL.keys():
            instanceSL[ip] = [i[1]]
        else:
            instanceSL[ip].append(i[1])
    print(instanceSL)

    return df_dict
if __name__ == '__main__':
    func1('D:\\pycharm\\dictlist\\DNSlist.xlsx')