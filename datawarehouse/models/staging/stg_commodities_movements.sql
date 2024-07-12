with source as (
    select
        date,
        ticker,
        action,
        quantity
    from 
        {{ source('database_hrso', 'commodities_movements') }}
),

renamed as (
    select
        cast(date as date) as date,
        ticker,
        action,
        quantity
    from source
)

select
    date,
    ticker,
    action,
    quantity
from renamed