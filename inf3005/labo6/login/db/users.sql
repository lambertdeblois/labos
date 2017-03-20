drop table users;
drop table sessions;

create table users (
  id integer primary key,
  utilisateur varchar(25),
  prenom varchar(25),
  nom varchar(25),
  email varchar(100),
  confirmed integer default 0,
  token varchar(32) NULL,
  salt varchar(32),
  hash varchar(128)
);

create table sessions (
  id integer primary key,
  id_session varchar(32),
  utilisateur varchar(25)
);
