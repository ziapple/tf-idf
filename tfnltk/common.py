import jieba.posseg as pseg

# 训练语料后的模型
MODEL_PATH = '../model'
MODEL_FILE = 'corpus.bin'
# 放语料库的文件夹
CORPUS_PATH = '../corpus'


# 对文本进行分词、去停用词
def tokenizing(s):
    result = []
    words = pseg.cut(s)
    for word, flag in words:
        result.append(word)
    return result
