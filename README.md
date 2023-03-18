# novo-pugpe
Codebase para o novo site do PUG-PE.

## Dependências

O projeto tem como dependências `make`, `docker` e `docker-compose`. Para instalar o docker e docker-compose, siga as instruções na página oficial do docker.

## Iniciando o projeto

Para iniciar o projeto você vai precisar fazer o clone do repositório na sua máquina.

```
git clone https://github.com/pugpe/novo-pugpe.git
cd novo-pugpe
```

Com o docker rodando em sua máquina, execute:

```
make serve
```

Esta comando irá levantar os containers necessários para o desenvolvimento, executar todas as migrações e carregar todas as fixtures da pasta `fixtures` do projeto.


## Testes

Para rodar os testes do projeto, use o seguinte comando no terminal.

```shell
make test
```

Se você quiser usar flags com o pytest, abra um shell do docker e execute o pytest diretamente. Por exemplo, para rodar os testes que falharam na última execução, use o seguinte comando.

```
> make shell
docker-compose run --rm web /bin/bash
[+] Running 2/0
 ⠿ Container novo-pugpe-redis-1     Running                                                     0.0s
 ⠿ Container novo-pugpe-postgres-1  Running                                                     0.0s
user@70fcf18af7aa:/code$ pytest --lf -s
```

## Lint

Usamos `black`, `isort` e `flake8` no projeto. Para executar os linters em conjunto com os testes, use o seguinte comando no terminal.

```
make check
```

## Banco de dados

Para ações diretamente no Postgres, execute o comando abaixo para abrir um shell do banco de dados.

```
make dbshell
```

## Resetar o ambiente de desenvolvimento

Algumas vezes podem ocorrer erros no ambiente de desenvolvimento que a solução mais direta para se fazer é resetar o ambiente, para isso execute o comando. **ATENÇÃO**: Este comando irá descartar todo o estado da aplicação, incluindo banco de dados.

```
make clean
```

Isto irá descartar todo o estado da aplicação, incluindo banco de dados. Para iniciar o ambiente novamente, execute o comando `make serve`.


