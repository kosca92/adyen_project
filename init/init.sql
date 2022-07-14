-- first table
create table transactions
(
    user_id int not null,
    ts timestamp not null,
    transaction_amount float not null
);
comment on table transactions is 'Append only table of all finished transactions';
comment on column transactions.user_id is 'Id of a user of this transaction';
comment on column transactions.ts is 'Transaction''s timestamp';
comment on column transactions.transaction_amount is 'Amount of money of this transaction';

-- second table
create table balance
(
    user_id int not null,
    total_amount float not null
);
comment on table balance is 'A table that contains current balance of each user from transactions table';
comment on column balance.user_id is 'Id of a user. Corresponds to transactions.user_id';
comment on column balance.total_amount is 'Sum of all transactions of this user';
create unique index balance_user_id_uindex on balance (user_id);

-- populate the tables
INSERT INTO transactions (user_id, ts, transaction_amount)
VALUES (1, '2021-05-04 04:20:00', 42);
INSERT INTO transactions (user_id, ts, transaction_amount)
VALUES (1, NOW(), 9000);
INSERT INTO transactions (user_id, ts, transaction_amount)
VALUES (1, NOW(), 0);
INSERT INTO transactions (user_id, ts, transaction_amount)
VALUES (2, NOW(), -1);