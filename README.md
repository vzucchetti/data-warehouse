Data Warehouse from Scratch

Here we' wi'll construct a Data WareHouse (DW) to analyse commodity data aiming to reduce manual work, enhance performance, easy to do SQL querys, reuse processing, and most important: 

**Make Money For The Company!**

To accomplish that, we'll do a *ELT process*, integrating *APIs to extract data and Excel sheets*, *load using PostgreSQL*, and *transform using dbt-core*. With all this transformed data in hands, we can construct a dashboard using the streamlit.

To start the project, we'll do the extraction of commodities data from Yahoo Finance's API using the library `yfinance`.

After that, we'll connect to our PostgreSQL database with the `sqlalchemy`, using the Render as server, to load commodities data on it. To connection work, it's needed a `.env` file with the environment variables (host, port, name, user, password, schema) which will link to the database server.

The aforementioned steps are in the script `extract_load.py`. Run this under the `src` folder:
```python
python extract_load.py
```

dbt-core is a open-source tool that documents your code, test it and use only SQL language to realize the transformations.
To start our dbt project it needs to install the library (in our case its integration with postgres):
```bash
pip install dbt-postgres
```

Once installed, we'll initiate the dbt
```bash
dbt init
```
and now we have our dbt folders.

To check if everything is right, we enter in the folder created
```bash
cd datawarehouse
```
and run a debug.
```bash
dbt debug
```



Libraries:
- pandas: to create dataframes and transform data.
- sqlalchemy: to manipulate the database.
- python-dotevn: to control environment variables.
- psycopg2-binary: to get acess to PostgreSQL with .env.
- yfinance: to acess data from yahoo.
- dbt-postgres: 

