export PGPASSWORD=password
psql -f ./customer.sql -U dsuser -d db_part1 -h db
psql -f ./item.sql -U dsuser -d db_part1 -h db
psql -f ./transaction.sql -U dsuser -d db_part1 -h db
psql -f ./transaction_detail.sql -U dsuser -d db_part1 -h db