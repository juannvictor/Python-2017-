#Algoritmo:
# Ler o peso da pessoa, em kg
# Ler a altura da pessoa, em metros
# Calcular o IMC através da formula
# Se o imc der abaixo de 20; mostrar que a pessoa esta abaixo do peso
# Se o imc der um valor entre 20 e 25; mostrar que a pessoa esta normal
# Se o imc der um valor entre 25 e 30; mostrar que a pessoa tem um excesso de peso
# Se o imc der um valor entre 30 e 35; mostrar que a pessoa tem obesidade
# Se o imc der acima de 35; mostrar que a pessoa esta com obesidade mórbida

x = float(input("Digite o seu peso, em kg: "))
y = float(input("Digite a sua altura, em metro: "))
conta = x/(y**2)
if conta<20:
    print("O seu IMC é de ", conta)
    print("Você esta abaixo do peso.")
elif conta>=20 and conta<=25:
    print("O seu IMC é de ", conta)
    print("Você esta com o peso normal.")
elif conta>25 and conta<=30:
    print("O seu IMC é de ", conta)
    print("Você esta com excesso de peso.")
elif conta>30 and conta<=35:
    print("O seu IMC é de ", conta)
    print("Você esta com obesidade.")
elif conta>35:
    print("O seu IMC é de ", conta)
    print("Você esta com obesidade mórbida.")
else:
    print("IMC inválido.")
