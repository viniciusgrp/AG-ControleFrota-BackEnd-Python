Olá!

Este projeto trata-se de um sistema de gestão de frota, sendo possível cadastrar motoristas, veículos e fazer o controle de entrada e saída dos veículos.

O projeto foi feito utilizando Django, Django RestFramework e Django ORM.

Para rodar o projeto:

Garanta que tenha instalado no seu computador:

Python
pip
MySQL

Comece criando um abiente virtual em python, acesse seu terminal GitBash e digite:

python -m venv venv

Depois é necessário acessar o ambiente virtual, no mesmo terminal digite:

source venv/Scripts/activate

Após isso vamos instalar as dependencias para que o projeto possa funcionar corretamente, esse repositório já possui o arquivo requirements.txt, contendo todas as dependencias.
Com o ambiente virtual ativo, digite no terminal:

pip install -r requirements.txt

Após isso, é necessário criar um banco de dados MySQL localmente, para isso vou deixar um tutorial para que você consiga realizar:

https://www.devmedia.com.br/primeiros-passos-no-mysql/28438

Lembre-se de anotar: Nome de usuário, senha, nome do banco.

Com esses dados em mãos, vá ate:

ControleFrota/settings.py

Procure pela seção DATABASES e preencha com as informações
"NAME" coloque o nome do banco
"USER" coloque o nome de usuario MySQL
"PASSWORD" coloque a senha do usuario MySQL

e garanta que a sua configuração de host e portas são as mesmas já definidas no projeto.

Com tudo certo, podemos rodar as migrations para realizar a criação das tabelas automaticamente em nosso banco de dados.
No mesmo terminal digite:

python manage.py migrate

Após isso, estará tudo pronto para rodarmos o servidor localmente, digite no terminal:

python manage.py runserver