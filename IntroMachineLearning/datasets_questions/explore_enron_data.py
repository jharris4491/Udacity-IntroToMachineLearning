#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle, math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print("Number of people:", len(enron_data))
# print("Number of features:", len(list(enron_data.values())[0]))

print("--- POIs ---")
poi_count = 0
salary_count = 0
email_count = 0
nan_payments_count = 0
nan_payments_poi_count = 0
for person, features in list(enron_data.items()):
  if features['poi']:
    print(person)
    poi_count += 1
    if features['total_payments'] == 'NaN':
      nan_payments_poi_count += 1
  if math.isnan(float(features['salary'])) is False:
    salary_count += 1
  if features['email_address'] != 'NaN':
    email_count += 1
  if features['total_payments'] == 'NaN':
    nan_payments_count += 1
print("Total:", poi_count)
print("# People with Salaries:", salary_count)
print("# People with email adresses:", email_count)
print("% People with \'NaN\' for total_payments:", str(nan_payments_count / len(enron_data)))
print("% POI\'s with \'NaN\' for total_payments:", str(nan_payments_poi_count / len(enron_data)))

# print(enron_data['LAY KENNETH L'])