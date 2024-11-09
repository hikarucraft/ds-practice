drop table if exists customer;
create type gender_enum as enum ('M','F','unknown');
create table customer(
    id varchar(32),
    customer_name varchar(30),
    customer_name_kana varchar(30),
    registration_timestamp timestamptz,
    email varchar(64),
    gender gender_enum default 'unknown',
    age integer,
    birth_day date,
    address_pref varchar(4),
    primary key (id)
)