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

<<<<<<< HEAD
+$ pip install django

+$ pip install djangorestframework

+$ pip install markdown       # Markdown support for the browsable API.

+$ pip install django-filter  # Filtering support
=======
$ pip install django

$ pip install djangorestframework

$ pip install markdown       # Markdown support for the browsable API.

$ pip install django-filter  # Filtering support
>>>>>>> de32e126607f61105e4c740ab5143879d5ea0554

Agora você deve clonar o repositorio e seguir os comandos abaixo:

$git clone (https://github.com/FabaoUfop/teste-starline-fabio.git)

$ virtualenv --python=`which python3` venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ cd teste-starline-fabio

$ python manage.py migrate

$ python manage.py runserver

<<<<<<< HEAD
=======
## Como inteiragir com o programa:
>>>>>>> de32e126607f61105e4c740ab5143879d5ea0554

Por padrão ele ira rodar em :

(http://127.0.0.1:8000)

Nesta páǵina será exibido uma lista de questoes por usuario e o tipo de questão (Objetiva ou Discursiva)

Como foi adotado o django-admin , para realizar operações CRUD para questoes basta acessar:

(http://127.0.0.1:8000/admin) (interface base)

ou

(http://127.0.0.1:8000/app) (interface rest)

Links para referencia :

[Documentação Oficial](http://www.django-rest-framework.org/)
