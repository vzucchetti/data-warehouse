import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Getting variables from .env file
DB_HOST = os.getenv("DB_HOST_PROD")
DB_PORT = os.getenv("DB_PORT_PROD")
DB_NAME = os.getenv("DB_NAME_PROD")
DB_USER = os.getenv("DB_USER_PROD")
DB_PASSWORD = os.getenv("DB_PASSWORD_PROD")
DB_SCHEMA = os.getenv("DB_SCHEMA_PROD")

# URL to acess database
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
    try:
        df = pd.read_sql(query, con=engine)
        return df
    except ProgrammingError as e:
        st.error(f"Error accessing table 'dm_commodities' in schema '{DB_SCHEMA}': {e}")
        return pd.DataFrame()  # returns an empty dataframe in case of error


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
st.write(
    """
This dashboard shows the commodities data extracted from Yahoo Finance and its transactions.
"""
)

# Get the data from the database
df = get_data()

#  Verify if the dataframe is empty
if df.empty:
    st.write(
        "Unable to load data. Check if the table 'dm_commodities' exists in the specified schema."
    )
else:
    # Show the data
    st.write("### Commodities data")
    st.dataframe(df)

    # Statistics
    st.write("### Statistical summary")
    st.write(df.describe())

    # Charts
    st.write("### Charts")

    # Bar chart for gains
    st.write("#### Gains")
    st.bar_chart(df[["date", "gain"]].set_index("date"))
