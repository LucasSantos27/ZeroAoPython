import requests
import random
from os import system
import time

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

req = requests.get(url)
word = req.content.splitlines()

word = [palavra.decode('utf-8') for palavra in word]


print("""\n\n##########     BEM VINDO AO DIGITANDO EM INGLÊS     ##########\n
    Nesse jogo você receberá uma palavra e deve digitar exatamente igual para pontuar.\n
    Vamos começar!\n""")

n_words = input('Primeiro você deve nos dizer quantas palavras você quer receber: ')

random_word = random.sample(word, int(n_words))

pontos = 0
isready = ''

while isready.lower() != 'começar':
    isready = input('Está preparado? Para começar digite \"COMEÇAR\"\n')
    if isready.lower() == 'começar':
        print('Prepara-se!!! Vai começar em 3 segundos!!\nVocê escolheu', n_words, 'palavras.')
        time.sleep(3)
        system('cls')
    else:
        print('Tudo bem, estamos esperando...\n')
        time.sleep(3)
        system('cls')


start = time.perf_counter()

for palavra in random_word:
    print(palavra)
    entrada = input()
    if entrada == palavra:
        pontos += 1
    system('cls')

end = time.perf_counter()
total_time = round(end - start, 2)

if pontos == int(n_words):
    print('Parabéns você acertou ' + str(pontos) + '/' + n_words + '. Em ' + str(total_time) + ' segundos.')
else:
    print('Continue treinando, você acertou ' + str(pontos) + '/' + n_words + '. Em ' + str(total_time) + ' segundos.')