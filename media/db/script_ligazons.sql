CREATE TABLE IF NOT EXISTS "moeda"(
    "id"        INTEGER UNIQUE NOT NULL,
    "simbolo"   TEXT NOT NULL,
    "nome"      TEXT NOT NULL,
    "ligazon"   TEXT UNIQUE NOT NULL,
    "data"      TEXT NOT NULL,
    "borrado"   INTEGER NOT NULL DEFAULT 0,
    CONSTRAINT moedaPK PRIMARY KEY ("id")
);
