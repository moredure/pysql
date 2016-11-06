drop table if exists users;
drop table if exists secrets;

create table users (
  id integer primary key autoincrement,
  login text not null,
  username text not null,
  password text not null,
  age int not null
);

create table secrets (
  id integer primary key autoincrement,
  secret text not null
);

insert into secrets (secret) values ("secret{VERY_VERY_SECRET_INFORMATION}");
