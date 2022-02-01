CREATE TABLE IF NOT EXISTS "moeda"(
    "id"        INTEGER UNIQUE NOT NULL,
    "simbolo"   TEXT UNIQUE NOT NULL,
    "nome"      TEXT NOT NULL,
    "ligazon"   TEXT UNIQUE NOT NULL,
    "data"      TEXT NOT NULL,
    CONSTRAINT moedaPK PRIMARY KEY ("id")
);
