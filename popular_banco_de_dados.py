""" Conexão com o banco de dados e popular o banco com os dados do arquivo CSV"""
import csv
import mysql.connector
from mysql.connector import errorcode

try:
    conexaoBD = mysql.connector.connect(host='localhost',user='root',database='pokedex',password='CounterSTRIKE15')
    dbcursor = conexaoBD.cursor()
    with open('pokemon.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            if linha[0] == 'pokedex_number':
                continue
            else:
                add_pokemons_query = "INSERT INTO pokedex.pokemon(pokemon_name, attack, classfication, defense, height_m, hp, speed, type1, type2, weight_kg, generation, is_legendary, abilities) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                valores = linha[1].lower(), linha[2], linha[3].replace(' PokÃ©mon','').lower(), linha[4], linha[5], linha[6], linha[7], linha[8], linha[9],linha[10], linha[11], linha[12], linha[13].replace("['",'').replace("']",'').replace("'",'').lower()
                dbcursor.execute(add_pokemons_query, valores)
                conexaoBD.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
