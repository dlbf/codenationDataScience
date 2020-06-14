from setuptools import setup

setup(
    name="hello",
    version="0.0.1",
    description="Meu novo pacote",
    author="Diego Luiz Bordignon Ferreira",
    email="dbordignon20@gmail.com",
    # programas desenvolvidos
    packages=["hello"],
    #pacotes necessarios para executar os packages
    install_requirements=["numpy"]
    #python setup.py build cria um diretorio com com tudo necessario para executar os programas
    #python setup.py sdist gera um arquivo compactado
    #python setup.py install para instalar o package
)