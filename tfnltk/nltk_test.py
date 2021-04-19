import logging
from gensim.models import word2vec
import common

model = word2vec.Word2Vec.load('../model/news_12g_baidubaike_20g_novel_90g_embedding_64.model')


# 找出相似词
def similar(word):
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
    result = model.most_similar(word, topn=10)
    print(result)


def two_word_similar():
    two_corpus = ["腾讯", "阿里巴巴"]
    res = model.similarity(two_corpus[0], two_corpus[1])
    print("similarity:%.4f" % res)
    similarity: 0.7268


if __name__ == "__main__":
    two_word_similar()
    print(similar('母亲'))