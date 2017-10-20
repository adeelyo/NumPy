import numpy as np
height = np.round(np.random.normal(1.75,0.5,15),2)
weight = np.round(np.random.normal(68.5,1.2,15),2)
np_generated = np.column_stack((height,weight))

print("The generated 2 d array is : \n",np_generated,"\nits type is: ",type(np_generated))

#finding the sum of row
sum_height = np.sum(np_generated[:,0])
sum_weight = np.sum(np_generated[:,1])
#sorting the generated array using numpy method sort()
sorted_height = np.sort(np_generated[:,0])
sorted_weight = np.sort(np_generated[:,1])

print("The sorted heights of generated array is: \n",sorted_height,"\nthe sorted weights of generated array is: \n",sorted_weight)