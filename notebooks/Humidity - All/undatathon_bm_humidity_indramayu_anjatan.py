#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pyextremes


# In[3]:


conda install -c conda-forge pyextremes


# In[4]:


from pyextremes import EVA, __version__
print("pyextremes", __version__)


# In[75]:


import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.stats.api as sms


# In[59]:


rawdata = (
    pd
    .read_csv("C:/Users/bagoe/OneDrive/Documents/undatathon2023/humi_prec.csv", parse_dates=True)
    .sort_index(ascending=True)
    .dropna()
)
rawdata["date"] = pd.to_datetime(rawdata["date"])
rawdata.head()
rawdata.tail()


# In[60]:


data_anjatan = rawdata.loc[rawdata['bps_kecamatan_nama'] == 'ANJATAN']


# In[61]:


data_anjatan.tail()


# In[62]:


humidity_anjatan = data_anjatan[['date', 'humidity']].set_index('date')


# In[63]:


humidity_anjatan.tail()


# In[64]:


humidity_anjatan.plot()


# In[65]:


model = EVA(data = humidity_anjatan.squeeze())
model


# In[66]:


model.get_extremes(
    method="BM",
    extremes_type="high",
    block_size="7D",
    errors="raise",
)
model


# In[67]:


model.plot_extremes()


# In[68]:


model.fit_model()
model


# In[69]:


model.plot_diagnostic(alpha=0.95)


# In[70]:


model.plot_return_values(
    return_period=np.logspace(0.01, 2, 100),
    return_period_size="183D",
    alpha=0.95,
)


# In[71]:


summary = model.get_summary(
    return_period=[1,2,3,4,  5,6,7,8,  9,10,11,12,  13,14,15,16,  17,18,19,20,  21,22,23,24],
    alpha=0.95,
    n_samples=1000,
)
summary


# In[72]:


calc_data = data_anjatan[['date', 'humidity']]
calc_data.tail()


# In[73]:


jul_2022 = (calc_data['date'] >= '2022-07-01') & (calc_data['date'] <= '2022-07-31')
df_jul_2022 = calc_data.loc[jul_2022]
df_jul_2022.head()


# In[82]:


df_jul_2022['humidity'].quantile([0.25, 0.75])


# In[83]:


aug_2022 = (calc_data['date'] >= '2022-08-01') & (calc_data['date'] <= '2022-08-31')
df_aug_2022 = calc_data.loc[aug_2022]
df_aug_2022.head()
df_aug_2022['humidity'].quantile([0.25, 0.75])


# In[84]:


sep_2022 = (calc_data['date'] >= '2022-09-01') & (calc_data['date'] <= '2022-09-30')
df_sep_2022 = calc_data.loc[sep_2022]
df_sep_2022.head()
df_sep_2022['humidity'].quantile([0.25, 0.75])


# In[86]:


oct_2022 = (calc_data['date'] >= '2022-10-01') & (calc_data['date'] <= '2022-10-31')
df_oct_2022 = calc_data.loc[oct_2022]
df_oct_2022.head()
df_oct_2022['humidity'].quantile([0.25, 0.75])


# In[87]:


nov_2022 = (calc_data['date'] >= '2022-11-01') & (calc_data['date'] <= '2022-11-30')
df_nov_2022 = calc_data.loc[nov_2022]
df_nov_2022.head()
df_nov_2022['humidity'].quantile([0.25, 0.75])


# In[88]:


dec_2022 = (calc_data['date'] >= '2022-12-01') & (calc_data['date'] <= '2022-12-31')
df_dec_2022 = calc_data.loc[dec_2022]
df_dec_2022.head()
df_dec_2022['humidity'].quantile([0.25, 0.75])


# In[ ]:




