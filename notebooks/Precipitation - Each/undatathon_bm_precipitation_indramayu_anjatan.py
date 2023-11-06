#!/usr/bin/env python
# coding: utf-8

# In[107]:


from pyextremes import EVA, __version__
print("pyextremes", __version__)


# In[108]:


import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.stats.api as sms


# In[109]:


rawdata = (
    pd
    .read_csv("C:/Users/bagoe/OneDrive/Documents/undatathon2023/humi_prec.csv", parse_dates=True)
    .sort_index(ascending=True)
    .dropna()
)
rawdata["date"] = pd.to_datetime(rawdata["date"])
rawdata.head()
rawdata.tail()


# In[110]:


data = rawdata.loc[rawdata['bps_kecamatan_nama'] == 'ANJATAN']


# In[111]:


data.tail()


# In[112]:


prec = data[['date', 'precipitation']].set_index('date')


# In[113]:


prec.tail()


# In[114]:


prec.plot()


# In[115]:


model = EVA(data = prec.squeeze())
model


# In[116]:


model.get_extremes(
    method="BM",
    extremes_type="high",
    block_size="7D",
    errors="raise",
)
model


# In[117]:


model.plot_extremes()


# In[118]:


model.fit_model()
model


# In[119]:


model.plot_diagnostic(alpha=0.95)


# In[120]:


model.plot_return_values(
    return_period=np.logspace(0.01, 2, 100),
    return_period_size="100D",
    alpha=0.95,
)


# In[121]:


summary = model.get_summary(
    return_period=[1,2,3,4,  5,6,7,8,  9,10,11,12,  13,14,15,16,  17,18,19,20,  21,22,23,24],
    alpha=0.95,
    n_samples=1000,
)
summary


# In[122]:


model.get_extremes(
    method="BM",
    extremes_type="low",
    block_size="7D",
    errors="raise",
)
model


# In[123]:


model.plot_extremes()


# In[124]:


model.fit_model()
model


# In[125]:


model.plot_diagnostic(alpha=0.95)


# In[126]:


model.plot_return_values(
    return_period=np.logspace(0.01, 2, 100),
    return_period_size="100D",
    alpha=0.95,
)


# In[127]:


summary = model.get_summary(
    return_period=[1,2,3,4,  5,6,7,8,  9,10,11,12,  13,14,15,16,  17,18,19,20,  21,22,23,24],
    alpha=0.95,
    n_samples=1000,
)
summary


# In[128]:


calc_data = data[['date', 'precipitation']]
calc_data.tail()


# In[129]:


jul_2022 = (calc_data['date'] >= '2022-07-01') & (calc_data['date'] <= '2022-07-31')
df_jul_2022 = calc_data.loc[jul_2022]
df_jul_2022.head()


# In[130]:


sms.DescrStatsW(df_jul_2022['precipitation']).tconfint_mean()


# In[131]:


df_jul_2022['precipitation'].quantile([0.25, 0.75])


# In[132]:


aug_2022 = (calc_data['date'] >= '2022-08-01') & (calc_data['date'] <= '2022-08-31')
df_aug_2022 = calc_data.loc[aug_2022]
df_aug_2022.head()


# In[133]:


sms.DescrStatsW(df_aug_2022['precipitation']).tconfint_mean()


# In[134]:


df_aug_2022['precipitation'].quantile([0.25, 0.75])


# In[135]:


sep_2022 = (calc_data['date'] >= '2022-09-01') & (calc_data['date'] <= '2022-09-30')
df_sep_2022 = calc_data.loc[sep_2022]
df_sep_2022.head()


# In[136]:


sms.DescrStatsW(df_sep_2022['precipitation']).tconfint_mean()


# In[137]:


df_sep_2022['precipitation'].quantile([0.25, 0.75])


# In[138]:


oct_2022 = (calc_data['date'] >= '2022-10-01') & (calc_data['date'] <= '2022-10-31')
df_oct_2022 = calc_data.loc[oct_2022]
df_oct_2022.head()


# In[139]:


sms.DescrStatsW(df_oct_2022['precipitation']).tconfint_mean()


# In[140]:


df_oct_2022['precipitation'].quantile([0.25, 0.75])


# In[141]:


nov_2022 = (calc_data['date'] >= '2022-11-01') & (calc_data['date'] <= '2022-11-30')
df_nov_2022 = calc_data.loc[nov_2022]
df_nov_2022.head()


# In[142]:


sms.DescrStatsW(df_nov_2022['precipitation']).tconfint_mean()


# In[143]:


df_nov_2022['precipitation'].quantile([0.25, 0.75])


# In[144]:


dec_2022 = (calc_data['date'] >= '2022-12-01') & (calc_data['date'] <= '2022-12-31')
df_dec_2022 = calc_data.loc[dec_2022]
df_dec_2022.head()


# In[145]:


sms.DescrStatsW(df_dec_2022['precipitation']).tconfint_mean()


# In[146]:


df_dec_2022['precipitation'].quantile([0.25, 0.75])


# In[ ]:




