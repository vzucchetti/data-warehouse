{% docs overview %}

### README of the dbt-Core Project 

# dbt-Core Project to Commodities Data Warehouse

This project uses dbt (Data Build Tool) to manage and transform data from a commodity Data Warehouse (DW). The main goal is to create a roubst and efficiente data pipeline that processes and organizes commodity data and its movements for analysis.

## Project Structure

### 1. Seeds
Seeds are static data that are loaded into the Data Warehouse from CSV files. In this project, we use seeds to load commodity movements data.

### 2. Models
Models define data transformation using SQL. They are divided into two main layers: staging and datamart.

**Staging**
The staging layer is responsible for preparing and cleaning the data before it's loaded into the final analysis table.

- **stg_commodities.sql:** handles and formats commodity data extracted from the API.
- **stg_commodities_movements.sql:** handles and formats commodity movement data.

**Datamart**
The datamart layer is where the final analysis data is stored. They are based on the data prepared by the sataging layer.

- **dm_commodities.sql:** integrates the processed commodity and movement data, creating a final data model for analysis.

### 3. Sources
Sources are the data source tables or files that DBT uses to perform transformations.

### 4. Snapshots
Snapshots are used to keep a history of how data changes over time.

## Directory Structure

├── models
│ ├── staging
│ │ ├── stg_commodities.sql
│ │ └── stg_commodities_movements.sql
│ └── datamart
│   └── dm_commodities.sql
├── seeds
│ └── commodities_movements.csv
├── dbt_project.yml
└── README.md

## Running the Project

### Requeriments

- Python 3.7+
- dbt

### Steps for Execution

**1. Clone the Repository:**
```bash
git clone <repository-URL>
cd <repository-name>
```

**2. Install dbt**
```bash
pip install dbt-core dbt-postgres
```

**3. Configure dbt**
    
- Configure the `profiles.yml` to connect to your Data Warehouse. The file must be in the `~/.dbt/` directory or the directory specified by the environment variable `DBT_PROFILES_DIR`.

`profiles.yml` example:
```yml
database:
    target: dev
    outputs:
        dev:
            type: postgres
            host: <DB_HOST_PROD>
            user: <DB_USER_PROD>
            password: <DB_PASSWORD_PROD>
            port: <DB_PORT_PROD>
            dbname: <DB_NAME_PROD>
            schema: <DB_SCHEMA_PROD>
            threads: 1
```

**4. Run dbt Seeds:**
```bash
dbt seed
```

**5. Run the dbt transformation:**
```bash
dbt run
```

**6. Check Project Status:**
```bash
dbt test
```

### Description of Models

**stg_commodities.sql**

This model is responsible for processing and formatting the commodity data extracted from the API. It does the necessary cleaning and transformation to prepare the data for the datamart.

**stg_commidities_movements.sql**

This model is responsible for processing and formatting commodity movement data taked from csv file seeded. It does the necessary cleaning and transformation to prepare the data for the datamart.

**dm_commodities.sql**
This model integrates the processed commodity and movement data, creating a final data model for analysis. It calculates metrics and aggregates data to facilitatre analysis on the dashboard.

{% enddocs %}