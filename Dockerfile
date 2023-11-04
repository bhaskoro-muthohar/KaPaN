FROM python:3.10.6-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python scripts/init_db.py
RUN python scripts/load_data.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]