create table utilisateur (
  nom varchar(20),
  prenom varchar(20),
  courriel varchar(50) primary key,
  date_inscription varchar(10),
  salt varchar(32),
  hash varchar(128)
);
