drop table if exists users;
drop table if exists flags;

create table users (
  id integer primary key autoincrement,
  name text not null,
  age int not null
);

create table flags (
  id integer primary key autoincrement,
  secret text not null
);
