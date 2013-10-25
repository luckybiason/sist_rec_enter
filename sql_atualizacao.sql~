-- cadastro de televisores
CREATE TABLE "televisores" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome" varchar(50) NOT NULL UNIQUE,
    "imagem" varchar(100) NOT NULL,
    "marca_id" integer NOT NULL REFERENCES "televisores_marca" ("id"),
    "polegadas" real NOT NULL,
    "altura" real NOT NULL,
    "largura" real NOT NULL,
    "profundidade" real,
    "peso" real,
    "potencia" real,
    "tipo_de_tela_id" integer REFERENCES "televisores_tipotela" ("id"),
    "resolucao" varchar(150),
    "formato_tela" varchar(150),
    "consumo_energia" real,
    "is_full_hd" bool,
    "is_smart_tv" bool,
    "is_hdtv" bool,
    "is_3d" bool,
    "has_pip" bool,
    "has_sap" bool,
    "has_conversor" bool,
    "alimentacao" varchar(150),
    "especificacao" text,
    "site" varchar(150),
    "video" varchar(150)
)
-- Inserir imagem na marca
alter table televisores_marca
add column "imagem" varchar(100) NOT NULL default " ";
