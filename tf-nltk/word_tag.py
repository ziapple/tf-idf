import nltk
import jieba.posseg as pseg
import common


# 用print输出本地字符格式
def dump_result(result):
    for item in result:
        print
        item[0], ",", item[1],
    print


# 等标注的词，以空格分词（分词问题不在此讨论）
raw = '支持给定语料内容自动入库、含教材、讲稿、试题等'
# 用jieba分词
tokens = common.tokenizing(raw)
print(nltk.pos_tag(tokens))
