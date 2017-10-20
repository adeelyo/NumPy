import numpy as np
height = [1.79,2.43,2.01,1.89,1.95,2.3]
weight = [78,65.4,70.3,68.77,80.1,78]
np_height = np.array(height)
np_weight = np.array(weight)
print("Type of np_height is: ",type(np_height),"\nType of np_weight is: ",type(np_weight),"\nType of height list is: ",type(height))
bmi = np_weight / np_height ** 2
print("Type of bmi is: ",type(bmi),"\n and its values are: ",bmi)

# printing the bmi which are greater than 20 in boolean form
print("printing the bmi which are greater than 20 in boolean form")
print(bmi>20)
print("\n\n")
#printing the bmi which are greatetr than 20 
print("Printing just the bmi which are greater than 20 ")
print(bmi[bmi>20])