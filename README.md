# Teste-starline-fabio
Teste tecnico para processo seletivo desenvolvedor full stack Starline Tecnologia

Teste tecnico para processo seletivo Starline Tecnologia
O projeto será desenvolvido utilizando a linguagem Python 3.6.0 com Django e a biblioteca Django Rest para backend (rest full) utilizando virtualenvwrapper usando gerenciador pip.

## Ambiente

Para instalar o virtualenvwrapper/criar o ambiente :

$ pip install virtualenvwrapper

Configure o arquivo .bashrc :

$ export WORKON_HOME=~/.virtualenvs

$ source /usr/local/bin/virtualenvwrapper.sh

Para criar um virtualenvs basta usar o comando :

$ mkvirtualenv (nome da virtualenv)

Para acessar a virtualenv criada basta utilizar o comando :

$workon (nome da virtualenv)

Você precisa agora instalar as dependências utilizadas neste projeto:

$ pip install django

$ pip install djangorestframework

$ pip install markdown       # Markdown support for the browsable API.

$ pip install django-filter  # Filtering support

##Agora você deve clonar o repositorio e seguir os comandos abaixo:

$git clone (https://github.com/FabaoUfop/teste-starline-fabio.git)

$ virtualenv --python=`which python3` venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ cd teste-starline-fabio

$ python manage.py migrate

$ python manage.py runserver

## Como inteiragir com o programa:

[Documentação Oficial](http://www.django-rest-framework.org/)
