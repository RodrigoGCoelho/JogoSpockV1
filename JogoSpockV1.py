# -*- coding: utf-8 -*-

import random
import time

valorHumano = str
valorComputador = str
valorPermitido = ["pedra" , "papel" , "tesoura" , "lagarto" , "spock"]
jogarNovamente = str
simNao = ["sim" , "nao"]
counter = 0

print("NAO USAR ACENTOS OU LETRAS MAIUSCULAS NAS RESPOSTAS")

while counter == 0:
    
    valorHumano = input("Escolha pedra, papel, tesoura, lagarto ou spock!\n")

    while valorHumano not in valorPermitido:
        print("*ERRO* Digite um valor valido!")
        valorHumano = input("Escolha pedra, papel, tesoura, lagarto ou spock!\n")
    
    time.sleep(0.5)    
    
    valorComputador = random.choice(["pedra" , "papel" , "tesoura" , "lagarto" , "spock"])
    print("Eu escolho:")
    print(valorComputador)
    time.sleep(1)    
    
    if valorHumano == valorComputador:
        print("O jogo empatou!")
    
    if valorHumano != valorComputador:
        if valorHumano == "pedra":
            if valorComputador == "lagarto" or valorComputador == "tesoura":
                print("Voce ganhou!")
            else:
                print("Voce perdeu!")
        
        if valorHumano == "papel":
            if valorComputador == "pedra" or valorComputador == "spock":
                print("Voce ganhou!")
            else:
                print("Voce perdeu!")
        
        if valorHumano == "tesoura":
            if valorComputador == "papel" or valorComputador == "lagarto":
                print("Voce ganhou!")
            else:
                print("Voce perdeu!")
        
        if valorHumano == "lagarto":
            if valorComputador == "papel" or valorComputador == "spock":
                print("Voce ganhou!")
            else:
                print("Voce perdeu!")
        
        if valorHumano == "spock":
            if valorComputador == "pedra" or valorComputador == "tesoura":
                print("Voce ganhou!")
            else:
                print("Voce perdeu!")

    time.sleep(1)    
    
    jogarNovamente = input(str("Deseja jogar novamente?\n"))
    
    while jogarNovamente not in simNao:
        print("Digite sim ou nao !!!!")
        jogarNovamente = input(str("Deseja jogar novamente? (sim/nao)\n"))
    if jogarNovamente == "nao":
        counter = counter + 1
        print("Obrigado!")
    else:
        time.sleep(1)
        continue
else:
    exit