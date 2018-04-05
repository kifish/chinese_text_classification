#-*- coding: UTF-8 -*-
#cnt = 1
"""
from lxml import html
def html2txt(path):
    with open(path,"rb") as f:
        content = f.read()
    page = html.document_fromstring(content)
    text = page.text_content()
    return text

if __name__ == "__main__":
    path = "test.htm"
    text = html2txt(path)
    print(text)
"""


"""
import jieba
seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
print("Full Mode:"+"/".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print("Default(Accurate) Mode:"+"/".join(seg_list))

seg_list = jieba.cut("他来到网易杭研大厦")
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
print(", ".join(seg_list))
"""


import os
import jieba
jieba.enable_parallel()
def savefile(path,content,_encode='utf-8'):
    with open(path,'w',encoding=_encode) as f:
        f.write(content)

def readfile(path,_encode='utf-8'):
    with open(path,'r',encoding=_encode,errors='ignore') as f:
        content = f.read()
    return content



def preprocess(content,save_path):

    '''
    global cnt
    if cnt == 1:
        print(type(content))
        print(content)
        cnt += 1
    '''

    content = content.replace("\r\n","")
    content = content.replace(" ","")
    content_seg = jieba.cut(content)
    content_seg = " ".join(content_seg)
    '''
    if cnt == 2:
        print(type(content_seg))
        cnt += 1
    '''
    savefile(save_path,''.join(content_seg))

def corpus_segment(corpus_path,seg_path):
    catelist = os.listdir(corpus_path)

    for subdir in catelist:
        class_path = os.path.join(corpus_path,subdir)
        #class_path = os.path.join(class_path,"")

        cur_seg_path = os.path.join(seg_path,subdir)
        #seg_path = os.path.join(seg_path,"")

        if not os.path.exists(cur_seg_path):
            os.makedirs(cur_seg_path)

        if ".DS_Store" not in class_path:
            file_list = os.listdir(class_path)

            for filename in file_list:
                file_path = os.path.join(class_path,filename)
                content = readfile(file_path,_encode='gb18030')
                save_path = os.path.join(cur_seg_path,filename)
                preprocess(" ".join(content), save_path)

            print("中文语料分词结束")

if __name__ == "__main__":
    corpus_path = "./train_corpus"
    seg_path = "./train_corpus_seg"
    corpus_segment(corpus_path,seg_path)


    corpus_path = "./test_corpus"
    seg_path = "./test_corpus_seg"
    corpus_segment(corpus_path,seg_path)

"""
from sklearn.datasets.base import Bunch
bunch = Bunch(target_name=[],lable=[],filenames=[],contents=[])
"""
