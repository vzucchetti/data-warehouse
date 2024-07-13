import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Variable of commodities to extract from API
commodities = ['CL=F', 'GC=F', 'SI=F'] #Crude Oil, Gold, Silver

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

#Function to extract data from Yahoo Finance
def find_commodities_data(symbol, period='5d', interval='1d'): #parameters for the function
    ticker = yf.Ticker(symbol) #function to access the data from Yahoo Finance
    data = ticker.history(period=period, interval=interval)[['Close']] #return a dataframe with the close price of stock
    data['symbol'] = symbol
    return data

# Function to append data of find_commodities_data
def find_all_commotities_data(commodities):
    all_data = [] #list to store the data
    for symbol in commodities: #loop to extract data from all commodities
        data = find_commodities_data(symbol)
        all_data.append(data) #append the data to the list
    return pd.concat(all_data) #return the data in a single dataframe

# Saving extracted data to a postgre database
def save_data_to_db(df, schema='public'):
    df.to_sql('commodities', con=engine, schema=schema, if_exists='replace', index=True, index_label='Date')

# Main function to run the code
if __name__ == '__main__':
    concatenated_data = find_all_commotities_data(commodities)
    save_data_to_db(concatenated_data)