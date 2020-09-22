/*
** prosjekt-script-mysql.txt
/*
** DROP TABLE-setninger som sletter gamle tabeller
*/

DROP TABLE IF EXISTS gjenstand;
DROP TABLE IF EXISTS egenskaper;
DROP TABLE IF EXISTS proveniens;
DROP TABLE IF EXISTS kategori;

/*
** Oppretter tabeller med entitetsintegritet
*/
CREATE TABLE gjenstand
(
regnr VARCHAR(10) NOT NULL,
navn VARCHAR(30),
kategori_id INT,
regdato VARCHAR(15),
regav VARCHAR(50),
inndato VARCHAR(15),
mottattav VARCHAR(50),
giver VARCHAR(300),
plassering VARCHAR(30),
kommentar VARCHAR(1000),
PRIMARY KEY(regnr)
)ENGINE=INNODB;

CREATE TABLE egenskaper
(
regnr VARCHAR(10) NOT NULL,
materiale VARCHAR(30),
maal VARCHAR(30),
tilstand VARCHAR(15),
fys_egenskap VARCHAR(1000),
PRIMARY KEY(regnr)
)ENGINE=INNODB;

CREATE TABLE proveniens
(
regnr VARCHAR(10) NOT NULL,
produsent VARCHAR(30),
prod_aar INT,
tidl_eiere VARCHAR(300),
siste_eier VARCHAR(50),
PRIMARY KEY(regnr)
)ENGINE=INNODB;

CREATE TABLE kategori
(
kategori_id INT NOT NULL,
katnavn VARCHAR(30),
PRIMARY KEY(kategori_id)
)ENGINE=INNODB;

/*
** Legger på referanseintegritet (fremmednøkler)
*/
ALTER TABLE gjenstand
 ADD FOREIGN KEY(kategori_id) REFERENCES kategori(kategori_id);

ALTER TABLE egenskaper
 ADD FOREIGN KEY(regnr) REFERENCES gjenstand(regnr);
 
ALTER TABLE proveniens
 ADD FOREIGN KEY(regnr) REFERENCES gjenstand(regnr);


/*
** Legger inn gyldige data i tabellene (eksempel)
*/

INSERT INTO kategori VALUES(1,'Møbel');

INSERT INTO gjenstand VALUES('TBM.4892','Kommode', 1, '03.04.2012','Museumsbestyrer Olav Nilsen', '29.04.2012','Museumsbestyrer Olav Nilsen', 'Gunnar Berg f.1952', 'M1.R2.P1.H1','Kommoden er laget av den kjente håndverkeren Mathias Guttormsen');

INSERT INTO egenskaper VALUES('TBM.4892','Tre Gran','L:103 cm, H:122 cm, D:42 cm','God','Rosemalt kommode');

INSERT INTO proveniens VALUES('TBM.4892','Mathias Guttormsen f.1798',1843,'Olaug Jørgensdatter Berg m.fl.','Gunnar Berg f.1952');


