# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:53:53 2021

@author: Pramod.Surve
"""

import pandas as pd

cars = {'Brand': ['Civic', 'Corolla'],
      'Color': ['Blue', 'Grey']
      }

df = pd.DataFrame(cars, columns= ['Brand', 'Color'])

print (df)

print("Time of execution is", now())
