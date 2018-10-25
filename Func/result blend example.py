import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
#1m_4a_BL_r2_lgb_1
import os
"""
d1=pd.read_csv('./input/lgsub_d.csv')##LGBM
d2=pd.read_csv('./input/lgsub_c.csv')##af
d3=pd.read_csv('./input/lgsub_point.csv')
print(d1.head())
print(d2.head())
print(d3.head())
print(d3.shape)
train=pd.DataFrame()
train["d1"]=d1["deal_probability"]
train["d2"]=d2["deal_probability"]
target=d3.deal_probability.copy()
print(train.head())
print(target.head())
print(train.shape)
print(target.shape)
from scipy.sparse import hstack, csr_matrix
X=csr_matrix(train.values)
y=csr_matrix(target)
lgbm_params =  {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'rmse',
    # 'max_depth': 15,
    'num_leaves': 270,
    'feature_fraction': 0.5,
    'bagging_fraction': 0.75,
    'bagging_freq': 2,
    'learning_rate': 0.016,
    'verbose': 0
}

lgtrain = lgb.Dataset(X, y,
                    feature_name=tfvocab,
                    categorical_feature = categorical)

"""

d2=pd.read_csv('./input/blend_11.csv')
d1=pd.read_csv('./input/lgsub_lgbpre_blend_0.csv')

d2['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d1['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d2['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d1['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d2['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d1['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d2['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d1['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2


d2['deal_probability']=(d1['deal_probability']+d2['deal_probability'])/2
d2.to_csv("blend_12.csv", index=False)
