create table livres (
  id_livre integer PRIMARY KEY,
  titre varchar(32),
  auteur varchar(50),
  annee_pub varchar(10),
  nb_pages integer DEFAULT 0,
  nb_chapitres integer DEFAULT 0
);

insert into livres values(1, 'harry potter', 'rowling', '2001-01-01', 500, 20);
insert into livres values(2, 'harry potter2', 'rowling', '2001-01-01', 500, 20);
insert into livres values(3, 'harry potter3', 'rowling', '2001-01-01', 500, 20);
insert into livres values(4, 'harry potter4', 'rowling', '2001-01-01', 500, 20);
