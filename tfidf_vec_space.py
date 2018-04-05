#coding = utf-8
import pickle
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer
''' vectorizer = TfidfVectorizer(stop_words=stoplist,sublinear_tf=True,
                                     max_df=0.5,vocabulary=trainbunch.vocabulary)

    stop_words:
    传入停用词，以后我们获得vocabulary_的时候，就会根据文本信息去掉停用词得到
    sublinear_tf:
    计算tf值采用亚线性策略。比如，我们以前算tf是词频，现在用1+log(tf)来充当词频。
    smooth_idf:
    计算idf的时候log(分子/分母)分母有可能是0，smooth_idf会采用log(分子/(1+分母))的方式解决。默认已经开启，无需关心。
     max_df:
    有些词，他们的文档频率太高了（一个词如果每篇文档都出现，那还有必要用它来区分文本类别吗？当然不用了呀），所以，我们可以
    设定一个阈值，比如float类型0.5（取值范围[0.0,1.0]）,表示这个词如果在整个数据集中超过50%的文本都出现了，那么我们也把它列
    为临时停用词。当然你也可以设定为int型，例如max_df=10,表示这个词如果在整个数据集中超过10的文本都出现了，那么我们也把它列
    为临时停用词。
    min_df:
    与max_df相反，虽然文档频率越低，似乎越能区分文本，可是如果太低，例如10000篇文本中只有1篇文本出现过这个词，仅仅因为这1篇
    文本，就增加了词向量空间的维度，太不划算。
    当然，max_df和min_df在给定vocabulary参数时，就失效了。
'''
def _readfile(path):
    with open(path,'rb') as f:
        content = f.read()
    return content

def _readbunchobj(path):
    with open(path,'rb') as fileobj:
        bunch = pickle.load(fileobj)
    return bunch

def _writebunchobj(path,bunchobj):
    with open(path,'wb') as file_obj:
        pickle.dump(bunchobj,file_obj)

def vector_space(stopword_path,bunch_path,space_path,train_tfidf_path=None):
    stoplist = _readfile(stopword_path).splitlines()
    bunch = _readbunchobj(bunch_path)
    #tdm存放的是计算后得到的TF-IDF权重矩阵
    #vocabulary是词典索引，例如
    #vocabulary={"我":0,"喜欢":1,"相国大人":2}，这里的数字对应的就是tdm矩阵的列
    tfidfspace = Bunch(target_name=bunch.target_name,label = bunch.label,filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    if train_tfidf_path is not None:
        trainbunch = _readbunchobj(train_tfidf_path)
        tfidfspace.vocabulary = trainbunch.vocabulary
        vectorizer = TfidfVectorizer(stop_words=stoplist,sublinear_tf=True,
                                     max_df=0.5,vocabulary=trainbunch.vocabulary,
                                     decode_error='ignore')
        #vectorizer 得到词频矩阵
        '''
        contents = ""
        for x in bunch.contents:
            x = str(x,encoding='utf-8')
            contents += x
        tfidfspace.tdm = vectorizer.fit_transform(contents)

        '''
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)


        '''
        vectorizer=CountVectorizer()
        transformer=TfidfTransformer()#
        tfidfspace=transformer.fit_transform(vectorizer.fit_transform(corpus))
        语料->词频矩阵->tfidf权重矩阵

        Tfidf-Transformer + Count-Vectorizer  = Tfidf-Vectorizer

        '''
    else:
        vectorizer = TfidfVectorizer(stop_words=stoplist,sublinear_tf=True,max_df=0.5,decode_error='ignore')
        #因为只有一个content编码有问题，可以直接忽略
        #vectorizer = TfidfVectorizer(stop_words=stoplist, sublinear_tf=True, max_df=0.5)
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
        '''
        vectorizer = TfidfVectorizer(stop_words=stoplist, sublinear_tf=True, max_df=0.5)
        bunch.contents =[ x.decode(encoding='utf-8') for x in bunch.contents]
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)

        Traceback (most recent call last):
        ...
        bunch.contents =[ x.decode(encoding='utf-8') for x in bunch.contents]
        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc0 in position 10: invalid start byte
        '''

        '''
        这段代码可以运行成功，只有idx为110的content编码有问题
        vectorizer = TfidfVectorizer(stop_words=stoplist, sublinear_tf=True, max_df=0.5)
        contents = []
        for idx,item in enumerate(bunch.contents):
            try:
                if idx ==110:
                    continue
                contents.append(bunch.contents[idx])
            except Exception as e:
                print('Error:',e)
                print(idx)
                print(len(bunch.contents))
        tfidfspace.tdm = vectorizer.fit_transform(contents)
        '''

        '''
        #这段代码也可以运行成功
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.feature_extraction.text import TfidfTransformer
        vectorizer=CountVectorizer()
        transformer=TfidfTransformer()#
        #print(type(bunch.contents))
        #<class 'list'>
        #print(type(bunch.contents[0]))
        #< class 'bytes'>
        #contents = [str(x,encoding='unicode') for x in bunch.contents]
        contents = [x for idx,x in enumerate(bunch.contents) if idx != 110]
        tfidfspace.tdm=transformer.fit_transform(vectorizer.fit_transform(contents))
        #tdm里面存储的就是tf-idf权值矩阵
        '''
        tfidfspace.vocabulary = vectorizer.vocabulary_

    _writebunchobj(space_path,tfidfspace)
    print("tf-idf词向量空间实例创建成功!")

if __name__ == '__main__':
    stopword_path = "./train_word_bag/hlt_stop_words.txt"
    bunch_path = "./train_word_bag/train_set.dat"
    space_path = "./train_word_bag/tfidfspace.dat"
    vector_space(stopword_path,bunch_path,space_path)

    bunch_path = "./test_word_bag/test_set.dat"
    space_path = "./test_word_bag/testspace.dat"
    train_tfidf_path="./train_word_bag/tfidfspace.dat"
    vector_space(stopword_path,bunch_path,space_path,train_tfidf_path)
