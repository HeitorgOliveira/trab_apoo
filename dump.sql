PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Usuario (
    id    INTEGER PRIMARY KEY,
    nome  TEXT NOT NULL,
    tipo  TEXT NOT NULL CHECK (tipo IN ('Prof', 'Alum', 'Admin'))
);
CREATE TABLE Tarefa (
    id           INTEGER PRIMARY KEY,
    peso         REAL NOT NULL,
    tipo         TEXT NOT NULL CHECK (tipo IN ('Trab', 'Prov', 'Ativ')),
	id_disciplina INTEGER NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);
CREATE TABLE IF NOT EXISTS "Disciplina" (
	"id"	INTEGER,
	"nome"	TEXT NOT NULL,
	"codigo"	TEXT NOT NULL,
	"tipo"	TEXT NOT NULL CHECK("tipo" IN ('Prof', 'Alum', 'Admin')),
	"id_professor"	INTEGER NOT NULL,
	"id_admin"	INTEGER NOT NULL,
	FOREIGN KEY("id_professor") REFERENCES "Usuario"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Relac_Entrega" (
	"id"	INTEGER NOT NULL,
	"id_aluno"	INTEGER NOT NULL,
	"id_tarefa"	INTEGER NOT NULL,
	"Nota"	REAL,
	"Data"	TEXT,
	FOREIGN KEY("id_tarefa") REFERENCES "Tarefa"("id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_aluno") REFERENCES "Usuario"("id")
);
DELETE FROM sqlite_sequence;
COMMIT;
