#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
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

#########################################################
from sklearn import svm
# Classifier optionsa
#classifier = svm.SVC( kernel='linear')
classifier = svm.SVC(C=10000)

# Reducing Trainging set size
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

time0 = time()
classifier.fit(features_train, labels_train);
time1 = time()
score = classifier.score(features_test, labels_test)
time_to_fit = time() - time1
time_to_train = time1 - time0

predictions = classifier.predict(features_test)

print "10: " + str(predictions[10])
print "26: " + str(predictions[26])
print "50: " + str(predictions[50])

count = 0
for prediction in predictions:
    if prediction == 1:
        count += 1

print "Chris's: " + str(count)

print "Accuracy: "
print score
print "Training Time: " + str(time_to_train) + " s"
print "Classification Time: " + str(time_to_fit) + " s" 
