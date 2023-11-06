#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyextremes import EVA, __version__
print("pyextremes", __version__)


# In[2]:


import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.stats.api as sms


# In[3]:


rawdata = (
    pd
    .read_csv("C:/Users/bagoe/OneDrive/Documents/undatathon2023/humi_prec.csv", parse_dates=True)
    .sort_index(ascending=True)
    .dropna()
)
rawdata["date"] = pd.to_datetime(rawdata["date"])
rawdata.head()
rawdata.tail()


# In[4]:


data = rawdata.loc[rawdata['bps_kecamatan_nama'] == 'LELEA']


# In[5]:


data.tail()


# In[6]:


prec = data[['date', 'precipitation']].set_index('date')


# In[7]:


prec.tail()


# In[8]:


prec.plot()


# In[9]:


model = EVA(data = prec.squeeze())
model


# In[10]:


model.get_extremes(
    method="BM",
    extremes_type="high",
    block_size="7D",
    errors="raise",
)
model


# In[11]:


model.plot_extremes()


# In[12]:


model.fit_model()
model


# In[13]:


model.plot_diagnostic(alpha=0.95)


# In[14]:


model.plot_return_values(
    return_period=np.logspace(0.01, 2, 100),
    return_period_size="100D",
    alpha=0.95,
)


# In[15]:


summary = model.get_summary(
    return_period=[1,2,3,4,  5,6,7,8,  9,10,11,12,  13,14,15,16,  17,18,19,20,  21,22,23,24],
    alpha=0.95,
    n_samples=1000,
)
summary


# In[16]:


model.get_extremes(
    method="BM",
    extremes_type="low",
    block_size="7D",
    errors="raise",
)
model


# In[17]:


model.plot_extremes()


# In[18]:


model.fit_model()
model


# In[19]:


model.plot_diagnostic(alpha=0.95)


# In[20]:


model.plot_return_values(
    return_period=np.logspace(0.01, 2, 100),
    return_period_size="100D",
    alpha=0.95,
)


# In[21]:


summary = model.get_summary(
    return_period=[1,2,3,4,  5,6,7,8,  9,10,11,12,  13,14,15,16,  17,18,19,20,  21,22,23,24],
    alpha=0.95,
    n_samples=1000,
)
summary


# In[22]:


calc_data = data[['date', 'precipitation']]
calc_data.tail()


# In[23]:


jul_2022 = (calc_data['date'] >= '2022-07-01') & (calc_data['date'] <= '2022-07-31')
df_jul_2022 = calc_data.loc[jul_2022]
df_jul_2022.head()


# In[24]:


sms.DescrStatsW(df_jul_2022['precipitation']).tconfint_mean()


# In[25]:


df_jul_2022['precipitation'].quantile([0.25, 0.75])


# In[26]:


aug_2022 = (calc_data['date'] >= '2022-08-01') & (calc_data['date'] <= '2022-08-31')
df_aug_2022 = calc_data.loc[aug_2022]
df_aug_2022.head()


# In[27]:


sms.DescrStatsW(df_aug_2022['precipitation']).tconfint_mean()


# In[28]:


df_aug_2022['precipitation'].quantile([0.25, 0.75])


# In[29]:


sep_2022 = (calc_data['date'] >= '2022-09-01') & (calc_data['date'] <= '2022-09-30')
df_sep_2022 = calc_data.loc[sep_2022]
df_sep_2022.head()


# In[30]:


sms.DescrStatsW(df_sep_2022['precipitation']).tconfint_mean()


# In[31]:


df_sep_2022['precipitation'].quantile([0.25, 0.75])


# In[32]:


oct_2022 = (calc_data['date'] >= '2022-10-01') & (calc_data['date'] <= '2022-10-31')
df_oct_2022 = calc_data.loc[oct_2022]
df_oct_2022.head()


# In[33]:


sms.DescrStatsW(df_oct_2022['precipitation']).tconfint_mean()


# In[34]:


df_oct_2022['precipitation'].quantile([0.25, 0.75])


# In[35]:


nov_2022 = (calc_data['date'] >= '2022-11-01') & (calc_data['date'] <= '2022-11-30')
df_nov_2022 = calc_data.loc[nov_2022]
df_nov_2022.head()


# In[36]:


sms.DescrStatsW(df_nov_2022['precipitation']).tconfint_mean()


# In[37]:


df_nov_2022['precipitation'].quantile([0.25, 0.75])


# In[38]:


dec_2022 = (calc_data['date'] >= '2022-12-01') & (calc_data['date'] <= '2022-12-31')
df_dec_2022 = calc_data.loc[dec_2022]
df_dec_2022.head()


# In[39]:


sms.DescrStatsW(df_dec_2022['precipitation']).tconfint_mean()


# In[40]:


df_dec_2022['precipitation'].quantile([0.25, 0.75])


# In[ ]:




