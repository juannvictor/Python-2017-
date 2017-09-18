import random
import math

#Variáveis do programa
ncasas = 24 #Número de casas no tabuleiro
scinicial = 10000 #Número de Space Coins iniciais
nomejogadores = "" #Nome dos jogadores
statusjogadores = "" #Variável que mostra o estado atual do jogadores (0 = Livre ; 1 = Preso por 1 turno; 2 = Preso por 2 turnos; 3 = Preso por 3 turnos; 4 = Falido)
posicaojogadores = "" #Variável que mostra a posição do jogadores no tabuleiro (de 0 = ponto inicial, até 24 = ultima casa)
spacecoins = "" #Variável que mostra a quantia de Space Coins de cada jogador, formatada com 6 espaços, possibilitanto o jogador conseguir acumular até 999.999$C
casasnome = "" #Variável que mostra o nome de cada casa do tabuleiro.
terrenos = "" #Variável que mostra os respectivos terrenos, com seu id, preço e aluguel, formatado em "(00)ID,(000)Preço,(000)Aluguel"
#ID's = 00 = Sem proprietário / 06 = Ponto de Partida / 01~05 = Reservado a jogadores / 07 = Imposto / 08 = Vá para prisão / 09 = Prisão / 10 = Jackpot

#Atribuição das casas
casasnome = ("Fronteira Intergaláctica/Portões do Universo."+
             "Base Interplanetária de Vênus."+
             "Base Interplanetária da Terra."+
             "Base Interplanetária de Marte."+
             "Base Interplanetária de Júpiter."+
             "Base Interplanetária de Saturno."+
             "Prisão Universal/Passagem de Visitantes."+
             "Base Lunar da Terra."+
             "Base Lunar de Fobos."+
             "Base Lunar Europa."+
             "Base Lunar de Pandora."+
             "Base Lunar de Talassa."+
             "Satélite da sorte:JACKPOT"+
             "Planeta anão: Plutão"+
             "Planeta anão: Éris"+
             "Planeta anão: Haumea"+
             "Planeta anão: Ceres"+
             "Planeta anão: Makemake"+
             "Vá para prisão universal!"+
             "Base extra-solar Gliese 581 d"+
             "Base extra-solar Upsilon Andromedae"+
             "Base extra-solar XO-3b"+
             "Base extra-solar COROT-Exo-1b"+
             "Imposto espacial"+
)
terrenos = ("06000000"+
            "00250025"+
            "00600060"+
            "00450045"+
            "00450045"+
            "00250025"+
            "09000000"+
            "00600060"+
            "00250025"+
            "00450045"+
            "00450045"+
            "00250025"+
            "10000000"+
            "00250025"+
            "00450045"+
            "00250025"+
            "00450045"+
            "00600060"+
            "08000000"+
            "00250025"+
            "00450045"+
            "00600060"+
            "00250025"+
            "07000000"+
)



#Código
numjogadores = 0
while numjogadores > 2 and numjogadores < 5:
    numjogadores = int(input("Digite o número de jogadores(De 2 a 5 jogadores): "))
for i in range(0, numjogadores):
    Nome = ""
    Nome = str(input("Digite o nome do",(i + 1),"º jogador: "))
    print("O nome do",(i+1),"º jogador será",Nome,".")
    numjogadores += Nome
    statusjogadores += "0"
    posicaojogadores += "00"
    spacecoins += "0" + str(scinicial)
    Nome = None
