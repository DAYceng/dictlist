# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.tokenize as tk
from nltk import word_tokenize
from nltk.corpus import stopwords

#需要分词的文本
doc = ["Are you ok? "]

set(stopwords.words('english'))

#文本分句
# tokens = tk.sent_tokenize(doc)
# for i, token in enumerate(tokens):
#     print('%2d' % (i + 1), token)
# print('-' * 10)

#文本分词
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
print(tokens)
# for i, token in enumerate(tokens):
#     print('%2d' % (i + 1), token)
