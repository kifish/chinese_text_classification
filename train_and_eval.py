#coding = utf-8
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

def _readbunchobj(path):
    with open(path,'rb') as file_obj:
        bunch = pickle.load(file_obj)
    return bunch

train_path = "./train_word_bag/tfidfspace.dat"
train_set = _readbunchobj(train_path)

test_path = "./test_word_bag/testspace.dat"
test_set = _readbunchobj(test_path)

clf = MultinomialNB(alpha=0.001).fit(train_set.tdm,train_set.label)
pred = clf.predict(test_set.tdm)

for flabel,file_name,pred_cate in zip(test_set.label,test_set.filenames,pred):
    if flabel != pred_cate:
        print(file_name,"实际类别:",flabel,"--->预测类别:",pred_cate)

print("预测完毕")
def metrics_result(actual,pred):
    print('精度:{0:.3f}'.format(metrics.precision_score(actual,pred,average='weighted')))
    print('召回:{0:0.3f}'.format(metrics.recall_score(actual,pred,average='weighted')))
    print('f1-score:{0:0.3f}'.format(metrics.f1_score(actual,pred,average='weighted')))

metrics_result(test_set.label,pred)
