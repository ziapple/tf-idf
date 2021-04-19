from nltk import FreqDist
from rake_nltk import Rake
import numpy as np
import common


# 词频统计
def stat_freq(text):
    words = common.tokenizing(text)
    freq_dist = FreqDist(words)
    freq_list = []
    num_words = len(freq_dist.values())
    for i in range(num_words):
        freq_list.append([list(freq_dist.keys())[i], list(freq_dist.values())[i]])
    freq_arr = np.array(freq_list)
    return freq_arr


# 主题词提取
def extract_key_word_rank(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    print(r.get_ranked_phrases())
    print("==============================")
    print(r.get_word_degrees())


# 主题词提取，找到词频最多的作为关键词，同时作为分类
def extract_key_word(text):
    arr = stat_freq(text)
    b = sorted(arr, key=lambda a: a[1], reverse=True)
    arr = []
    for item in b:
        if item[0] not in ['的', '，', '。', '了','是']:
            arr.append(item)
    return arr


if __name__ == '__main__':
    sentence = "本书是莫言篇幅最为饱满的长篇小说，从抗日战争一直写到改革开放之后，描绘了一部波澜壮阔的历史。书中的母亲和瑞典人马洛亚牧师生下了上官金童"
    extract_key_word(sentence)
