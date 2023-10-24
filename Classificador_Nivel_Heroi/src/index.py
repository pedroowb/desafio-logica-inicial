import os

print('Bem-vindo, Aventureiro..')
def musicPlayer():
    os.startfile(r'C:\Users\1039856\Documents\Dio Projects\Desafio #1\add\SnapInsta.io - One last shot - Dragon Quest the adventure of Dai 2020 anime OST - Sortie with strong determination (128 kbps).mp3')
def playerInfo():
    global nome
    nome = input('Qual seu nome, oh bravo aventureiro!: ')    
def nivelAventureiro():
    global ranking, xp
    xp = int(input('Estou conseguindo ler.. sim.. através da clarividência eu consigo identificar.. (digite sua quantidade de XP): '))
    if xp < 1000:
        xp = 'Ferro'
    elif 1001 <= xp <= 2000:
        xp = 'Bronze'
    elif 2001 <= xp <= 5000:
        xp = 'Prata'
    elif 6001 <= xp <= 7000:
        xp = 'Ouro'
    elif 7001 <= xp <= 8000:
        xp = 'Platina'
    elif 8001 <= xp <= 9000:
        xp = 'Ascendente'
    elif 9001 <= xp <= 10000:
        xp = 'Imortal'
    elif xp >= 10001:
        xp = 'Radiante'
    ranking = xp
    print(f'Ah certo.. sim, você se chama "{nome}", e seu nível como aventureiro é equivalente a um Cavaleiro de {ranking},\nBem-vindo, a este mundo de aventuras!')
  
musicPlayer()  
while True:
    playerInfo()
    nivelAventureiro()