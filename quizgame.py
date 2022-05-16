import json
import os
import random
 
#Dicionário com perguntas de 1 até 15. A perguntas de 1 á 5 são categorizadas como fáceis, as de 6 á 10 médias e as de 11 á 15 são difíceis.
quizes= {
    1 : {
        'pergunta' : 'Qual o nome das personagens principais da série ?',
        'respostas': {
        'A' : 'Lorelai e Rory',
        'B' : 'Penny e Amy',
        'C' : 'Rachel e Monica',
        },
        'resposta_certa' : 'A',
    },
    2 : {
        'pergunta' : 'Qual o nome do restaurante/café mais famoso da cidade ?',
        'respostas': {
        'A' : "Ranold's",
        'B' : "Luke's",
        'C' : "Jonh's",
        },
        'resposta_certa' : 'B',
    },
    3 : {
        'pergunta' : 'Em que cidade se passa a trama ?',
        'respostas' : {
        'A' : 'Rosewood',
        'B' : 'Stars Hollow',
        'C' : 'Hamilton',
        },
        'resposta_certa' : 'B',
    },
    4 : {
        'pergunta' : 'Quem é o primeiro namorado de Rory ?',
        'respostas' : {
        'A' : 'Jess',
        'B' : 'Logan',
        'C' : 'Dean',
        },
        'resposta_certa' : 'C',
    },
    5 : {
        "pergunta" : 'Quem é a sua melhor amiga ?',
        'respostas' : {
        'A' : 'Lane',
        'B' : 'Sookie',
        'C' : 'Paris',
        },
        'resposta_certa' : 'A',
    },
    6 : {
        'pergunta' : 'Em que ano Rory nasceu ?',
        'respostas': {
        'A' : '1984',
        'B' : '1985',
        'C' : '1986',
        },
        'resposta_certa' : 'A',
    },
    7 : {
        'pergunta' : 'Para qual universidade Rory decide ir ?',
        'respostas': {
        'A' : 'Stanford',
        'B' : 'Havard',
        'C' : 'Yale',
        },
        'resposta_certa' : 'C',
    },
    8 : {
        'pergunta' : 'Quantas temporadas tem a série ?',
        'respostas': {
        'A' : '6',
        'B' : '7',
        'C' : '5',
        },
        'resposta_certa' : 'B',
    },
    9 : {
        'pergunta' : 'Qual era o sonho de Lorelai ?',
        'respostas': {
        'A' : 'Ter uma fazenda',
        'B' : 'Ter um hotel',
        'C' : 'Ter uma empresa',
        },
        'resposta_certa' : 'B',
    },
    10 : {
        'pergunta' : 'Qual ator de Gilmore Girls já faleceu ?',
        'respostas': {
        'A' : 'Edward Herrmann',
        'B' : 'Sean Gunn',
        'C' : 'Scott Patterson',
        },
        'resposta_certa' : 'A',
    },  
    11 : {
        'pergunta' : 'Jess escreveu um livro. Qual o título ?',
        'respostas' : {
        'A' : 'The Suspense',
        'B' : 'The Subject',
        'C' : 'The Subsect',
        },
        'resposta_certa' : 'C',
    },
     12 : {
        'pergunta' : 'Onde o episódio piloto da série foi filmado ?',
        'respostas' : {
        'A' : 'Hartford, Connecticuit',
        'B' : 'Toronto, Canadá',
        'C' : 'Burbank, Califórnia',
        },
        'resposta_certa' : 'A',
    },
     13 : {
        'pergunta' : 'Qual slogan ilustra o pôster da Hep Alien ?',
        'respostas' : {
        'A' : 'We are out of this world!',
        'B' : 'We are out there!',
        'C' : 'Humans are not real!',
         },
        'resposta_certa' : 'C',
    },
    14 : {
        'pergunta' : 'Rory adorava participar de atividades extracurriculares em Chilton. Ela gostava muito de :',
      'respostas' : {
        'A' : 'Nadar',
        'B' : 'Debates',
        'C' : 'Clubes do Livro',
    },
        'resposta_certa' : 'B',
    },
    15 : {
        'pergunta' : 'Lorelai teve diversos companheiros na série. Alguns deles são :',
      'respostas': {
        'A' :  'Luke, Max e Christopher',
        'B' : 'Kirk, Luke e Dennis',
        'C' : 'Max, Christopher e Kirk',
      },
        'resposta_certa': 'A',
    },
}
 
