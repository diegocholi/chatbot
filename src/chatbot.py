# Contrução do chatbot com deep NLP
import numpy as np  # Lib para processamento matemático/cientifico
import re  # Lib para expressões regulares
import time
import os
import tensorflow

base_cwd = f'''{os.getcwd()}\\DOCS\\base de conhecimento'''


def chatbot():
    # Recuperando bases RAW
    conversations, conversations_id = import_base()
    # Tratamento inicial das bases
    conversations = map_conversations(conversations)
    conversations_id = map_conversations_id(conversations_id)
    # Recuperando perguntas e respostas no modelo de aprendizagem assistida
    questions, answers = questions_and_answers(conversations, conversations_id)
    # Contagem de palavras
    count_words = {}
    count_words = remove_little_used_words(count_words, questions)
    count_words = remove_little_used_words(count_words, answers)
    print(count_words)


# 1. Importação da base
def import_base():
    movie_lines_cwd = f'''{base_cwd}\\movie_lines.txt'''
    movie_conversations_cwd = f'''{base_cwd}\\movie_conversations.txt'''
    conversations = open(movie_lines_cwd, encoding='utf-8', errors='ignore').read().split('\n')
    conversations_id = open(movie_conversations_cwd, encoding='utf-8', errors='ignore').read().split('\n')
    return conversations, conversations_id


# 2. Criação de dicionário para mapear cada linha da conversa com seu ID
# Colocamos os IDs das conversas e as conversas em um dicionário
# EX:
# {
#   L1045: They do not!,
#   ...
# }
def map_conversations(conversas):
    map_conversations = {}
    for linha in conversas:
        _linha = linha.split(' +++$+++ ')
        if len(_linha) == 5:
            map_conversations[_linha[0]] = _linha[4]

    return map_conversations


# 3. Criação de um dicionário com os ids das conversas completas
# Colocamos os IDs que repersentam uma conversa completa dentro de um Lista
# [
#   ['L194', 'L195', 'L196', 'L197'],
#   ['L200', 'L201', 'L202', 'L203']
#   ...
# ]
def map_conversations_id(conversations_id):
    map_conversations_id = []
    for conversa in conversations_id[:-1]:  # [:-1]  Excluir o último registro
        if conversa:
            # [-1] --> Traz somente o último registro da lista
            # [1:-1] --> Excluir o primeiro e o último item
            _conversa = conversa.split(' +++$+++ ')[-1][1:-1].replace('\'', '').replace(' ', '')
            map_conversations_id.append(_conversa.split(','))
    return map_conversations_id


# 4. Separação das perguntas e das respostas
# Perguntas         |       Respostas       |
# ------------------|-----------------------|
# Olá[L194]         |       Tudo bem?[L195] |
# Tudo bem?[L195]   |       Tudo[L196]      |
# Tudo[L196]        |       Eu também[L197] |
# ------------------|-----------------------|
def questions_and_answers(conversations, conversations_id):
    questions = []
    answers = []
    for conversation_id in conversations_id:  # Iteramos cada grupo de conversas IDs
        for i in range(len(conversation_id) - 1):  # Ireramos esse grupo para recuperação dos seus respectivos ids
            questions.append(text_clear(conversations[conversation_id[i]]))  # Pegunta é o ID corrente
            answers.append(text_clear(conversations[conversation_id[i + 1]]))  # A resposta é o ID corrente + 1

    return questions, answers


def text_clear(texto: str):
    texto = texto.lower()
    texto = re.sub(r"i'm", "i am", texto)
    texto = re.sub(r"he's", "he is", texto)
    texto = re.sub(r"she's", "she is", texto)
    texto = re.sub(r"that's", "that is", texto)
    texto = re.sub(r"what's", "what is", texto)
    texto = re.sub(r"where's", "where is", texto)
    texto = re.sub(r"\'ll", "will", texto)
    texto = re.sub(r"\'ve", "heve", texto)
    texto = re.sub(r"\'re", "are", texto)
    texto = re.sub(r"\'d", "would", texto)
    texto = re.sub(r"won't", "will not", texto)
    texto = re.sub(r"can't", "cannot", texto)
    texto = re.sub(r"[-()#/@;:<>{}~+=?.|,]", "", texto)
    return texto


# Criação de um dicionário que mapeia cada palavra e o número de ocrrências e remove as menos usadas
def remove_little_used_words(count_words, sentences):
    for sentence in sentences:  # Percorremos as frases do obj
        for word in sentence.split():  # splitamos a frases em palavras
            if word not in count_words:  # Se a palavra não existir no dicionário a adicionamos com o contator em 1
                count_words[word] = 1
            else:
                count_words[word] += 1  # Se não incrementamos o contados
    return count_words
