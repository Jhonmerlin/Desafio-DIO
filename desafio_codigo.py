#Desafio do felipão. Medidor de experiência do herói

elos = ["Ferro","Bronze","Prata","Ouro","Platina","Ascendente","Imortal","Radiante"]

nome_heroi = str(input("Bem vindo Aventureiro(a)!, Qual seu nome?\n"))
xp_heroi = int(input("Qual seu nível de experiência atual?"))

if xp_heroi <= 1000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[0]}')

elif xp_heroi >=1001 and xp_heroi <= 2000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[1]}')

elif xp_heroi >=2001 and xp_heroi <= 5000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[2]}')

elif xp_heroi >=5001 and xp_heroi <= 7000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[3]}')

elif xp_heroi >=7001 and xp_heroi <= 8000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[4]}')    

elif xp_heroi >=8001 and xp_heroi <= 9000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[5]}')    

elif xp_heroi >=9001 and xp_heroi <= 10000:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[6]}')

elif xp_heroi >=10001:
    print(f'O Herói de nome {nome_heroi} está no nível {elos[7]}')