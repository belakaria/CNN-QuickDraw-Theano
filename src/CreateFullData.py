## -*- coding: utf-8 -*-
#"""
#Created on Thu Nov 23 20:14:41 2017
#
#@author: Syrine Belakaria
#"""
import gzip, cPickle
#import numpy as np
#import random
#
#def load_data(filename,i):
#    file_data = np.load(filename)
#    random.shuffle(file_data)
#    num = int(np.ceil(len(file_data)*0.3))
#    num1= int(np.floor(len(file_data)*0.7))
#    if num  % 2 != 0: 
#        num=num-1
#        num1=num1+1
#    training_data_content=file_data[0:num1-1]
#    testing_data_content=file_data[num1:num1+(num/2)]
#    validation_data_content=file_data[num1+1+(num/2):len(file_data)]
#    training_data_label=i*np.ones(len(training_data_content)).astype(int)
#    testing_data_label=i*np.ones(len(testing_data_content)).astype(int)
#    validation_data_label=i*np.ones(len(validation_data_content)).astype(int)    
#    return(training_data_content,testing_data_content,validation_data_content,training_data_label,testing_data_label,validation_data_label)
#
#brains_tr_data,brains_ts_data,brains_va_data,brains_tr_lab,brains_ts_lab,brains_va_lab=load_data('../data/brain.npy',0)
#arms_tr_data,arms_ts_data,arms_va_data,arms_tr_lab,arms_ts_lab,arms_va_lab=load_data('../data/arm.npy',1)
#ears_tr_data,ears_ts_data,ears_va_data,ears_tr_lab,ears_ts_lab,ears_va_lab=load_data('../data/ear.npy',2)
#eyes_tr_data,eyes_ts_data,eyes_va_data,eyes_tr_lab,eyes_ts_lab,eyes_va_lab=load_data('../data/eye.npy',3)
#faces_tr_data,faces_ts_data,faces_va_data,faces_tr_lab,faces_ts_lab,faces_va_lab=load_data('../data/face.npy',4)
#mouths_tr_data,mouths_ts_data,mouths_va_data,mouths_tr_lab,mouths_ts_lab,mouths_va_lab=load_data('../data/mouth.npy',5)
#tooth_tr_data,tooth_ts_data,tooth_va_data,tooth_tr_lab,tooth_ts_lab,tooth_va_lab=load_data('../data/tooth.npy',6)
#moustache_tr_data,moustache_ts_data,moustache_va_data,moustache_tr_lab,moustache_ts_lab,moustache_va_lab=load_data('../data/moustache.npy',7)
#leg_tr_data,leg_ts_data,leg_va_data,leg_tr_lab,leg_ts_lab,leg_va_lab=load_data('../data/leg.npy',8)
#finger_tr_data,finger_ts_data,finger_va_data,finger_tr_lab,finger_ts_lab,finger_va_lab=load_data('../data/finger.npy',9)
##--------------------------------------------------------------------------------------------------------------------------------------------------------
#trainingcontentfull=np.concatenate((brains_tr_data,arms_tr_data,ears_tr_data,eyes_tr_data,faces_tr_data,mouths_tr_data,tooth_tr_data,moustache_tr_data,leg_tr_data,finger_tr_data),axis=0)
##trainingcontentfull=np.concatenate((brains_tr_data,arms_tr_data,ears_tr_data),axis=0)
#n=len(trainingcontentfull)
#trainingcontentfull=trainingcontentfull[0:n-(n % 10)]
#traininglabfull=np.concatenate((brains_tr_lab,arms_tr_lab,ears_tr_lab,eyes_tr_lab,faces_tr_lab,mouths_tr_lab,tooth_tr_lab,moustache_tr_lab,leg_tr_lab,finger_tr_lab),axis=0)
##traininglabfull=np.concatenate((brains_tr_lab,arms_tr_lab,ears_tr_lab),axis=0)
#traininglabfull=traininglabfull[0:n-(n % 10)]
#trainingdatafull=[]
#
#trainingdatafull=zip(trainingcontentfull,traininglabfull)
#random.shuffle(trainingdatafull)
#trainingcontentfull1=[]
#traininglabfull1=[]
#for element in trainingdatafull:    
#    trainingcontentfull1.append(element[0])
#    traininglabfull1.append(element[1])
#trainingdatafull1=[]
#trainingdatafull1.append(trainingcontentfull1)
#trainingdatafull1.append(traininglabfull1)
#trainingdatafull1=tuple(trainingdatafull1)
#
###--------------------------------------------------------------------------------------------------------------------------------------------------------
#testingcontentfull=np.concatenate((brains_ts_data,arms_ts_data,ears_ts_data,eyes_ts_data,faces_ts_data,mouths_ts_data,tooth_ts_data,moustache_ts_data,leg_ts_data,finger_ts_data),axis=0)
##testingcontentfull=np.concatenate((brains_ts_data,arms_ts_data,ears_ts_data),axis=0)
#n=len(testingcontentfull)
#testingcontentfull=testingcontentfull[0:n-(n % 10)]
#testinglabfull=np.concatenate((brains_ts_lab,arms_ts_lab,ears_ts_lab,eyes_ts_lab,faces_ts_lab,mouths_ts_lab,tooth_ts_lab,moustache_ts_lab,leg_ts_lab,finger_ts_lab),axis=0)
##testinglabfull=np.concatenate((brains_ts_lab,arms_ts_lab,ears_ts_lab),axis=0)
#testinglabfull=testinglabfull[0:n-(n % 10)]
#testingdatafull=[]
#
#testingdatafull=zip(testingcontentfull,testinglabfull)
#random.shuffle(testingdatafull)
#testingcontentfull1=[]
#testinglabfull1=[]
#for element in testingdatafull:    
#    testingcontentfull1.append(element[0])
#    testinglabfull1.append(element[1])
#
#testingdatafull1=[]
#testingdatafull1.append(testingcontentfull1)
#testingdatafull1.append(testinglabfull1)
#testingdatafull1=tuple(testingdatafull1)
####--------------------------------------------------------------------------------------------------------------------------------------------------------
#validationcontentfull=np.concatenate((brains_va_data,arms_va_data,ears_va_data,eyes_va_data,faces_va_data,mouths_va_data,tooth_va_data,moustache_va_data,leg_va_data,finger_va_data),axis=0)
##validationcontentfull=np.concatenate((brains_va_data,arms_va_data,ears_va_data),axis=0)
#n=len(validationcontentfull)
#validationcontentfull=validationcontentfull[0:n-(n % 10)]
#validationlabfull=np.concatenate((brains_va_lab,arms_va_lab,ears_va_lab,eyes_va_lab,faces_va_lab,mouths_va_lab,tooth_va_lab,moustache_va_lab,leg_va_lab,finger_va_lab),axis=0)
##validationlabfull=np.concatenate((brains_va_lab,arms_va_lab,ears_va_lab),axis=0)
#validationlabfull=validationlabfull[0:n-(n % 10)]
#validationdatafull=[]
#validationdatafull=zip(validationcontentfull,validationlabfull)
#random.shuffle(validationdatafull)
#validationcontentfull1=[]
#validationlabfull1=[]
#for element in validationdatafull:    
#    validationcontentfull1.append(element[0])
#    validationlabfull1.append(element[1])
#
#validationdatafull1=[]
#validationdatafull1.append(validationcontentfull1)
#validationdatafull1.append(validationlabfull1)
#validationdatafull1=tuple(validationdatafull1)
#
#dataset = [trainingdatafull1, validationdatafull1, testingdatafull1]
#
#f = gzip.open('../data/quickdrawfull.pkl.gz','wb')
#cPickle.dump(dataset, f, protocol=2)
#f.close()
f = gzip.open("../data/quickdrawfull.pkl.gz", 'rb')
training_data, validation_data, test_data = cPickle.load(f)
f.close()