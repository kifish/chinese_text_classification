from corpus_segment import *
from seg2bunch import *
from tfidf_vec_space import *
import os
corpus_path = "./train_corpus"
seg_path = "./train_corpus_seg"
corpus_segment(corpus_path,seg_path)

corpus_path = "./test_corpus"
seg_path = "./test_corpus_seg"
corpus_segment(corpus_path,seg_path)

word_bag_path = "./train_word_bag/train_set.dat"
seg_path = "./train_corpus_seg"
corpus2Bunch(word_bag_path,seg_path)

word_bag_path = "./test_word_bag/test_set.dat"
seg_path = "./test_corpus_seg"
corpus2Bunch(word_bag_path,seg_path)


stopword_path = "./train_word_bag/hlt_stop_words.txt"
bunch_path = "./train_word_bag/train_set.dat"
space_path = "./train_word_bag/tfidfspace.dat"
vector_space(stopword_path,bunch_path,space_path)

bunch_path = "./test_word_bag/test_set.dat"
space_path = "./test_word_bag/testspace.dat"
train_tfidf_path="./train_word_bag/tfidfspace.dat"
vector_space(stopword_path,bunch_path,space_path,train_tfidf_path)

os.system("python train_and_eval.py")
print("Done!")
