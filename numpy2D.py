import numpy as np
height = [1.79,2.43,2.01,1.89,1.95,2.3]
weight = [78,65.4,70.3,68.77,80.1,78]
np_height = np.array(height)
np_weight = np.array(weight)

h_w = [[1.79,2.43,2.01,1.89,1.95,2.3],[78,65.4,70.3,68.77,80.1,78]]
np_h_w = np.array(h_w)
#np_h_w is now a 2D array containing height in the first row and weight in the second row
print("The 2D array is: \n",np_h_w)
print("\n")

#selecting a small 2D array out of items
small_array = np_h_w[:,1:3]
print("The small 2D array is: \n",small_array)

#selecting a whole row
print("A whole row being printed is: \n",np_h_w[1:])

#the number of rows and columns is given bytearray
print("The number of rows and columns are: \n",np_h_w.shape)