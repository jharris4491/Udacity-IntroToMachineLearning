#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb+") )
features = ["salary", "bonus"]

data_dict.pop("TOTAL", 0)

data = featureFormat(data_dict, features)


### your code below

from queue import PriorityQueue
pq = PriorityQueue()


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    pq.put((salary, bonus))

while not pq.empty():
    print(pq.get())

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
