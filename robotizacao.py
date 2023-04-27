valor = float(input("insira o valor: "))
if valor <= 100:
    limite = input("Está dentro do limite?: ")
    limite = limite.upper()
    if limite == "SIM":
        print("Pressão OK")
    elif limite == "NÃO" or limite == "NAO": # corrigido para verificar a variável limite
        acima = input("Está acima do limite: ") # corrigido "=" em excesso
        acima = acima.upper()
        if acima == "SIM" and valor > 30:
            print("ALERTA: possível estrangulamento")
        elif acima == "NÃO" or acima == "NAO": # corrigido para verificar a variável acima
            if valor < 10:
                print("ALERTA: possível vazamento")
            else:
                print("Pressão OK")
        else:
            print("Valor fora de trabalhabilidade")
    else:
        print("Valor fora de trabalhabilidade")
else:
    print("Valor fora de trabalhabilidade")
