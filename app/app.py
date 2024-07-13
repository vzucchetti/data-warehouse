import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Getting variables from .env file
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASSWORD = os.getenv('DB_PASSWORD_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# URL to acess database
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# Create the engine to connect to the database
engine = create_engine(DATABASE_URL)

# Function to get data from the database and return a dataframe
def get_data():
    query = f"""
    SELECT 
        *
    FROM
        public.dm_commodities;
    """
    df = pd.read_sql(query, con=engine)
    return df

# Configurate streamlit app
st.set_page_config(
    page_title="Commodities Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dashboard title
st.title("Commodities Dashboard")

# Description of the dashboard
st.write("""
This dashboard shows the commodities data extracted from Yahoo Finance and its transactions.
""")

# Get the data from the database
df = get_data()

st.dataframe(df)

