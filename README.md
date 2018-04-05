# chinese_text_classification

version:python3.6.3

python main.py


output:
......
./test_corpus_seg/C4-Literature/C4-Literature61.txt 实际类别: C4-Literature --->预测类别: C3-Art
./test_corpus_seg/C4-Literature/C4-Literature49.txt 实际类别: C4-Literature --->预测类别: C3-Art
./test_corpus_seg/C4-Literature/C4-Literature63.txt 实际类别: C4-Literature --->预测类别: C3-Art
预测完毕
精度:0.962
召回:0.960
f1-score:0.944

分析:
art样本数740
literature样本数33
精度较高。所有错误都是把literature类的预测成了art类。显然是因为类别不平衡的样本数量。

