import logging
from gensim.models import word2vec
import os
import common


def train():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
    log = '加载语料...\n'
    sentences = word2vec.PathLineSentences(common.CORPUS_PATH)
    log = log + ' \n'.join(sentences.input_files)

    log = log + '\n开始训练..., word2vec.Word2Vec(sentences, min_count=1)\n'
    model = word2vec.Word2Vec(sentences, min_count=1)

    # 保存模型
    if not os.path.exists(common.MODEL_PATH):
        os.mkdir(common.MODEL_PATH)
    model.save(common.MODEL_PATH + '/' + common.MODEL_FILE)
    log = log + '训练结束...，模型保存在' + common.MODEL_FILE
    return log


if __name__ == "__main__":
    print(train())