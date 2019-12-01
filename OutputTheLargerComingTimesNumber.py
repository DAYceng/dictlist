f=open("2.txt",'r')
ll=f.read()
'''将空格都取代为逗号，方便后面的split（）'''
ll=ll.replace(" ",',')
'''防止由于文档编辑不规范出现双逗号的情况'''
ll=ll.replace(",,",',')
l=ll.split("\n")
rows=[]
dic={}
for i in l:
    row=i.split(",")
    rows.append(row)
for ii in rows:
    for each in ii:
        if each in dic:
            dic[each]=dic[each]+1
        else:
            dic[each]=1

#输出所有的排序：
print(sorted(dic.items(),key=lambda x:x[1],reverse=True))

'''只输出最大的值'''
HighValue=0
HighKey=None
for each in dic:
    if dic[each]>HighValue:
        HighValue=dic[each]
        HighKey=each
print(HighKey,HighValue)