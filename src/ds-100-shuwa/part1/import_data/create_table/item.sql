drop table if exists item;
create table item(
    id varchar(14),
    item_name varchar(30),
    price integer,
    primary key (id)
)