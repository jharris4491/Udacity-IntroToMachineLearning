#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
t0 = time()
classifier.fit(features_train, labels_train)
t1 = time()
predicted_labels = classifier.predict(features_test)
t2 = time()

time_to_fit = t1 - t0
time_to_predict = t2 - t1
print "Time to train: ", round(time_to_fit, 3), "s"
print "Time to predict: ", round(time_to_predict, 3), "s"

accuracy = classifier.score(features_test, labels_test)
print"Accuracy: ", accuracy

#########################################################


