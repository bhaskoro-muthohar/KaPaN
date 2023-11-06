import numpy as np
import pandas as pd

def lower_bound(x):
  return x.quantile(0.25) - 1.5 * (x.quantile(0.75) - x.quantile(0.25))

def upper_bound(x):
  return x.quantile(0.75) + 1.5 * (x.quantile(0.75) - x.quantile(0.25))

data_dir = "data/"
filename_input = "district_feature.csv"
filename_output = "district_feature_with_extreme_mark.csv"

df = pd.read_csv(data_dir + filename_input)

df_q = df.groupby("bps_kecamatan_kode").agg({
  "humidity": [lower_bound, upper_bound],
  "precipitation": [lower_bound, upper_bound],
  "windspeed": [lower_bound, upper_bound],
  "temperature": [lower_bound, upper_bound],
  "shortwavenet": [lower_bound, upper_bound],
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
  df["humidity"] < df["humidity_lower_bound"],
  "below",
  np.where(
    df["humidity"] > df["humidity_upper_bound"],
    "above",
    "normal"
  )
)

df["precipitation_extreme_mark"] = np.where(
  df["precipitation"] < df["precipitation_lower_bound"],
  "below",
  np.where(
    df["precipitation"] > df["precipitation_upper_bound"],
    "above",
    "normal"
  )
)

df["windspeed_extreme_mark"] = np.where(
  df["windspeed"] < df["windspeed_lower_bound"],
  "below",
  np.where(
    df["windspeed"] > df["windspeed_upper_bound"],
    "above",
    "normal"
  )
)

df["temperature_extreme_mark"] = np.where(
  df["temperature"] < df["temperature_lower_bound"],
  "below",
  np.where(
    df["temperature"] > df["temperature_upper_bound"],
    "above",
    "normal"
  )
)

df["shortwavenet_extreme_mark"] = np.where(
  df["shortwavenet"] < df["shortwavenet_lower_bound"],
  "below",
  np.where(
    df["shortwavenet"] > df["shortwavenet_upper_bound"],
    "above",
    "normal"
  )
)

df = df.drop(columns=df_q.columns)
df.to_csv(data_dir + filename_output, index=False)
