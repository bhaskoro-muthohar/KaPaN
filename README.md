# KaPaN (Kalender Padi Nusantara)

[![Built with ❤️ by team 4SKA1](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F-by%20team%204SKA1-red)](https://github.com/bhaskoro-muthohar/kapan)
[![UN Data Hackathon Winner](https://img.shields.io/badge/UN%20Datathon%202023-Asia%20Region%20Winner-gold)](https://drive.google.com/drive/folders/1NnulzX_Ks9JgqXNSTpLsTdTjq2gWKH2z)

> 🏆 **Award-Winning Data Analysis Project for the 2023 UN Datathon**  
> Developed award-winning data-driven Python application; recognized as best team in Asian region.  
> [View Certificate](https://drive.google.com/drive/folders/1NnulzX_Ks9JgqXNSTpLsTdTjq2gWKH2z)

KaPaN (Kalender Padi Nusantara) is an award-winning project developed for the UN Data Hackathon 2023, focusing on agricultural data analysis and visualization in Indonesia. Our innovative approach to agricultural data analysis earned us recognition as the best team in the Asian region.

## 📋 Table of Contents
- [Awards](#awards)
- [Features](#features)
- [Installation](#installation)
- [Data Processing](#data-processing)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributors](#contributors)
- [Data Sources](#data-sources)

## 🏆 Awards
- **UN Datathon 2023 - Asian Region Winner**
  - Recognized for excellence in data-driven agricultural analysis
  - Developed innovative Python application for agricultural planning
  - [View Certificate](https://drive.google.com/drive/folders/1NnulzX_Ks9JgqXNSTpLsTdTjq2gWKH2z)

## 🚀 Features
- Real-time weather data visualization
- Extreme weather pattern detection
- Agricultural calendar recommendations
- Interactive district-level data exploration
- Data-driven agricultural planning insights
- Advanced weather pattern analysis

## 💻 Installation

### Prerequisites
- Python 3.x
- Git

### Local Setup

1. Clone the repository
```bash
git clone git@github.com:bhaskoro-muthohar/kapan.git
cd kapan
```

2. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Unix/macOS
source venv/bin/activate
# For Windows
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🔄 Data Processing

### Data Directory Structure
```
data/
├── giovanni/
├── opendatajabar/
└── processed/
```

### Processing Steps

1. Extract raw data from NetCDF files to CSV:
```bash
python scripts/convert_nc_to_csv.py humidityrelative
python scripts/convert_nc_to_csv.py humidityspecific
python scripts/convert_nc_to_csv.py precipitation
python scripts/convert_nc_to_csv.py shortwavenet
python scripts/convert_nc_to_csv.py temperature
python scripts/convert_nc_to_csv.py windspeed
```

2. Combine CSV files by metric:
```bash
python scripts/combine_csv.py humidityrelative
python scripts/combine_csv.py humidityspecific
python scripts/combine_csv.py precipitation
python scripts/combine_csv.py shortwavenet
python scripts/combine_csv.py temperature
python scripts/combine_csv.py windspeed
```

3. Generate extreme weather markers:
```bash
python scripts/mark_extremes.py
```

## 🖥️ Usage

Run the Streamlit application:
```bash
streamlit run streamlit_app.py
```

The application will be available at [http://localhost:8501/](http://localhost:8501/)

## 🚀 Deployment

### Streamlit Cloud (Recommended)
Deploy directly to [Streamlit Cloud](https://streamlit.io/cloud) for the easiest setup.

For alternative deployment options, refer to the [Streamlit deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099).

## 👥 Contributors

Team 4SKA1:
- [Bhaskoro Muthohar](https://github.com/bhaskoro-muthohar)
- [Bagoes Rahmat Widiarso](https://github.com/zeogabrw)
- [Figarri Keisha](https://github.com/kfigarri)
- [Nashir Muhammad](https://github.com/nashr)

## 📊 Data Sources

This project utilizes data from various sources:

- **Open Data Jabar**
  - Accessed: November 4th, 2023
  - Source: [Open Data Jabar](https://opendata.jabarprov.go.id/)

- **NASA/AIRS Project**
  - Dataset: Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only)
  - Version: V7.0
  - DOI: 10.5067/UO3Q64CTTS1U

- **Global Modeling and Assimilation Office (GMAO)**
  - Dataset: MERRA-2 instM_2d_lfo_Nx
  - Version: V5.12.4
  - DOI: 10.5067/11F99Y6TXN99

- **GPM IMERG**
  - Dataset: Early Precipitation L3
  - Version: V06
  - DOI: 10.5067/GPM/IMERGDE/DAY/06

- **FLDAS Noah Land Surface Model**
  - Version: GDAS and CHIRPS-PRELIM
  - DOI: 10.5067/L8GPRQWAWHE3

- **GLDAS Catchment Land Surface Model**
  - Version: V2.2
  - DOI: 10.5067/TXBMLX370XX8

## 🙏 Acknowledgments

This package was created with:
- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [cookiecutter-streamlit template](https://github.com/gerardrbentley/cookiecutter-streamlit)

---

[![UN Data Hackathon 2023 Winner](https://img.shields.io/badge/UN%20Datathon%202023-Asia%20Region%20Winner-gold)](https://drive.google.com/drive/folders/1NnulzX_Ks9JgqXNSTpLsTdTjq2gWKH2z)