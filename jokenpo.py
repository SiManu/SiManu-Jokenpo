# Faça um programa que jogue Jokenpo com você

from random import choice
from time import sleep

titulo = 'Jokenpô'
print('\033[33m-=-\033[m' * 35, '\n\033[1;31m{:^105}\033[m\n'.format(titulo)+'\033[33m-=-\033[m' * 35)

print ('\033[1;31mEsse é um jogo baseado na sorte, o computador escolherá pedra, papel ou tesoura, o seu objetivo é vencer!\033[m')

print('Escolha o que você jogará: \033[33mPedra, Papel ou Tesoura\033[m')
player = (input('Digite sua opção: '))
escolhas = ['Pedra', 'Papel', 'Tesoura']
pc = choice(escolhas)


sleep(1.5)

print ('Você jogará contra uma IA sem piedade! \033[1;31mQue os jogos comecem\033[m')

print ('Carregando resultados...'), sleep(1.5)


if player == 'Tesoura' and pc == 'Pedra':
    print('PEDRA!')
    print ('\033[1;31mVocê foi amassado por uma pedra. HAHAHAHA\033[m')
elif player == 'Pedra' and pc == 'Tesoura':
    print('TESOURA!')
    sleep(1)
    print ('\033[1;37mEu perdi, parabéns, você ganhou :(\033[m ')
elif player == 'Papel' and pc == 'Pedra':
    print ('PEDRA!')
    sleep(1)
    print ('\033[1;37mEu perdi, parabéns, você ganhou :(\033[m ')
elif player == 'Pedra' and pc == 'Papel':
    print ('PAPEL!')
    sleep(1)
    print ('\033[1;31mSUA PEDRA NÃO SURTE EFEITO NO MEU PAPEL! HHAHAHAHAHA \033[m')
elif player == 'Tesoura' and pc == 'Papel':
    print('PAPEL!')
    sleep(1)
    print('\033[1;37[mEu perdi, parabéns, você ganhou :(\033[m')
elif player == 'Papel' and pc == 'Tesoura':
    print ('TESOURA')
    sleep(1)
    print('\033[1;31mSEU PAPEL FOI RASGADO PELA MINHA TESOURA!\033[m')
elif player == pc:
    print('\033[1;97mNÓS ESCOLHEMOS O MESMO, EMPATE!!\033[m')
elif player != escolhas:
    print('Você não escolheu as opções da lista!', end='')
