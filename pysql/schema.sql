drop table if exists users;
drop table if exists secrets;

create table users (
  id serial primary key,
  login varchar,
  username varchar,
  password varchar,
  age integer
);

create table secrets (
  id serial primary key,
  secret varchar
);

insert into secrets (secret) values ('secret{VERY_VERY_SECRET_INFORMATION}');