#Criação de dicionários para serem utilizados posteriormente na manipulação de arquivos 
dict_pontuacoes = {}
#Criação de listas para armazenar nomes e pontuações dos jogadores, usarei na formação do ranking
jogadores = []
scores = []
 
def linha():
  print('---------------------------------------------')
 
#Introdução 
def intro():
  linha()    
  print("Bem vindos ao nosso quiz sobre Gilmore Girls!")
  linha()  
 
#Menu principal de apresentação do jogo
def menu():
  print('''
        As perguntas serão divididas em três níveis:
       
        1º 5 perguntas fáceis
        2º 5 perguntas médias
        3º 5 perguntas difíceis
 
        Serão apresentadas 5 perguntas misturadas no jogo.
      obs: há qualquer momento você pode sair da partida digitando a palavra "sair"
        ''')
  opcao = str(input('Digite "Ok" para continuar: '))  
  linha()
  if opcao.lower() == 'ok':
    quiz()
  else:
    while opcao.lower() != 'ok':
      print('Opção inválida')
      opcao = str(input('Digite "Ok" para continuar: '))
      linha()
    quiz()
 
#Ranking de pontuações para apresentar o jogador que teve a maior pontuação do jogo, imprime o nome a pontuação
def ranking():
  maior_pont = -1
  for (i,num) in enumerate(scores):
    if (num > maior_pont and num!=-1):
      indice_maior_pont = i
      maior_pont = num
  print('Ranking:')
  print('Maior Pontuação:', jogadores[indice_maior_pont], scores[indice_maior_pont], 'pontos')
  linha()  

#Função que imprime as perguntas e conta pontuações 
def quiz():
  nome = str(input('Digite o nome do jogador: '))
  if (nome != ''):
    jogadores.append(nome)
  else:
    while (nome == ''):
      nome = str(input('\nDigite o nome do jogador: '))
  linha()

  score = 0
  perguntas = []
  cont = 0
  while (cont < 5):
#Imprime 5 perguntas aleatórias do dicionário
    numero_pergunta = random.randrange(1,15)
    if not numero_pergunta in perguntas:
      perguntas.append(numero_pergunta)
      cont = cont + 1

  quizes[numero_pergunta]
  for num in perguntas : 
    pergunta = quizes[num]
    print('Questão-',pergunta["pergunta"])
    respostas = pergunta["respostas"]
    for alternativa in respostas.keys():
      print(f'{alternativa}: {respostas[alternativa]}') 
#Usuário responde e se acertar pontua, se errar não pontua e apresenta lista de nome dos jogadores junto com a maior pontuação
    resposta_usuario = input('\nDigite aqui: ')
    if resposta_usuario.upper() == pergunta['resposta_certa']:
        linha()
        print('Muito bem!')
        score +=1
        print('Sua pontuação é', score)
        linha()
        #Salvar nome do jogador e pontos no arquivo
        dict_pontuacoes[nome] = score
        salvar_pontuacoes()
    elif resposta_usuario.lower() == 'sair' :
      linha()
      print('''Obrigada por participar do nosso joguinho''')
      print('Sua pontuação foi de:', score, 'pontos!' )
      linha()
      menu()
    else:
      linha()
      print('Resposta errada')
      print('Sua pontuação é', score)
      linha()

  total = score
  scores.append(total)
  print('Jogadores:')
  print('\n'.join(map(str, jogadores)))
  linha()
  ranking()
  menu()
 
#Criar e armazenar todas as perguntas e respostas do dicionário no arquivo
def dicionario_arquivo():
  open('dicionario.txt','w').write(json.dumps(quizes))
 
#Criação de arquivo para salvar as pontuações dos jogadores 
def carregar_arquivos():
  if not os.path.exists('pontuacao.txt'):
    open('pontuacao.txt', 'x')
  else:
    with open('pontuacao.txt') as f:
      file_content = f.read()
      if(not file_content == ""):
        dict_pontuacoes.update(json.loads(file_content))

#Armazenar pontuações e nomes dos jogadores no arquivo
def salvar_pontuacoes():
  with open('pontuacao.txt', 'w') as convert_file:
    convert_file.write(json.dumps(dict_pontuacoes))
 
dicionario_arquivo()
carregar_arquivos()
intro()
menu()