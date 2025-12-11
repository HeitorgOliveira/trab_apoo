PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE Usuario (
    id    INTEGER PRIMARY KEY,
    nome  TEXT NOT NULL UNIQUE,
    senha  TEXT NOT NULL,
    tipo  TEXT NOT NULL CHECK (tipo IN ('Prof', 'Alum', 'Admin'))
);
CREATE TABLE Tarefa (
    id INTEGER PRIMARY KEY,
    peso REAL NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Trab', 'Prov', 'Ativ')),
    id_disciplina INTEGER NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
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

INSERT INTO Usuario (id, nome, tipo, senha) VALUES (1, '[admin_padrão] Maria', 'Admin', 'senha');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (2, '[admin_padrão] João', 'Admin', 'senha');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (3, '[professor_padrão] Lucas', 'Prof', 'senha');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (4, '[aluno_padrão] Marcos', 'Alum', 'senha');

CREATE TABLE IF NOT EXISTS "Disciplina" (
	"id"	INTEGER,
	"nome"	TEXT NOT NULL,
	"codigo"	TEXT NOT NULL,
	"id_professor"	INTEGER,
	"id_admin"	INTEGER NOT NULL,
	FOREIGN KEY("id_professor") REFERENCES "Usuario"("id"),
	PRIMARY KEY("id")
);
DELETE FROM sqlite_sequence;
COMMIT;
