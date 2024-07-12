-- models/datamart/dm_commodities.sql

with commodities as (
    select
        date,
        ticker,
        close_value
    from
        {{ ref('stg_commodities') }}
),

movements as (
    select
        date,
        ticker,
        action,
        quantity
    from
        {{ ref('stg_commodities_movements') }}
),

joined as (
    select
        c.date,
        c.ticker,
        c.close_value,
        m.action,
        m.quantity,
        (m.quantity * c.close_value) as movement_value,
        case
            when m.action = 'sell' then (m.quantity * c.close_value)
            else -(m.quantity * c.close_value)
        end as gain
    from
        commodities c
    inner join 
        movements m 
    on 
        c.date = m.date and c.ticker = m.ticker
),

last_day as (
    select
        max(date) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        date = (select max_date from last_day)
)

select
    date,
    ticker,
    close_value,
    action,
    quantity,
    movement_value,
    gain
from
    filtered