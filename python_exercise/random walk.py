import numpy as np
import random


def random_walk(text, length):
    # 将文本划分为单词列表
    words = text.split()
    # 随机选择起始单词
    current_word = random.choice(words)
    # 初始化路径
    path = [current_word]

    # 从当前单词开始生成路径
    for i in range(length-1):
        # 获取当前单词的所有相邻单词
        neighbors = []
        for j in range(len(words)-1):
            if words[j] == current_word:
                neighbors.append(words[j+1])
        # 如果没有相邻单词，停止生成路径
        if len(neighbors) == 0:
            break
        # 随机选择相邻单词作为下一个单词，并添加到路径中
        current_word = random.choice(neighbors)
        path.append(current_word)

    # 返回生成的路径
    return ' '.join(path)


vocab_size = 100
embedding_size = 50
word2idx = {f"word{i}": i for i in range(vocab_size)}
embeddings = np.random.randn(vocab_size, embedding_size)