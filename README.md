# teste-starline-fabio
Teste tecnico para processo seletivo Starline Tecnologia

Teste tecnico para processo seletivo Starline Tecnologia
O projeto será desenvolvido utilizando a linguagem Python 3.6.0 com Django e a biblioteca Django Rest para backend (rest full) utilizando virtualenvwrapper usando gerenciador pip.


Para instalar o virtualenvwrapper/criar o ambiente :

#$ pip install virtualenvwrapper

Configure o arquivo .bashrc :

#$ export WORKON_HOME=~/.virtualenvs
#$ source /usr/local/bin/virtualenvwrapper.sh

Para criar um virtualenvs basta usar o comando :
#$ mkvirtualenv (nome da virtualenv)

Para criar uma virtualenv diferente do seu sistema (default) basta passar o parametro da versao do Python
que serea utilizada:

# mkvirtualenv teste_py3 --python=/usr/local/bin/python3.6.0 (versao utilizada neste teste)

Para acessar a virtualenv criada basta utilizar o comando :

#$workon (nome da virtualenv)

Você precisa agora instalar as dependências utilizadas neste projeto:

#$ pip install django
#$ pip install djangorestframework
#$ pip install markdown       # Markdown support for the browsable API.
#$ pip install django-filter  # Filtering support

Para executar o projeto basta digitar o comando runserver dentro no arquivo manage.py:

#./manage.py runserver

Por padrão ele ira rodar em :
http://127.0.0.1:8000

Links para referencia :

http://www.django-rest-framework.org/


No front end o foi utilizado o Vue.JS framework .

https://vuejs.org/

Executando o projeto.
