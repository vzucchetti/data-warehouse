-- import

with source as (
    select
        *
    from
        {{ source ('database_hrso','commodities') }}
),

-- renamed

renamed as (
    select
        cast("Date" as date) as date,
        "Close" as close_value,
        symbol as ticker
    from
        source
)

-- query

select 
    * 
from renamed