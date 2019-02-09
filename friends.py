import statistics

def mean_num_friends(x):
    # TODO
    a=0
    for friends in x: a+=friends
    return (a/len(x))

def median_num_friends(x):
    # TODO
    return statistics.median(x)

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))