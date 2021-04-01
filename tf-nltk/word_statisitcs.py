from nltk import FreqDist
import numpy as np
import common

sent = '词频统计、词表生成、关键词索引、句型统计、主题词提取等'


def stat_freq(text):
    words = common.tokenizing(text)
    freq_dist = FreqDist(words)
    freq_list = []
    num_words = len(freq_dist.values())
    for i in range(num_words):
        freq_list.append([list(freq_dist.keys())[i], list(freq_dist.values())[i]])
    freq_arr = np.array(freq_list)
    print(freq_arr)



