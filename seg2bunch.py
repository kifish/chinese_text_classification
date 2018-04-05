#coding = utf-8
import os
import pickle
from sklearn.datasets.base import Bunch

"""
'_'为了增强可读性
"""


def _readfile(path):
    with open(path,"rb") as f:
        content = f.read()
    return content

def corpus2Bunch(word_bag_path,seg_path):
    catelist = os.listdir(seg_path)
    bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])
    catelist = [x for x in catelist if "DS_Store" not in str(x) and "txt" not in str(x)]
    bunch.target_name.extend(catelist)
    for subdir in catelist:
        class_path = os.path.join(seg_path,subdir)
        #class_path = os.path.join(class_path,"")
        filename_list = os.listdir(class_path)
        for filename in filename_list:
            filepath = os.path.join(class_path,filename)
            bunch.label.append(subdir)
            bunch.filenames.append(filepath)
            bunch.contents.append(_readfile(filepath)) #append bytes
    with open(word_bag_path,"wb") as file_obj:
        pickle.dump(bunch,file_obj)
    print("构建文本对象结束！")


if __name__ == "__main__":
    word_bag_path = "./train_word_bag/train_set.dat"
    seg_path = "./train_corpus_seg"
    corpus2Bunch(word_bag_path,seg_path)

    word_bag_path = "./test_word_bag/test_set.dat"
    seg_path = "./test_corpus_seg"
    corpus2Bunch(word_bag_path,seg_path)
