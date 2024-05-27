import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://airflow:airflow@postgres/airflow')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
