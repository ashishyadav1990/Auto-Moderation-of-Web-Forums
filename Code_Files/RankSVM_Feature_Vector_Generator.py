# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 12:50:34 2015

@author: Ashish Yadav
"""



import pandas as pd


def measure(word1,word2):
    if word1==word2:
        return 1
    else:
        return 0

def main():
    df = pd.read_csv('Data_Formatted2.csv')
    Y = df.values

    num_of_rows = Y.shape[0]
    ans = ""
    for i in range(num_of_rows):
        if Y[i,3] != 1:
            ans = ans + Y[i,3]
            
    word_list = ans.split()
    unique_words = set(word_list)
    vocabulary = list(unique_words)
    
    questions_list = []
    answers_list = []
    answers = []
    label = []
    for i in range(num_of_rows):
        if Y[i,1] == 1:
            answers_list.append(answers)
            questions_list.append(Y[i,3])
            answers2 = []
        else:
            answers2.append(Y[i,3])
            label.append(Y[i,6])
    
    
    answers_list.append(answers2)
    del answers_list[0]
    feature_vector = []
    
    for i in range(len(answers_list)):
        questions_list_split = questions_list[i].split()
        lis = answers_list[i]
        for j in range(len(lis)):
            val = lis[j]
            val_list = val.split()
            vocab_zeros = [0] * len(vocabulary)
            for k in range(len(val_list)):
                sum_simil = 0;
                for l in range(len(questions_list_split)):
                    sum_simil = sum_simil + measure(val_list[k],questions_list_split[l])
                avg_simil = float(sum_simil)/len(questions_list_split)
                if val_list[k] in vocabulary:
                    vocab_zeros[vocabulary.index(val_list[k])] = avg_simil
            feature_vector.append(vocab_zeros)
            
    print feature_vector
    
    f = open('workfile.dat', 'a')
    for i in range(len(feature_vector)):
        str_feature=str(label[i]) + " " + "qid:1 "
        list_feature = feature_vector[i]
        for j in range(len(list_feature)):
            str_feature += str(j)+":"+str(float(list_feature[j]))+ " "
        str_feature+='\n'
        f.write(str_feature)
     

    f.close()                       
                
    #print answers_list
    #print answers2
    #print questions_list
    
if __name__ == "__main__":
    main()
    

    
    
    