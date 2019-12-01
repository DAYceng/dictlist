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
    for i in df.index.values:
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[i, ['IP', 'DNS']].to_dict()
        # df_lineDns = df.loc[i, ['DNS']].to_dict()
        # print(df_lineDns)
        # print(df_line)
        Getdictvalue = df_line['DNS']
        # print(Getdictvalue)
        list = re.sub("A", " ", Getdictvalue, 5)
        df_line['DNS'] = list
        print(df_line)

        # 将每一行转换成字典后添加到列表
        df_list.append(df_line)
        corpus.append(list)
    df_dict = df_list
    print(df_dict)
    print(corpus)


    return df_dict
if __name__ == '__main__':
    func1('D:\\pycharm\\dictlist\\DNSlist.xlsx')
