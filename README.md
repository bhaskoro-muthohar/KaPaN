# [TBD] KaPaN

[TBD] Kalender Padi Nusantara

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


## Credits

This package was created with Cookiecutter and the `gerardrbentley/cookiecutter-streamlit` project template.
- Cookiecutter: [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
- `gerardrbentley/cookiecutter-streamlit`: [https://github.com/gerardrbentley/cookiecutter-streamlit](https://github.com/gerardrbentley/cookiecutter-streamlit)
- [TODO] Credits to Open Data Jabar
- [TODO] Credits to Giovanni
- [TODO] Anyone else?

Built with ❤️ by team 4SKA1 for UN Data Hackathon 2023.
Members:
- [Bhaskoro Muthohar](https://github.com/bhaskoro-muthohar)
- [Bagoes Rahmat Widiarso](https://github.com/zeogabrw)
- [Figarri Keisha](https://github.com/kfigarri)
- [Nashir Muhammad](https://github.com/nashr)

---

## What's this?

- `README.md`: This Document! To help you find your way around
- `streamlit_app.py`: The main app that gets run by [`streamlit`](https://docs.streamlit.io/)
- `requirements.txt`: Pins the version of packages needed
- `LICENSE`: Follows Streamlit's use of Apache 2.0 Open Source License
- `.gitignore`: Tells git to avoid comitting / scanning certain local-specific files
- `.streamlit/config.toml`: Customizes the behaviour of streamlit without specifying command line arguments (`streamlit config show`)

## Local Setup

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
## Deploy

For the easiest experience, deploy to [Streamlit Cloud](https://streamlit.io/cloud)

For other options, see [Streamilt deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)
