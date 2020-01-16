import numpy as np
import scipy as sc
import pandas as pd
from fractions import Fraction
def display_format(my_vector, my_decimal):
   return np.round((my_vector).astype(np.float), decimals=my_decimal)
my_dp = Fraction(1,5)
print(my_dp)
Mat = np.matrix([[0,1,1,1,1],
        [1/3,0,0,0,0],
        [1/3,0,0,0,0],
        [0,0,0,0,0],
        [1/3,0,0,0,0]])
Ex = np.zeros((5,5))

Ex[:] = my_dp


beta = 0.8
Al = beta * Mat + ((1-beta) * Ex)
r = np.matrix([my_dp, my_dp, my_dp, my_dp, my_dp])
r = np.transpose(r)

previous_r = r
count=0
for i in range(1,100):
   r = Al * r
   print (r)
   if (previous_r==r).all():
      break
   previous_r = r
   count=count+1

print(count)
print ("Final:\n", display_format(r,3))
print ("sum", np.sum(r))
p=r.item(0)
print(p)