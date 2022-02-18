DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titolo TEXT,
	info TEXT
);

INSERT INTO posts (titolo, info) VALUES (
	"Notturno",
	"Scritto da Leonardo Sartori"
);

INSERT INTO posts (titolo, info) VALUES (
	"Falling Snow",
	"Scritto da Leonardo Sartori"
);
