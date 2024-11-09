drop table if exists transaction_history;
create table transaction_history(
    id varchar(32),
    price integer,
    payment_timestamp timestamptz,
    customer_id varchar(32) REFERENCES customer(id) ON DELETE CASCADE,
    primary key (id)
)