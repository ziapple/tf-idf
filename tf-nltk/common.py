import jieba.posseg as pseg


# 对文本进行分词、去停用词
def tokenizing(s):
    result = []
    words = pseg.cut(s)
    for word, flag in words:
        result.append(word)
    return result