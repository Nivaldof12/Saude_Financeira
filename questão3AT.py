#Entrada
moradia = float(input("Informe quanto gasta com moradia: "))
educacao = float(input("Informe quanto gasta com educação: "))
transporte = float(input("Informe quanto gasta com transporte: "))
valor_total = moradia + educacao + transporte
percentual_moradia = (moradia / valor_total)* 100
percentual_educacao = (educacao / valor_total)* 100
percentual_transporte = (transporte / valor_total)* 100
#Saída
print("O valor total gasto por mês é:R$ {:.2f}".format(valor_total))
print("O valor gasto por mês em moradia é:R$ {:.2f}".format(moradia))
print("O valor gasto por mês em educação é:R$ {:.2f}".format(educacao))
print("O valor gasto por mês em transporte é:R$ {:.2f}".format(transporte))

if percentual_moradia >= 30:
    print("Seus gastos totais com moradia comprometem {:.2f}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${}".format(percentual_moradia , (valor_total *30) /100))
elif percentual_moradia <= 31:
    print("Seus gastos totais com moradia comprometem {:.2f}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.".format(percentual_moradia))
if percentual_educacao >= 20:
    print("Seus gastos totais com educação comprometem {:.2f}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {}".format(percentual_educacao ,(valor_total *20) /100 ))
elif percentual_educacao <= 21:
    print("Seus gastos totais com educação comprometem {:.2f}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.".format(percentual_educacao))
if percentual_transporte >= 15:
    print("Seus gastos totais com transporte comprometem {:.2f}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {}".format(percentual_transporte , (valor_total *15) /100 ))
elif percentual_transporte <= 16:
    print("Seus gastos totais com transporte comprometem {:.2f}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.".format(percentual_transporte))

