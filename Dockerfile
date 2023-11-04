FROM python:3.10.13-slim-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python scripts/init_db.py
RUN python scripts/load_data.py

EXPOSE 80

ENV STREAMLIT_SERVER_PORT=80

CMD ["streamlit", "run", "app.py", "--server.port=80"]