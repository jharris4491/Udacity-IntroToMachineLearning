#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """

    cleaned_data = []

    ### your code goes here
    from queue import PriorityQueue
    pq = PriorityQueue()
    
    ages_list = ages.tolist()
    predictions_list = predictions.tolist()
    net_worths_list = net_worths.tolist()

    for i in range(0, len(ages)):
        pq.put((abs(predictions_list[i][0] - net_worths_list[i][0]), (ages_list[i][0], net_worths_list[i][0])))

    for i in range (0, len(ages) - int(len(ages) / 10)):
        val = pq.get()
        print(val)
        cleaned_data.append((val[1][0], val[1][1], val[0]))

    print(cleaned_data)
    return cleaned_data

