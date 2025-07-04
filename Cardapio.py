print('Restaurante O Cretino')
massas = ['Spaghetti', 'Raviolli', 'Tortelle', 'Pizza']
frutos_do_mar = ['Lagosta', 'Camarão Frito', 'Marisco Cozido', 'Molusco No Vapor']
guarnicoes = ['Arroz', 'Feijão', 'Molho À Campanha', 'Farofa', ]
comidas = 0
precos = [59.90, 63.50, 66.50, 55.50, 190.60, 60.00, 81.20, 92.40, 15.00, 10.00, 7.00, 5.00]
valor_unitario = 0
conta = 0
fazer = int(input('Digite 1 para abrir o cardápio: '))
if fazer == 1:
    print('----===----===---- 1. Massas ----===----===----')
    while comidas != len(massas):
        print(f'\n{massas[comidas]}')
        print(precos[valor_unitario])
        comidas += 1
        valor_unitario += 1
if comidas == len(massas):
    comidas = 0
    print('\n----===----===---- 2. Frutos do Mar ----===----===----')
    while comidas != len(frutos_do_mar):
        print(f'\n{frutos_do_mar[comidas]}')
        print(precos[valor_unitario])
        comidas += 1
        valor_unitario += 1
if comidas == len(frutos_do_mar):
    comidas = 0
    print('\n----===----===---- 3. Guarnições ----===----===----')
    while comidas != len(guarnicoes):
        print(f'\n{guarnicoes[comidas]}')
        print(precos[valor_unitario])
        comidas += 1
        valor_unitario += 1
if comidas == len(guarnicoes):
    comidas = 0
resposta = str(input('\nDigite o prato desejado,(1x por vez): ')).title()
print(resposta)
if resposta not in massas and resposta not in frutos_do_mar and resposta not in guarnicoes:
    while resposta not in massas and resposta not in frutos_do_mar and resposta not in guarnicoes:
        resposta = str(input('Não entendi bem. digite novamente, por favor: ')).title()
        if resposta in massas or resposta in frutos_do_mar or resposta in guarnicoes:
            break
if resposta in massas or resposta in frutos_do_mar or resposta in guarnicoes:
    if resposta in massas:
        conta += precos[precos.index(59.90) + massas.index(resposta)]
        print(conta)
    if resposta in frutos_do_mar:
        conta += precos[precos.index(190.60) + frutos_do_mar.index(resposta)]
        print(conta)
    if resposta in guarnicoes:
        conta += precos[precos.index(15.00) + guarnicoes.index(resposta)]
        print(conta)
