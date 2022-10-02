
import numpy as np
import nltk
#nltk.download('punkt')
from nltk import word_tokenize
import csv


path = './Data/coca_ngrams_x3w.csv'
f= open(path, 'r')

reader3 = csv.reader(f, delimiter=',')
data3 = np.array(list(reader3))

path = './Data/coca_ngrams_x2w.csv'
f= open(path, 'r')

reader2 = csv.reader(f, delimiter=',')
data2 = np.array(list(reader2))

path = './Data/coca_ngrams_x4w.csv'
f= open(path, 'r')

reader4 = csv.reader(f, delimiter=',')
data4 = np.array(list(reader4))
print(data4)

while True :
    
    t = input('text : ')
    

    print('-----------------------------------------------------------------------------------\n')
    print(t)
    print('\n-----------------------------------------------------------------------------------')
    dataText = word_tokenize(t)
    last2 = dataText[-1:]
    last3 = dataText[-2:]
    last4 = dataText[-3:]
    
    r = np.where(data2 ==  last2[0])
    
    i=0
    while i<20 and len(r[0])>(i+1):
        index = r[0][i]
        
        if data2[index][1] ==last2[0]:
            print(data2[index][2])
            i=i+4
        i=i+1  
        
    if len(last3)>0 :   
        l = len(last3)
        if l==2 :
            r = np.where(data3 ==  last3[1])
            i=0
            while i<20 and len(r[0])>(i+1): 
                index = r[0][i]
                
                if data3[index][2] ==last3[1] and data3[index][1] ==last3[0] :
                    print(data3[index][3])
                    i=i+4
                if data3[index][1] ==last3[1] :
                    print(data3[index][2] +' '+data3[index][3])  
                    i=i+4 
                i=i+1
        
        if l ==1:
            r = np.where(data3 ==  last3[0])
            i=0
            while i<20 and len(r[0])>(i+1): 
                index = r[0][i]
                
                if data3[index][2] ==last3[0]  :
                    print(data3[index][3])
                    i=i+4
                if data3[index][1] ==last3[0] :
                    print(data3[index][2] +' '+data3[index][3])  
                    i=i+4 
                i=i+1
        
    if len(last4) >0 :
        l = len(last4)
        if l==3 :
            r = np.where(data4 ==  last4[0])
            i=0
            while i<20 and len(r[0])>(i+1):
                index = r[0][i] 
                if data4[index][1] == last4[0]  and data4[index][2] == last4[1] and data4[index][3] ==last4[2] :
                    print(data4[index][4])
                    i=i+4
                else: 
                    if  data4[index][1] == last4[1] and data4[index][2] ==last4[2]   :
                        print(data4[index][3] +' '+ data4[index][4])
                        i=i+4
                    else:    
                        if  data4[index][1] == last4[2]:
                            print(data4[index][2] +' '+ data4[index][3] +' '+data4[index][4]) 
                            i=i+4 
                i=i+1                
        else:
            if l==2:
                r = np.where(data4 ==  last4[0])
                i=0
                while i<20 and len(r[0])>(i+1) :
                    index = r[0][i] 
                    if data4[index][1] == last4[0] and data4[index][2] == last4[1]:
                        print(data4[index][3] +' '+ data4[index][4])
                        i=i+4
                    else:
                        if data4[index][1] == last4[1]  :
                            print( data4[index][2]+' ' +data4[index][3] +' '+ data4[index][4])
                            i=i+4
                    i=i+1
            else:
                if l==1:
                    r = np.where(data4 ==  last4[0])
                    i=0
                    while i<20 and len(r[0])>(i+1) :
                        index = r[0][i]
                        if data4[index][1] == last4[0]  :
                            print( data4[index][2]+' ' +data4[index][3] +' '+ data4[index][4])
                            i=i+4
                        i=i+1    



    # if len(last3)>1 :
    #     r = np.where(data3 ==  last3[1])
    #     i=0
    #     while i<10 and len(r[0])>(i+1): 
    #         index = r[0][i]
    #         print('in grams :' + data3[index][1])
    #         if data3[index][2] ==last3[1] :
    #             print(data3[index][3])
    #             i=i+4
    #         if data3[index][1] ==last3[1]  :
    #             print(data3[index][2] +' '+data3[index][3])
                
    #             i=i+4 
    #         i=i+1 
        
    
    
    
    


    print('\n-----------------------------------------------------------------------------------')
