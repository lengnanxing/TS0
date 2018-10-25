import numpy as np
import pandas as pd
import math
import time
import os.path

d1=pd.read_csv('./input/blend_4_to_1_sub.csv')
d2=pd.read_csv('./input/blend_4_to_1_sub_1.csv')
d3=pd.read_csv('./input/blend_4_to_1_sub_2.csv')
d4=pd.read_csv('./input/sub_1m_1a.csv')
d5=pd.read_csv('./input/sub_sub_1.csv')
d6=pd.read_csv('./input/1m_4a.csv')
d7=pd.read_csv('./input/sub_unknown.csv')
d8=pd.read_csv('./input/sub_un_1m_4a.csv')
def rmse(y, y0):
    assert len(y) == len(y0)
    return np.sqrt(np.mean(np.power((y - y0), 2)))
print("rmse ")
print (rmse(d4['deal_probability'], d8['deal_probability']))

"""
print (rmse(d1['deal_probability'], d2['deal_probability']),
rmse(d1['deal_probability'], d3['deal_probability']),
rmse(d1['deal_probability'], d4['deal_probability']),
rmse(d1['deal_probability'], d5['deal_probability']),
       )
print("rmse with d2")
print(rmse(d2['deal_probability'], d3['deal_probability']),
rmse(d2['deal_probability'], d4['deal_probability']),
rmse(d2['deal_probability'], d5['deal_probability']),
)

print("rmse with d3")
print (rmse(d3['deal_probability'], d4['deal_probability']),
rmse(d3['deal_probability'], d5['deal_probability']),
              )

print("rmse with d4")
print (rmse(d4['deal_probability'], d5['deal_probability']),
       )

#d1, d2,
"""""