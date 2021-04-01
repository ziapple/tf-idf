from nltk.corpus import PlaintextCorpusReader


# https://blog.csdn.net/weixin_42137022/article/details/113714873?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242
# 文件根目录
corpus_root = r'../corpus'
# 文件名
corpus_file = r'example1.txt'
file = PlaintextCorpusReader(corpus_root, corpus_file)

print('words --->', file.words())
print('raw ----->', file.raw())