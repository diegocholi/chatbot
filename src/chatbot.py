# Contrução do chatbot com deep NLP
import numpy as np  # Lib para processamento matemático/cientifico
import re  # Lib para expressões regulares
import time
import os
import tensorflow

base_cwd = f'''{os.getcwd()}\\DOCS\\base de conhecimento'''


def chatbot():
    import_base()
    linhas, conversas = import_base()
    map_dictionary(linhas, conversas)


# Importação da base
def import_base():
    movie_lines_cwd = f'''{base_cwd}\\movie_lines.txt'''
    movie_conversations_cwd = f'''{base_cwd}\\movie_conversations.txt'''
    linhas = open(movie_lines_cwd, encoding='utf-8', errors='ignore').read().split('\n')
    conversas = open(movie_conversations_cwd, encoding='utf-8', errors='ignore').read().split('\n')
    return linhas, conversas


# Criação de dicionário para mapear cada linha com seu ID
def map_dictionary(linhas, conversas):
    id_para_linha = {}
    for linha in linhas:
        _linha = linha.split(' +++$+++ ')
        if len(_linha) == 5:
            id_para_linha[_linha[0]] = _linha[4]

    print(id_para_linha)