gameover = False
while not gameover:
    for i in range(0,numjogadores):
        if statusjogadores[i] != "4":
            print(Nome,", é a sua vez.")
            if statusjogadores[i] == "0":
                posicao = int(posicaojogadores[(i*2):((i*2)+2)])
                sc = int(spacecoins[(i*6):((i*6)+6)])
                mov = "."
                while mov != "":
                    print("Digite 1 para saber sua posição.")
                    print("Digite 2 para saber sua quantia de dinheiro.")
                    print("Digite 3 para ver suas propriedades.")
                    print("Pressione [ENTER] para jogar os dados.")
                    mov = input()
                    if mov == "1":
                        print(Nome,", você se encontra na", str(posicao),"º do tabuleiro.")
                        print()
                    elif mov == "2":
                        print(Nome,", você ainda tem $C",str(sc))
                        print()
                    elif mov == "3":
                        cont = ""
                        for i2 in range(0,175,7):
                            if terrenos[i2:i2+2] == "0" + str(i + 1):
                                cont += casasnome[((i2//7)*20):(((i2//7)+1)*20)] + "\r\n"
                            if cont != "":
                                print(Nome,", você tem esses terrenos:")
                                print(cont)
                            elif:
                                print(Nome,", você não tem terrenos no momento.")
                                print()
                d6 = random.randint(1,6)
                print("Você rodou",d6,"no primeiro dado.")
                posicao += d6
                d62 = random.randint(1,6)
                print("Você rodou",d62,"no segundo dado.")
                posicao += d62
                if posicao > ncasas - 1:
                    posicao -= ncasas #24 = ultima casa. Se der 26 significa que ele voltou para a casa 0
                    sc += 200
                    print("Você atravessou os Portões do Universo e chegou na Fronteira Intergaláctica e recebeu $C200 para pagar a gasolina da espaçonave, totalizando $C",str(sc))
                terrenoatual = ncasas[posicao*20:(posicao+1)*20]
                print("Você se encontra no terreno:",terrenoatual)
                terrenoatual = terrenos[posicao*7: (posicao+1)*7]
                idterreno = terrenoatual[0:2]
                if idterreno == "00": #que não pertence a ninguém
                    valorterreno = int(terrenoatual[2:5])
                    print("Este satélite remoto esta inabitável e seu valor é de $C",str(valorterreno),".")
                    if sc>valorterreno:
                        print("Deseja comprar esse satélite? (S ou N)")
                        if input().upper() == "S":
                            sc -= valorterreno
                            print("Parabéns! Você acaba de adiquirir um novo satélite para colonizar!")
                            terrenos = terrenos[0:posicao * 7] + "0" + str(i+1) + terrenos[(posicao * 7 )+2:]
                        else:
                            print("Infelizmente você não possui Space Coins suficientes para adquirir esse satélite! ):")
                    elif 0 < int(idterreno) < 6: #o terreno pertence a alguém
                        aluguel = int(terrenoatual[5:8])
                        idterreno = int(idterreno) - 1
                        if idterreno != 1:
                            scdono = int(spacecoins[(idterreno * 5):((idterreno + 1)*5)])
                            print("Este satélite ja tem dono e você tera que pagar $C",str(aluguel),"de aluguel a",nomejogadores[(idterreno*50):((idterreno + 1)*50)])
                        sc -= aluguel
                        scdono += aluguel
                    elif idterreno == "07": #imposto espacial
                        sc = sc *0.9
                        print("Como taxa de impostos espaciais, você deverá pagar 10% do seu dinheiro ao governo intergaláctico, te deixando com $C",str(sc))
                    elif idterreno == "10": #jackpot
                        print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                        print("O jogo se resume em digitar um número e rodar um único dado, se o número digitado for igual ao número do dado, você ganhará $S200, caso contrário, perderá $S100")
                        num = int(input("Digite um número de 1 a 6: "))
                        print("Número escolhido:",num)
                        dado = random.randint(1,6)
                        print("O dado caiu na posição número",dado)
                        if num == dado:
                            print("Parabéns! Você acaba de ganhar $C200.")
                            sc = sc + 200
                        else:
                            print("Você perdeu $C100.")
                            sc = sc - 100
                    elif idterreno == "08": #va para a prisão
                        print("Você foi pego ultrapassando os limites de velocidades espaciais e foi preso. Você ficará preso por até 3 rodadas se não tirar dois números iguais nos dados. Se você não conseguir, deverá pagar $C50 e será solto na 4ª rodada.")
                        statusjogadores = statusjogadores [0:1] + "3" + statusjogadores[i+1]
                        posicao=10
                    elif idterreno == "09":
                        print("Você esta passando pela prisão, mas apenas como visitante...")
                else: #Jogador preso






