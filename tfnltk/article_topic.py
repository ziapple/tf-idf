from gensim import corpora
import nltk
from pprint import pprint
# 针对文档-词频矩阵进行LDA主题建模
from gensim.models.ldamodel import LdaModel

sentence_pro = '伸入大洋的印度半岛有利于拓展其在印度洋的海上存在'
# 直接使用上面case的文本数据
all_tokens = []
for text in sentence_pro:
    tokens = []
    raw = nltk.wordpunct_tokenize(text)
    for token in raw:
        tokens.append(token)
        all_tokens.append(tokens)

# 创建一个字典（dictionary）和 矩阵（matrix）
dictionary = corpora.Dictionary(all_tokens)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in all_tokens]
model = LdaModel(doc_term_matrix, num_topics=5, id2word=dictionary, passes=40)
pprint(model.print_topics(num_topics=2, num_words=2))