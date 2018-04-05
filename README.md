# chinese_text_classification

version:python3.6.3

run:python main.py

output: </br>
...... </br>
./test_corpus_seg/C4-Literature/C4-Literature61.txt 实际类别: C4-Literature --->预测类别: C3-Art  </br>
./test_corpus_seg/C4-Literature/C4-Literature49.txt 实际类别: C4-Literature --->预测类别: C3-Art  </br>
./test_corpus_seg/C4-Literature/C4-Literature63.txt 实际类别: C4-Literature --->预测类别: C3-Art  </br>
predictions finished </br>
precision:0.962 </br>
recall:0.960 </br>
f1-score:0.944 </br>

分析: 
art类样本数740 </br>
literature类样本数33 </br>
precision较高。所有错误都是把literature类的预测成了art类。显然是因为数据集的类别不平衡。

this project:vector space--->tfidf--->traditional machine learning. </br>
see also: </br>
deep learning(which doesn‘t need to extract features by tfidf)
https://github.com/kifish/cnn-text-classification-tf   </br>
