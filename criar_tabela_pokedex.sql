CREATE DATABASE pokedex;
use pokedex;
CREATE TABLE pokemon(
	pokemon_number smallint PRIMARY KEY DEFAULT 1,
    pokemon_name varchar(30) UNIQUE NOT NULL,
    attack smallint NOT NULL,
    classfication varchar(30) NOT NULL,
    defense smallint NOT NULL,
    height_m varchar(10),
    hp smallint NOT NULL,
    speed smallint NOT NULL,
    type1 varchar(15) NOT NULL,
    type2 varchar(15) NOT NULL,
    weight_kg float NOT NULL,
    generation tinyint NOT NULL,
    is_legendary tinyint NOT NULL,
    abilities varchar(100)
);