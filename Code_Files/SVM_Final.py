# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:29:00 2015

@author: Ashish Yadav
"""


import pandas as pd
from sklearn import svm

def measure(word1,word2):
    if word1==word2:
        return 1
    else:
        return 0

def main():
    df = pd.read_csv('TrainRel1.csv',header = None)
    Y = df.values

    print Y
    num_of_rows = Y.shape[0]
    print num_of_rows
    ans = ""
    for i in range(num_of_rows):
        if Y[i,0] != 1:
            ans = ans + str(Y[i,1])
            
    word_list = ans.split()
    unique_words = set(word_list)
    vocabulary = list(unique_words)
    
    questions_list = []
    answers_list = []
    answers = []
    answers2 = []
    label = []
    for i in range(num_of_rows):
        if Y[i,0] == 1:
            answers_list.append(answers2)
            questions_list.append(Y[i,1])
            answers2 = []
        else:
            #count_label += 1
            answers2.append(Y[i,1])
            if Y[i,2]>0 and len(str(Y[i,1]))>0:
                label.append(1)
            elif Y[i,2]<=0 and len(str(Y[i,1]))>0:
                label.append(-1)
    
    answers_list.append(answers2)
    del answers_list[0]
    feature_vector = []
    print "ans"
    
    #print answers_list
    #print len(answers_list)
    #print len(label)
    count_ans = 0
    #print answers_list
    for i in range(len(answers_list)):
        questions_list_split = questions_list[i].split()
        lis = answers_list[i]
        print len(lis)
        for j in range(len(lis)):            
            val = lis[j]
            if (isinstance(val,basestring)):
                val_list = val.split()
                print val                
            else:
                del label[count_ans]
                continue                
            count_ans = count_ans + 1                
                
            print val_list
            vocab_zeros = [0] * len(vocabulary)
            for k in range(len(val_list)):
                sum_simil = 0;
                for l in range(len(questions_list_split)):
                    sum_simil = sum_simil + measure(val_list[k],questions_list_split[l])
                avg_simil = float(sum_simil)/len(questions_list_split)
                if val_list[k] in vocabulary:
                    vocab_zeros[vocabulary.index(val_list[k])] = avg_simil
            feature_vector.append(vocab_zeros)
    '''        
    for i in range(len(feature_vector)):
        print feature_vector[i],label[i]
    '''
    #print len(feature_vector)
    #print feature_vector
    print label
    #print feature_vector
    
    clf = svm.SVC(kernel='rbf')
    clf.fit(feature_vector, label)
    
    
    df = pd.read_csv('TestRel1.csv',header = None)
    Y = df.values

    print Y
    num_of_rows = Y.shape[0]
    print num_of_rows
    ans = ""
    for i in range(num_of_rows):
        if Y[i,0] != 1:
            ans = ans + str(Y[i,1])
            
    word_list = ans.split()
    unique_words = set(word_list)
    vocabulary = list(unique_words)
    
    questions_list = []
    answers_list = []
    answers = []
    answers2 = []
    label = []
    for i in range(num_of_rows):
        if Y[i,0] == 1:
            answers_list.append(answers2)
            questions_list.append(Y[i,1])
            answers2 = []
        else:
            #count_label += 1
            answers2.append(Y[i,1])
            if Y[i,2]>0 and len(str(Y[i,1]))>0:
                label.append(1)
            elif Y[i,2]<=0 and len(str(Y[i,1]))>0:
                label.append(-1)
    
    answers_list.append(answers2)
    del answers_list[0]
    feature_vector = []
    print "ans"
    
    #print answers_list
    #print len(answers_list)
    #print len(label)
    count_ans = 0
    #print answers_list
    for i in range(len(answers_list)):
        questions_list_split = questions_list[i].split()
        lis = answers_list[i]
        print len(lis)
        for j in range(len(lis)):            
            val = lis[j]
            if (isinstance(val,basestring)):
                val_list = val.split()
                print val                
            else:
                del label[count_ans]
                continue                
            count_ans = count_ans + 1                
                
            #print val_list
            vocab_zeros = [0] * len(vocabulary)
            for k in range(len(val_list)):
                sum_simil = 0;
                for l in range(len(questions_list_split)):
                    sum_simil = sum_simil + measure(val_list[k],questions_list_split[l])
                avg_simil = float(sum_simil)/len(questions_list_split)
                if val_list[k] in vocabulary:
                    vocab_zeros[vocabulary.index(val_list[k])] = avg_simil
            feature_vector.append(vocab_zeros)    
    
    
    
    
    
    print clf.predict(feature_vector)
    
if __name__=="__main__":
    main()