FROM python:3.10.13-slim-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python scripts/init_db.py
RUN python scripts/load_data.py

EXPOSE 8501
EXPOSE 80

CMD ["streamlit", "run", "app.py"]