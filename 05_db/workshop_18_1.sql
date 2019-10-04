CREATE TABLE bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    debut INTEGER
);

INSERT INTO bands(name, debut)
VALUES ('Queen', 1973), ('Coldplay', 1998), ('MCR', 2001);