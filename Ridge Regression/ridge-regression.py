import csv
import sys

# _lambda , sigma2, X,Y,X_test = sys.argv[1:]
mylist=[1,2,3,4]
with open("test.csv", 'w') as myfile:
    wr=csv.writer(myfile) #, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)
print("done")