import nltk
import jieba.posseg as pseg
import common


# 用print输出本地字符格式
def dump_result(result):
    for item in result:
        print(item[0], ",", item[1])


def tag(raw):
    # 用jieba分词
    tokens = common.tokenizing(raw)
    return nltk.pos_tag(tokens)


if __name__ == "__main__":
    text = '经过漫长的盘旋，中国的封建社会走到20世纪已经风光不再、败相尽露。外敌入侵有加无已、国内民变接连而起，危机四伏的大清王朝犹如一艘破烂不堪的航船，'
    print(tag(text))
