principal = open('resultados.txt', 'r')
partidas = []
placar = []

corinthians = 0
palmeiras = 0
santos = 0
sãopaulo = 0
guarani = 0


for linhas in principal:
    winner = ''
    partida = linhas.strip().split(':')
        
    if (int(partida[1]) == int(partida[3])):
        print('')
    elif(int(partida[1]) > int(partida[3])):
        winner = partida[0]
    else:
        winner = partida[2]


    if winner.lower() == 'corinthians':
        corinthians +=1
    elif winner.lower() == 'palmeiras':
        palmeiras += 1
    elif winner.lower() == 'santos':
        santos += 1
    elif winner.lower() == 'sãopaulo':
        sãopaulo += 1
    elif winner.lower() == 'guarani':
        guarani += 1

print('Corinthians: ', corinthians)
print('Guarani: ', guarani)
print('Palmeiras: ', palmeiras)
print('Santos: ', santos)
print('São Paulo: ', sãopaulo)

principal.close()
