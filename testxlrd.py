import xlrd
import re

def get_data(filename, sheetnum):
    dir_case = 'D:\\pycharm\\dictlist\\' + filename + '.xlsx'
    data = xlrd.open_workbook(dir_case) #打开Excel文件
    table = data.sheets()[sheetnum] ##通过索引顺序获取一个工作表
    nor = table.nrows #获取该sheet中的有效行数
    nol = table.ncols #获取列表的有效列数
    print(nor)
    print(nol)
    dict = {}
    for i in range(1, nor):   #for i in range(1,622)
        for j in range(nol):  #for j in range(5)
            title = table.cell_value(0, j)
            print(title)
            value = table.cell_value(i, j)
            # print(value)
            dict[title] = value
        yield dict

def get_data2(filename, sheetnum):
    dir_case = 'D:\\pycharm\\dictlist\\' + filename + '.xlsx'
    data = xlrd.open_workbook(dir_case) #打开Excel文件
    table = data.sheets()[sheetnum] ##通过索引顺序获取一个工作表
    nor = table.nrows #获取该sheet中的有效行数
    nol = table.ncols #获取列表的有效列数
    dict = {}
    for i in range(1, nor): #i控制行数
        for j in range(nol): #j控制列数
            title = table.cell_value(0, j)
            value = table.cell_value(i, j)
            dict[title] = value
        yield dict

# def CombineDict(dica,dicb):
#     dic = {}
#     for key in dica:
#         if dicb.get(key):
#             dic[key] = dica[key] + dicb[key]
#         else:
#             dic[key] = dica[key]
#     for key in dicb:
#         if dica.get(key):
#             pass
#         else:
#             dic[key] = dicb[key]
#     print(dic)



if __name__ == '__main__':
    for a in get_data('DNSlist', 0):
        saveDictValue = [] #用于存放DNS
        dica = a #获取Excel中的数据并以字典存放
        del dica[''] #删除冗余键值
        # print(dica)
        Getdictvalue = dica['DNS']
        # print(Getdictvalue)
        list = re.sub("A", " ", Getdictvalue,5)
        # print(Getdictvalue+list)
        dica['DNS'] = list
        # print(dica)
        saveDictValue.append(dica["DNS"])
        # print(saveDictValue)



        # SaveDictValue.append(dica['DNS'])
        # print(SaveDictValue)

        # for i in dica.keys():
        #     SaveDictValue.append(dica[i])
        #     del.SaveDictValue
        # print(SaveDictValue)







