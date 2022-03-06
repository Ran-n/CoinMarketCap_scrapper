CREATE TABLE IF NOT EXISTS "moeda"(
    "id"                INTEGER UNIQUE NOT NULL,
    "simbolo"           TEXT NOT NULL,
    "nome"              TEXT NOT NULL,
    "ligazon"           TEXT UNIQUE NOT NULL,
    "creada"            TEXT NOT NULL,
    "modificada"        TEXT,
    "estado"            INTEGER NOT NULL DEFAULT 0,
    CONSTRAINT moedaPK PRIMARY KEY ("id")
);
