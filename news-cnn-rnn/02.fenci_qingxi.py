import os
import jieba
import time

#获取停用词
def stopwordslist(): #加载停用词表
    stopwords = [line.strip() for line in open('stop_words.txt', encoding="UTF-8").readlines()]
    return stopwords

#去除停用词
def deleteStop(sentence):
    stopwords = stopwordslist()
    outstr = ""
    for i in sentence:
        #print(i)
        if i not in stopwords and i!="\n":
            outstr += i
    return outstr

#中文分词
def fenci_text(file_name, write_name):
    #写入文件
    fw = open(write_name, 'w', encoding='UTF-8')
    #读取文件
    with open(file_name, 'r', encoding='UTF-8') as p:
        for line in p.readlines():
            #读取数据
            name = line.split('\t')[0]
            content = line.split('\t')[1]
            #中文分词
            seglist = jieba.cut(content,cut_all=False)  #精确模式
            #去停用词
            stc = deleteStop(seglist)                   #注意此时句子无空格 seglist仅用一次消失
            #空格拼接
            seg_list = jieba.cut(stc,cut_all=False)
            result = ' '.join(list(seg_list))
            #print(result)
            #文件写入
            fw.write(name + '\t' + result + '\n')
        else:
            print('fenci done!', write_name)
    fw.close()

#函数调用
fenci_text("data_test.txt", "fenci_test.txt")
fenci_text("data_train.txt", "fenci_train.txt")
fenci_text("data_val.txt", "fenci_val.txt")

