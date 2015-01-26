#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, write_out,write_init

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################
def print_picture(prefix, clf):
  try:
    filename = prefix + ".png"
    prettyPicture(clf, features_test, labels_test, filename)
  except NameError:
    pass

results_file = "output.txt"
write_init(results_file)

#Nearest Neighbors
print("Starting Nearest Neighbors...")
nn_string = "nn_"
nearest_neighbors_weights = ['uniform', 'distance']
nearest_neighbors_algorithms = ['ball_tree', 'kd_tree', 'brute']
nearest_neighbors_n = [5 * i for i in range(1,10)]




from sklearn.neighbors import KNeighborsClassifier
from time import time

for x in range(0, len(nearest_neighbors_weights)):
  weights = nearest_neighbors_weights[x]

  for y in range(0, len(nearest_neighbors_algorithms)):
    algorithm = nearest_neighbors_algorithms[y]

    for z in range(0, len(nearest_neighbors_n)):
      n_neighbors = nearest_neighbors_n[z]
      n_neighbors_str = str(n_neighbors)
      prefix = nn_string + weights + "_" + algorithm + "_" + n_neighbors_str

      clf  = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, algorithm=algorithm)

      start_time = time()
      clf.fit(features_train, labels_train)
      runtime = time() - start_time

      acc = clf.score(features_test, labels_test)

      write_out(acc, runtime, results_file, prefix)

      complete = x * len(nearest_neighbors_algorithms) * len(nearest_neighbors_n) + y * len(nearest_neighbors_n) + z + 1.0
      total = len(nearest_neighbors_n) * len(nearest_neighbors_algorithms) * len(nearest_neighbors_weights)

      print("%", (complete / total) * 100, " Completed! Last run took ", runtime, "s\n")
      print_picture(prefix, clf)

#Random Forrest
print('Starting Random Forrest...')
from sklearn.ensemble import RandomForestClassifier
random_forrest_str = "rf_"
n_estimators_arr = [5 * i for i in range(1,10)]
max_features_arr = ['sqrt', 'log2', None]
min_samples_leaf_arr = [i for i in range(1,5)]

for x in range(0, len(max_features_arr)):
  max_features = max_features_arr[x]
  if (max_features == None):
    max_features_str = 'None'
  else:
    max_features_str = max_features

  for y in range(0, len(min_samples_leaf_arr)):
    min_samples_leaf = min_samples_leaf_arr[y]
    min_samples_leaf_str = str(min_samples_leaf)

    for z in range(0, len(n_estimators_arr)):
      n_estimators = n_estimators_arr[z]
      n_estimators_str = str(n_estimators)
      prefix = random_forrest_str + max_features_str + "_" + min_samples_leaf_str + "_" + n_estimators_str
      clf  = RandomForestClassifier(max_features=max_features, min_samples_leaf=min_samples_leaf, n_estimators=n_estimators)

      start_time = time()
      clf.fit(features_train, labels_train)
      runtime = time() - start_time

      acc = clf.score(features_test, labels_test)

      write_out(acc, runtime, results_file, prefix)

      complete = x * len(min_samples_leaf_arr) * len(n_estimators_arr) + y * len(n_estimators_arr) + z + 1.0
      total = len(n_estimators_arr) * len(min_samples_leaf_arr) * len(max_features_arr)

      print("%", (complete / total) * 100, " Completed! Last run took ", runtime, "s\n")
      print_picture(prefix, clf)



#Ada Boost
print("Starting Ada Boost...\n")
from sklearn.ensemble import AdaBoostClassifier
ada_boost_str = "ab_"
algorithm_arr = ['SAMME', 'SAMME.R']
n_estimators_arr = [10 * i for i in range(1,20)]


for x in range(0, len(algorithm_arr)):
  algorithm = algorithm_arr[x]

  for y in range(0, len(n_estimators_arr)):
    n_estimators = n_estimators_arr[y]
    n_estimators_str = str(n_estimators)
    prefix = ada_boost_str + algorithm + "_" + n_estimators_str
    clf  = AdaBoostClassifier(algorithm=algorithm, n_estimators=n_estimators)

    start_time = time()
    clf.fit(features_train, labels_train)
    runtime = time() - start_time

    acc = clf.score(features_test, labels_test)

    write_out(acc, runtime, results_file, prefix)

    complete = x * len(n_estimators_arr) + y + 1.0
    total = len(n_estimators_arr) * len(algorithm_arr)

    print("%", (complete / total) * 100, " Completed! Last run took ", runtime, "s\n")
    print_picture(prefix, clf)

