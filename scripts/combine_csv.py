import pandas as pd

METRICS_HUMIDITYRELATIVE = "humidityrelative"
METRICS_HUMIDITYSPECIFIC = "humidityspecific"
METRICS_PRECIPITATION = "precipitation"
METRICS_SHORTWAVENET = "shortwavenet"
METRICS_TEMPERATURE = "temperature"
METRICS_WINDSPEED = "windspeed"

metrics = METRICS_HUMIDITYRELATIVE

startdate = "2022-01-01"
frequency = "D" # day
if metrics in (METRICS_HUMIDITY, METRICS_WINDSPEED):
  startdate = "2020-01-01"
  frequency = "MS" # month start

data_dir = "data/{0}/".format(metrics)

df = pd.DataFrame()

dates = pd.date_range(startdate, "2023-06-30", freq=frequency).strftime("%Y%m%d").tolist()
for i in range(len(dates)):
  date = dates[i]
  print(date)

  try:
    df_i = pd.read_csv(data_dir + "{0}_tab_{1}.csv".format(metrics, date))

    df_i = df_i[
      (df_i["latitude"] >= -8) & (df_i["latitude"] <= -5)
      & (df_i["longitude"] >= 106) & (df_i["longitude"] <= 109)
    ]
    df_i["date"] = date
    if df_i.shape[0] > 0:
      df = pd.concat([df, df_i], ignore_index=True)
  except:
    pass

df = df.sort_values(["latitude", "longitude", "date"])
df.to_csv(data_dir + "{0}_tab_all.csv".format(metrics), index=False)
