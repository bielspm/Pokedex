# Pokedex
# Tela de busca - TELA 1
<img src="imgs/index.png" width="574px" height="244px">
<hr>
# Tela de resultados - TELA 2
<img src="imgs/resultados.png" width="486px" height="246px">
<hr>
# Pokemon - TELA 3
<img src="imgs/pokemon.png" width="843px" height="503px">
<hr>
## Instruções para o teste

Foi usado Python 3.7 , Mysql 8.0 , Django 2.2.

1. Instalar o Python (https://www.python.org/downloads/). Marcar a opção 'adicionar ao path'.
2. Instalar o django usando o comando 'pip install django' no cmd do windows. PIP é o gerenciador de pacotes do python.
  Se não funcionar use: 'py -m pip install django' ou 'python -m pip install django'.
3. Rodar o script "criar_tabela_pokedex.sql" para criar o banco de dados e a tabela no Mysql.
4. Edite o arquivo python 'popular_banco de dados.py' e mude os argumentos da função 'mysql.connector.connect()' usando os dados do seu banco de dados como usuario, senha, porta, etc.
5. Rode o script 'popular_banco de dados.py'.
6. Dentro da pasta pokedex, dentro do arquivo 'setting.py' mude os valores da variavel 'DATABASES = {}' e use os dados do seu banco de dados como usuario, senha , etc.
7.Pelo CMD do windows, navegue até a pasta raiz (pokedex), onde esta o arquivo 'manage.py' e use o comando 'py manage.py runserver' ou 'python manage.py runserver' para iniciar o servidor.Depois é so abrir o 'localhost' na url do google chrome ou '127.0.0.1:8000'.
