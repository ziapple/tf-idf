# -*- coding:utf-8 -*-
import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities

# 构建停用词表
stop_words = 'stop_words.txt'
stop_words = codecs.open(stop_words, 'r', encoding='utf8').readlines()
stop_words = [w.strip() for w in stop_words]
# 结巴分词后的停用词性 [标点符号、连词、助词、副词、介词、时语素、‘的’、数词、方位词、代词]
stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']


# 对标准答案进行分词、去停用词
def tokenization(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stop_words:
            result.append(word)
    return result


# 获取答案
file_names = ['answer1.txt', 'answer2.txt', 'answer3.txt']
corpus = []
for each in file_names:
    corpus.append(tokenization(each))


# 建立词袋模型
dictionary = corpora.Dictionary(corpus)
doc_vectors = [dictionary.doc2bow(text) for text in corpus]

# 建立TF-IDF模型
tf_idf = models.TfidfModel(doc_vectors)
tf_idf_vectors = tf_idf[doc_vectors]

# 构建一个query文本，利用词袋模型的字典将其映射到向量空间
# query = tokenization('answer_std.txt')
# query_bow = dictionary.doc2bow(query)
# index = similarities.MatrixSimilarity(tf_idf_vectors)
# 用TF-IDF模型计算相似度
# sims = index[query_bow]
# print('TF-IDF相似度')
# print(list(enumerate(sims)))
###

# 构建LSI模型，降维到主题数，主题数很关键
lsi = models.LsiModel(tf_idf_vectors, id2word=dictionary, num_topics=2)
lsi_vector = lsi[tf_idf_vectors]
# 在LSI向量空间中，所有文本的向量都是二维的
query = tokenization('answer_std.txt')
query_bow = dictionary.doc2bow(query)
query_lsi = lsi[query_bow]
index = similarities.MatrixSimilarity(lsi_vector)
sims = index[query_lsi]
# 可以看到LSI的效果很好
print('LSI相似度')
print(list(enumerate(sims)))