import pandas as pd
import time
from netCDF4 import Dataset

METRICS_HUMIDITYRELATIVE = "humidityrelative"
METRICS_HUMIDITYSPECIFIC = "humidityspecific"
METRICS_PRECIPITATION = "precipitation"
METRICS_SHORTWAVENET = "shortwavenet"
METRICS_TEMPERATURE = "temperature"
METRICS_WINDSPEED = "windspeed"

metrics = METRICS_HUMIDITYRELATIVE

code = "unknown"
if metrics == METRICS_HUMIDITY:
  code = "FLDAS_NOAH01_CP_GL_M_001_Qair_f_tavg"
elif metrics == METRICS_HUMIDITYRELATIVE:
  code = "AIRS3STD_7_0_RelHumSurf_A"
elif metrics == METRICS_PRECIPITATION:
  code = "GPM_3IMERGDE_06_precipitationCal"
elif metrics == METRICS_SHORTWAVENET:
  code = "GLDAS_CLSM025_DA1_D_2_2_Swnet_tavg"
elif metrics == METRICS_TEMPERATURE:
  code = "AIRS3STD_7_0_SurfSkinTemp_A"
elif metrics == METRICS_WINDSPEED:
  code = "M2IMNXLFO_5_12_4_SPEEDLML"

startdate = "2022-01-01"
frequency = "D" # day
if metrics in (METRICS_HUMIDITY, METRICS_WINDSPEED):
  startdate = "2020-01-01"
  frequency = "MS" # month start

data_dir = "data/{0}/".format(metrics)

dates = pd.date_range(startdate, "2023-06-30", freq=frequency).strftime("%Y%m%d").tolist()

for i in range(len(dates)):
  start_time = time.time()

  date = dates[i]
  filename = "raw/shapeMasked.scrubbed.{0}.{1}.nc".format(code, date)

  print("Processing", date)

  # read source file
  try:
    nc = Dataset(data_dir + filename, "a")
  except:
    continue

  # # save in a geomap format
  # df_geo = pd.DataFrame(
  #   data    = nc.variables[code][0],
  #   index   = nc.variables["lat"][:],
  #   columns = nc.variables["lon"][:]
  # )
  # df_geo.to_csv(data_dir + "{0}_geo_{1}.csv".format(metrics, date))

  # save in a tabular format
  lists = []
  for r in range(nc.variables["lat"].shape[0]):
    for c in range(nc.variables["lon"].shape[0]):
      val = nc.variables[code][0][r][c]
      if val != "--":
        lists.append(
          [
            nc.variables["lat"][r],
            nc.variables["lon"][c],
            val,
          ]
        )
  df_tab = pd.DataFrame(lists, columns=["latitude", "longitude", "value"])
  df_tab.to_csv(data_dir + "{0}_tab_{1}.csv".format(metrics, date), index=False)

  end_time = time.time()
  print("in", end_time - start_time, "seconds")
