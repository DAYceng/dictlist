import xlrd
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from collections import Counter


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
    stoplist = ['com', 'org', 'www', 'net']  # 停用词列表
    df_list = []
    oldcorpus = []
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
        oldcorpus.append(listDNS)
    df_dict = df_list
    print("从Excel读取的原始数据以列表方式存放")
    print(df_dict)
    print(' ')
    print("旧逻辑下的语料库")
    print(oldcorpus)
    print(' ')

    # ip去重
    # newlistip = list(set(listIP))
    # newlistip.sort(key=listIP.index)
    # print(listIP)
    # print(newlistip)

    '''用pandas库方法去除重复ip并合并该ip下的dns
    df = pd.DataFrame(df_dict)
    result = df.groupby(['IP']).sum()
    instanceLS = []
    instanceLS.append(result)

    print(instanceLS)'''

    # 生成新的不含重复ip的字典
    instanceSL = {}
    qiepian = {}
    for i in df_dict:  # 遍历实例字典
        ip = i[0]  # 获取实例中的ip
        if ip not in instanceSL.keys():  # 判断instanceSL中是否有键值与当前ip对应
            instanceSL[ip] = [i[1]]  # 没有的话就将当前ip作为键值，其对应DNS作为列表
        else:
            instanceSL[ip].append(i[1])  # 已存在相同的ip键值就只将对应DNS添加
    print("新的不含重复ip的字典(实例)")
    print(instanceSL)
    print(' ')

    # # 计算TFIDF值3
    corpus = []
    for key, value in instanceSL.items():
        strlist = value
        k = " ".join(strlist)
        # 笨办法去除停用词
        a = k.replace('com', ' ')
        b = a.replace('net', ' ')
        c = b.replace('org', ' ')
        d = c.replace('www', ' ')

        # for word in a:
        #     if word not in stoplist:
        #
        # print(a)
        corpus.append(d)
    print("新逻辑下的语料库")
    print(corpus)
    print(' ')
    # compercorpus = []
    # for i in corpus:
    #     print(i.split())
    #
    # print(' ')
    # 将文本中的词语转换为词频矩阵
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(
        vectorizer.fit_transform(corpus))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

    for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        scoredict = {}
        print(u"-------这里输出第", i, u"个文档的词语tf-idf权重------")

        for j in range(len(word)):
            if weight[i][j] != 0:  # 输出结果不为0的tfidf
                # print(word[j], weight[i][j])
                dnsWord = word[j]
                dnstfidfscore = weight[i][j]
                if dnsWord not in scoredict.keys():
                    scoredict[dnsWord] = dnstfidfscore

        print(scoredict)
        print("按值(value)排序:")
        print(sorted(scoredict.items(), key=lambda x: x[1], reverse=True))
        print(' ')

    return df_dict


if __name__ == '__main__':
    func1('D:\\pycharm\\dictlist\\DNSlist.xlsx')