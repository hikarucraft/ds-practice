drop table if exists transaction_detail;
create table transaction_detail(
    id integer,
    quantity integer,
    transaction_history_id varchar(32) REFERENCES transaction_history(id) ON DELETE CASCADE,
    item_id varchar(32) REFERENCES item(id) ON DELETE CASCADE,
    primary key (id)
)