# [TBD] KaPaN

[TBD] Kalender Padi Nusantara

## Requirements
All required libraries and packages are listed in `requirements.txt`.

## Data Pre-processing

### Data Sources
All raw data are available under `data/` directory, grouped by the source name. Everything under `data/giovanni` is downloaded from [Giovanni](https://giovanni.gsfc.nasa.gov/), everything under `data/opendatajabar` is from [Open Data Jabar](https://opendata.jabarprov.go.id/), etc.

### Pre-processing Raw Data

#### Extracting Raw Data
Run following commands in console/terminal.
```sh
python scripts/convert_nc_to_csv.py humidityrelative
python scripts/convert_nc_to_csv.py humidityspecific
python scripts/convert_nc_to_csv.py precipitation
python scripts/convert_nc_to_csv.py shortwavenet
python scripts/convert_nc_to_csv.py temperature
python scripts/convert_nc_to_csv.py windspeed
```

There will be a series of CSV files generated in each respective metrics directory, something like `humidityrelative_tab_20220701.csv`. After that, combining all those CSV files can done by running following commands.
```sh
python scripts/combine_csv.py humidityrelative
python scripts/combine_csv.py humidityspecific
python scripts/combine_csv.py precipitation
python scripts/combine_csv.py shortwavenet
python scripts/combine_csv.py temperature
python scripts/combine_csv.py windspeed
```

After that, you'll get a single CSV file for each metrics, namely `humidityrelative_tab_all.csv` directly under `data/` directory.

#### Labeling Extreme Weather in Raw Data
Run following command to get file `data/district_feature_with_extreme_mark.csv` from which the website read data to visualize.
```sh
python scripts/mark_extremes.py
```

## Running App

### Local Setup

Assumes working python installation and some command line knowledge ([install python with conda guide](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html)).

```sh
# External users: download Files
git clone git@github.com:bhaskoro-muthohar/kapan.git

# Go to correct directory
cd kapan

# Create virtual environment for this project
python -m venv venv

# Activate the virtual environment
. ./venv/bin/activate
# .\venv\Scripts\activate for Windows

# Install required Packages
python -m pip install -r requirements.txt

# Run the streamlit app
streamlit run streamlit_app.py
```

Open your browser to [http://localhost:8501/](http://localhost:8501/) if it doesn't open automatically.

### Deploy

For the easiest experience, deploy to [Streamlit Cloud](https://streamlit.io/cloud)
For other options, see [Streamilt deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)

## Credits

This package was created with Cookiecutter and the `gerardrbentley/cookiecutter-streamlit` project template.
- Cookiecutter: [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
- `gerardrbentley/cookiecutter-streamlit`: [https://github.com/gerardrbentley/cookiecutter-streamlit](https://github.com/gerardrbentley/cookiecutter-streamlit)
- Open Data Jabar, Accessed: November 4th, 2023.
- AIRS project (2019), Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: November 4th, 2023, 10.5067/UO3Q64CTTS1U
- Global Modeling and Assimilation Office (GMAO) (2015), MERRA-2 instM_2d_lfo_Nx: 2d,Monthly mean,Instantaneous,Single-Level,Assimilation,Land Surface Forcings V5.12.4, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: November 4th, 2023, 10.5067/11F99Y6TXN99
- Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2019), GPM IMERG Early Precipitation L3 1 day 0.1 degree x 0.1 degree V06, Edited by Andrey Savtchenko, Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: November 3th, 2023, 10.5067/GPM/IMERGDE/DAY/06
- Jossy Jacob, Kimberly Slinksi (NASA/GSFC/HSL) (2021), FLDAS Noah Land Surface Model L4 Global Monthly 0.1 x 0.1 degree (GDAS and CHIRPS-PRELIM), Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: November 4th, 2023, 10.5067/L8GPRQWAWHE3
- Li, B., H. Beaudoing, and M. Rodell, NASA/GSFC/HSL (2020), GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree GRACE-DA1 V2.2, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: November 4th, 2023, 10.5067/TXBMLX370XX8

---

Built with ❤️ by team 4SKA1 for UN Data Hackathon 2023.

Members:
- [Bhaskoro Muthohar](https://github.com/bhaskoro-muthohar)
- [Bagoes Rahmat Widiarso](https://github.com/zeogabrw)
- [Figarri Keisha](https://github.com/kfigarri)
- [Nashir Muhammad](https://github.com/nashr)
