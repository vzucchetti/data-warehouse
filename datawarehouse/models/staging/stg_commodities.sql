-- import

with source as (
    select
        "Date",
        "Close",
        symbol
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

-- select * from

select 
    date,
    close_value,
    ticker
from renamed