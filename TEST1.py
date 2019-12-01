from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = (" netcom netatmo com   netcom netatmo net")

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)






# Message = [[2,'Mike'],[1,'Jone'],[2,'Marry']]
# dict1 = {}
# for number in Message:
#     value = number[0]
#     if value not in dict1.keys():
#         dict1[value] = [number]        #此句话玄机
#     else:
#         dict1[value].append(number[1])
# print (dict1)
# list=[]
# l = ['  aps1-relay tplinkcloud com', '  devs tplinkcloud com', '  0 pool ntp org']
# k=" ".join(l)
# list.append(k)
# print(list)

