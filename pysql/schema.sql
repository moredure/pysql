drop table if exists users;
drop table if exists flags;

create table users (
  id integer primary key autoincrement,
  login text not null,
  username text not null,
  password_digest text not null,
  age int not null
);

create table secrets (
  id integer primary key autoincrement,
  secret text not null
);
