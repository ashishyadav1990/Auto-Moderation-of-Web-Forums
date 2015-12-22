# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:47:33 2015

@author: Ashish Yadav
"""

import pandas as pd

def main():
    df = pd.read_csv('TestEconomicsandLaw.csv')
    Y = df.values
    num_of_rows = Y.shape[0]
    list_scores = []
    for i in range(num_of_rows):
        if Y[i,0]!=1 and isinstance(Y[i,1],basestring):
            list_scores.append(Y[i,2])
     

    list_pred = []
    count = 0
    f = open('EandLPredictions','r')
    for line in f:
        list_pred.append(float(line))
        
    print len(list_pred)
    print len(list_scores)
    
    for i in range(len(list_scores)-1):
        for j in range(len(list_scores)-i-1):
            if list_scores[j]>list_scores[j+1]:
                temp = list_scores[j]
                list_scores[j]=list_scores[j+1]
                list_scores[j+1]=temp
                
                temp = list_pred[j]
                list_pred[j] = list_pred[j+1]
                list_pred[j+1] = temp
                
    '''        
    for i in range(len(list_scores)-1):
        if((list_scores[i]>list_scores[i+1] and list_pred[i]>list_pred[i+1])
        or (list_scores[i]<list_scores[i+1] and list_pred[i]<list_pred[i+1])
        or (list_scores[i]==list_scores[i+1] and list_pred[i]==list_pred[i+1])):
            count = count + 1
    '''
    
    print list_scores
    print list_pred

    for i in range(len(list_pred)-1):
        if list_pred[i]>list_pred[i+1]:
            count = count+1
            
    accuracy = float((len(list_pred)-count))/(len(list_pred))
    accuracy = accuracy*100
    print accuracy
    print count
            
            
    
        
    
    
    
if __name__=="__main__":
    main()