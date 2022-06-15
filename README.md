## FRIENDS API

### DESCRIÇÃO
API para Gerenciamento de Amigos com base em um modelo de grafo não-direcionado.

O projeto foi desenvolvido com Python e o Framework Flask.

Não foi-se utilizado banco de dados, por acreditar que a implementação do mesmo 
geraria complexidade elevada para o projeto que é relativamente simples, não 
possuindo relacionamentos complexos entre as entidades.

### REQUERIMENTOS
* Docker
* Python 3

### INICIALIZAÇÃO
Para iniciar a aplicação localmente, você deverá criar a imagem docker a partir do seguinte comando:
```
docker build -t friends .
```

Para rodar a aplicação, basta executar o seguinte comando:
```
docker run -d -p 8080:8080 -e PROFILE=Production friends
```

Para rodar os testes, basta executar o comando abaixo:
```
python3 -m unittest src.test.${arquivo_de_teste}
```