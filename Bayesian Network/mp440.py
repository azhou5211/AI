from __future__ import division
import math
import numpy as np
import inspect
import sys

'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    for i in range (0,width):
        for j in range(0,height):
            if(digit_data[i][j]==0):
                features.append(False)
            else:
                features.append(True)
    return features

'''
Compute the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
# data is the list of raw data images
# label is the list of accompanying labels
# width and height are the dimension of the images

global prior0
global prior1
global prior2
global prior3
global prior4
global prior5
global prior6
global prior7
global prior8
global prior9
global prob0
prob0 = []
global prob1
prob1 = []
global prob2
prob2 = []
global prob3
prob3 = []
global prob4
prob4 = []
global prob5
prob5 = []
global prob6
prob6 = []
global prob7
prob7 = []
global prob8
prob8 = []
global prob9
prob9 = []

def initPrior(ZeroCount,OneCount,TwoCount,ThreeCount,FourCount,FiveCount,SixCount,SevenCount,EightCount,NineCount,n):
    global prior0
    global prior1
    global prior2
    global prior3
    global prior4
    global prior5
    global prior6
    global prior7
    global prior8
    global prior9
    prior0 = np.float64(ZeroCount/n)
    prior1 = np.float64(OneCount/n)
    prior2 = np.float64(TwoCount/n)
    prior3 = np.float64(ThreeCount/n)
    prior4 = np.float64(FourCount/n)
    prior5 = np.float64(FiveCount/n)
    prior6 = np.float64(SixCount/n)
    prior7 = np.float64(SevenCount/n)
    prior8 = np.float64(EightCount/n)
    prior9 = np.float64(NineCount/n)

def initProb(temp0,temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,ZeroCount,OneCount,TwoCount,ThreeCount,FourCount,FiveCount,SixCount,SevenCount,EightCount,NineCount):
    global prob0
    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6
    global prob7
    global prob8
    global prob9
    k = 0.01
    for i in range(0,len(temp0)):
        prob0.append(np.float64((temp0[i]+k)/(ZeroCount+k)))
        prob1.append(np.float64((temp1[i]+k)/(OneCount+k)))
        prob2.append(np.float64((temp2[i]+k)/(TwoCount+k)))
        prob3.append(np.float64((temp3[i]+k)/(ThreeCount+k)))
        prob4.append(np.float64((temp4[i]+k)/(FourCount+k)))
        prob5.append(np.float64((temp5[i]+k)/(FiveCount+k)))
        prob6.append(np.float64((temp6[i]+k)/(SixCount+k)))
        prob7.append(np.float64((temp7[i]+k)/(SevenCount+k)))
        prob8.append(np.float64((temp8[i]+k)/(EightCount+k)))
        prob9.append(np.float64((temp9[i]+k)/(NineCount+k)))

def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0): 
    N = len(label)
    n = int(N*(percentage/100))
    # Count the number of each label
    ZeroCount = 0
    OneCount = 0
    TwoCount = 0
    ThreeCount = 0
    FourCount = 0
    FiveCount = 0
    SixCount = 0
    SevenCount = 0
    EightCount = 0
    NineCount = 0
    for i in range(0,n):
        if(label[i]==0):
            ZeroCount = ZeroCount + 1
            continue
        if(label[i]==1):
            OneCount = OneCount + 1
            continue
        if(label[i]==2):
            TwoCount = TwoCount + 1
            continue
        if(label[i]==3):
            ThreeCount = ThreeCount + 1
            continue
        if(label[i]==4):
            FourCount = FourCount + 1
            continue
        if(label[i]==5):
            FiveCount = FiveCount + 1
            continue
        if(label[i]==6):
            SixCount = SixCount + 1
            continue
        if(label[i]==7):
            SevenCount = SevenCount + 1
            continue
        if(label[i]==8):
            EightCount = EightCount + 1
            continue
        if(label[i]==9):
            NineCount = NineCount + 1
            continue
    initPrior(ZeroCount,OneCount,TwoCount,ThreeCount,FourCount,FiveCount,SixCount,SevenCount,EightCount,NineCount,n)

    temp0 = [0] * (width*height)
    temp1 = [0] * (width*height)
    temp2 = [0] * (width*height)
    temp3 = [0] * (width*height)
    temp4 = [0] * (width*height)
    temp5 = [0] * (width*height)
    temp6 = [0] * (width*height)
    temp7 = [0] * (width*height)
    temp8 = [0] * (width*height)
    temp9 = [0] * (width*height)
    for i in range(0,n):
        features = feature_extractor(data[i],width,height)
        if(label[i]==0):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp0[j]+=1
        elif(label[i]==1):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp1[j]+=1
        elif(label[i]==2):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp2[j]+=1
        elif(label[i]==3):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp3[j]+=1
        elif(label[i]==4):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp4[j]+=1
        elif(label[i]==5):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp5[j]+=1
        elif(label[i]==6):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp6[j]+=1
        elif(label[i]==7):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp7[j]+=1
        elif(label[i]==8):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp8[j]+=1
        elif(label[i]==9):
            for j in range(0,len(features)):
                if (features[j]==1):
                    temp9[j]+=1
    initProb(temp0,temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,ZeroCount,OneCount,TwoCount,ThreeCount,FourCount,FiveCount,SixCount,SevenCount,EightCount,NineCount)

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    x0 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    for j in range(0,len(features)):
        if(features[j]==1):
            x0 += math.log(prob0[j])
            x1 += math.log(prob1[j])
            x2 += math.log(prob2[j])
            x3 += math.log(prob3[j])
            x4 += math.log(prob4[j])
            x5 += math.log(prob5[j])
            x6 += math.log(prob6[j])
            x7 += math.log(prob7[j])
            x8 += math.log(prob8[j])
            x9 += math.log(prob9[j])
        else:
            x0 += math.log(1-prob0[j])
            x1 += math.log(1-prob1[j])
            x2 += math.log(1-prob2[j])
            x3 += math.log(1-prob3[j])
            x4 += math.log(1-prob4[j])
            x5 += math.log(1-prob5[j])
            x6 += math.log(1-prob6[j])
            x7 += math.log(1-prob7[j])
            x8 += math.log(1-prob8[j])
            x9 += math.log(1-prob9[j])
    
    p0 = math.exp(math.log(prior0) + x0)
    p1 = math.exp(math.log(prior1) + x1)
    p2 = math.exp(math.log(prior2) + x2)
    p3 = math.exp(math.log(prior3) + x3)
    p4 = math.exp(math.log(prior4) + x4)
    p5 = math.exp(math.log(prior5) + x5)
    p6 = math.exp(math.log(prior6) + x6)
    p7 = math.exp(math.log(prior7) + x7)
    p8 = math.exp(math.log(prior8) + x8)
    p9 = math.exp(math.log(prior9) + x9)
    temp = {'0':p0,'1':p1,'2':p2,'3':p3,'4':p4,'5':p5,'6':p6,'7':p7,'8':p8,'9':p9}
    t = max(temp, key=temp.get)

    return int(t)

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):
    global prior0
    global prior1
    global prior2
    global prior3
    global prior4
    global prior5
    global prior6
    global prior7
    global prior8
    global prior9
    global prob0
    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6
    global prob7
    global prob8
    global prob9
    predicted=[]
    for i in range(0,len(data)):
        features = feature_extractor(data[i],width,height)
        t = compute_class(features)
        predicted.append(t)

    return predicted







        
    
