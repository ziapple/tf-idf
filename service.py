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


# 对文本进行分词、去停用词
def tokenizing(s):
    result = []
    words = pseg.cut(s)
    for word, flag in words:
        if flag not in stop_flag and word not in stop_words:
            result.append(word)
    return result


# 计算两个文本的相似度,std标准答案,arr多个答案
def apply(std, arr):
    corpus = []
    for each in arr:
        corpus.append(tokenizing(each))
    # 建立词袋模型
    dictionary = corpora.Dictionary(corpus)
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]

    # 建立TF-IDF模型
    tf_idf = models.TfidfModel(doc_vectors)
    tf_idf_vectors = tf_idf[doc_vectors]

    # 构建LSI模型，降维到主题数，主题数很关键
    lsi = models.LsiModel(tf_idf_vectors, id2word=dictionary, num_topics=2)
    lsi_vector = lsi[tf_idf_vectors]
    # 在LSI向量空间中，所有文本的向量都是二维的
    query = tokenizing(std)
    query_bow = dictionary.doc2bow(query)
    query_lsi = lsi[query_bow]
    index = similarities.MatrixSimilarity(lsi_vector)
    sims = index[query_lsi]
    # 可以看到LSI的效果很好
    return list(enumerate(sims))


if __name__ == '__main__':
    print(apply('开辟了中国特色社会主义道路，形成了中国特色社会主义理论体系',
                ['从百姓民生到重大事件，以“以故事讲思想”的方式原汁原味的再现了历史和人民是为什么选择了中国共产党、选择了社会主义、选择了改革开放',
                 '共产党他一心救中国']))
