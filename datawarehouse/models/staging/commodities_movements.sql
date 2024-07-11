with source as (
    select
        *
    from 
        {{ source('database_hrso', 'commodities_movements') }}
),

renamed as (
    select
        cast(date as date) as date,
        symbol as ticker,
        action,
        quantity
    from source
)

select
    *
from renamed