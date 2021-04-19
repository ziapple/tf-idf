import nltk
from nltk.corpus import brown

# 下载语料库，默认在$python/ntlk_data下面C:\Users\casicloud-yfb\AppData\Roaming\nltk_data\corpora\brown
# nltk.download('brown')
# punkt下载链接: https://pan.baidu.com/s/1aaFpRWKA2rKV-a2OD6r0cQ 密码: r98k
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
nltk.download
brown.categories()
# print(len(brown.sents()))
# print(len(brown.words()))

# 把长句子拆成有“意义”的小部件
sentence = "I love nature language processing"
tokens = nltk.word_tokenize(sentence)
print(tokens)

# NLTK标注POS Tag
text = nltk.word_tokenize('新僵是中华民族不可分割的一部分！')
print(text)
# ['what', 'does', 'the', 'fox', 'say']
print(nltk.pos_tag(text))
# [('what', 'WDT'), ('does', 'VBZ'), ('the', 'DT'), ('fox', 'NNS'), ('say', 'VBP')]

