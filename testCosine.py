import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
#语料
corpus = [
    'sina com cn',
    'sina com',
    'w sina com',
]
#将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
#计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
#获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
print (word)
a = X.toarray()
#查看词频结果
b = a.tolist()
print(b)
#计算余弦相似度
i=0
while(i<len(b)):
    vector_a = b[0]
    vector_b = np.mat(b[i])
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    i += 1
    print(sim)


# vector_a = np.mat(b[1])
# vector_b = np.mat(b[2])#  转换为Numpy矩阵
# # print(vector_a)
# num = float(vector_a * vector_b.T)
# denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
# cos = num / denom
# sim = 0.5 + 0.5 * cos
#
# print(sim)






# if __name__ == '__main__':
