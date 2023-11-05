import numpy as np
import pandas as pd

def q25(x):
  return x.quantile(0.25)

def q75(x):
  return x.quantile(0.75)

data_dir = "data/"
filename_input = "district_feature.csv"
filename_output = "district_feature_with_extreme_mark.csv"

df = pd.read_csv(data_dir + filename_input)

df_q = df.groupby("bps_kecamatan_kode").agg({
  "humidity": [q25, q75],
  "precipitation": [q25, q75],
  "windspeed": [q25, q75],
  "temperature": [q25, q75],
  "shortwavenet": [q25, q75],
})
df_q = df_q.reset_index()

df_q.columns = [
  df_q.columns.get_level_values(0)[i]
  + "_"
  + df_q.columns.get_level_values(1)[i]
  for i in range(len(df_q.columns))
]

df = pd.merge(
  df,
  df_q,
  left_on="bps_kecamatan_kode",
  right_on="bps_kecamatan_kode_"
)

df["humidity_extreme_mark"] = np.where(
  df["humidity"] < df["humidity_q25"],
  "below",
  np.where(
    df["humidity"] > df["humidity_q75"],
    "above",
    "normal"
  )
)

df["precipitation_extreme_mark"] = np.where(
  df["precipitation"] < df["precipitation_q25"],
  "below",
  np.where(
    df["precipitation"] > df["precipitation_q75"],
    "above",
    "normal"
  )
)

df["windspeed_extreme_mark"] = np.where(
  df["windspeed"] < df["windspeed_q25"],
  "below",
  np.where(
    df["windspeed"] > df["windspeed_q75"],
    "above",
    "normal"
  )
)

df["temperature_extreme_mark"] = np.where(
  df["temperature"] < df["temperature_q25"],
  "below",
  np.where(
    df["temperature"] > df["temperature_q75"],
    "above",
    "normal"
  )
)

df["shortwavenet_extreme_mark"] = np.where(
  df["shortwavenet"] < df["shortwavenet_q25"],
  "below",
  np.where(
    df["shortwavenet"] > df["shortwavenet_q75"],
    "above",
    "normal"
  )
)

df = df.drop(columns=df_q.columns)
df.to_csv(data_dir + filename_output, index=False)
