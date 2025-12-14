PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Prof', 'Alum', 'Admin'))
);

CREATE TABLE Disciplina (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL,
    id_professor INTEGER,
    id_admin INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES Usuario(id),
    FOREIGN KEY (id_admin) REFERENCES Usuario(id)
);

CREATE TABLE Tarefa (
    id INTEGER PRIMARY KEY,
    peso REAL NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('atividade', 'trabalho', 'prova')),
    id_disciplina INTEGER NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);

CREATE TABLE Inscricao (
    id_aluno INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES Usuario(id),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);

CREATE TABLE Relac_Entrega (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_tarefa INTEGER NOT NULL,
    nota REAL,
    data TEXT,
    FOREIGN KEY (id_aluno) REFERENCES Usuario(id),
    FOREIGN KEY (id_tarefa) REFERENCES Tarefa(id)
);

CREATE TABLE Relac_Media (
    id_aluno INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    media_atividade REAL,
    media_trabalho REAL,
    media_prova REAL,
    media_final REAL,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES Usuario(id),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);

INSERT INTO Usuario (id, nome, tipo, senha) VALUES (1, '[admin_padrão "Maria"]', 'Admin', '1234');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (2, '[professor_padrão "Lucas"]', 'Prof', '1111');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (3, '[professor_padrão "Ana"]', 'Prof', '2222');
INSERT INTO Usuario (id, nome, tipo, senha) VALUES (4, '[aluno_padrão "Marcos"]', 'Alum', '3333');
INSERT INTO Disciplina (id, nome, codigo, id_professor, id_admin) VALUES (1, '[disciplina_padrão "APOO"]', '345', 2, 1);

DELETE FROM sqlite_sequence;
COMMIT;
