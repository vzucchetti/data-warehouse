Data Warehouse from Scratch

Here we' wi'll construct a Data WareHouse (DW) to analyse commodity data aiming to reduce manual work, enhance performance, easy to do SQL querys, reuse processing, and most important: 

**Make Money For The Company!**

To accomplish that, we'll do a *ELT process*, integrating *APIs to extract data in Python*, *load using PostgreSQL*, and *transform using dbt-core*.

To start the project, we'll do the extraction of commodities data from Yahoo Finance using the library `yfinance`.

After, the data was extracted we'll connect to our PostgreSQL database using the Render as server. To work the connection, it's needed a .env file with the environment variables of the database (host, port, name, user, password, schema).

The aforementioned steps are in the `extract_load.py` file. Run this under the `src` folder:
```python
python extract_load.py
```

Libraries:
- pandas: to create dataframes and transform data.
- sqlalchemy: to manipulate de database.
- python-dotevn: to control environment variables.
- psycopg2-binary: to work with the PostgreSQL.
- yfinance: to acess data from yahoo.

dbt-core is a open-source tool that documents your code, test it and use only SQL language to realize the transformations.