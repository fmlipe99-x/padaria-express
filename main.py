#terminal de venda de uma padaria

#camel case 

# ID serve para a indentificação dos valores dentro  de um array
produtosDisponiveis = [
    {"id": 1, "nome": 'pao frances (un)', "preco": 0.80}, #0
    {"id": 2, "nome": 'cafe (copo)', "preco": 3.80}, #1
    {"id": 3, "nome": 'pao de queijo (un)', "preco": 4.80}, #2
    {"id": 4, "nome": 'bolo de fuba (fatia)', "preco": 7.80} #3
]

#print(produtosDisponiveis[0])
#print(produtosDisponiveis[1])
#print(produtosDisponiveis[2])
#print(produtosDisponiveis[3])


carrinho = []
totalCompra = 0.0

while True:
    print("\n" + "=" * 40)
    print("    padaria express menu    ")
    print("=" * 40)
    print("[0] - sair")
    print("[1] - ver caradapio" )
    print("[2] - ver carrinho" )
    print("[3] - fechar a conta e finalizar")
    
    opcao = int(input("escolha uma opção"))
    
    if opcao == 0:
        print("saindo do sistema")
        break
    elif opcao == 1:
        print(100 * "==")
        print("produtos disponiveis")
        print(100 * "==")

        for prod in produtosDisponiveis:
            print(f"ID: {prod['id']} | {prod['nome']}: R$ {prod['preco']:.2f}")
            
            
        try:
            id_escolhido = int(input("digite o item que quer adicionar"))


            produto_encontrado = None

            for prod in produtosDisponiveis:
                if prod['id'] == id_escolhido:
                    produto_encontrado = prod #apenas atribui um valor
                    break
            if produto_encontrado:
                qtd = int(input(f"quantas unidades de '{produto_encontrado['nome']}' ? "))
                if qtd > 0:
                    carrinho.append({"produto": produto_encontrado, "quantidade" : qtd}) #.append para add coisas a um array, geralmente usado para add mais de uma coisa num array
                    print(f"{qtd} x {produto_encontrado['nome']} adicionado ao carrinho!")
                else:
                    print("quantidade invalida")
            else:
                print("produto não encontrado")

        except ValueError:
            print("por favor digite numeros validos")
            
    elif opcao == 2:
        print(100 * "==")
        print(" seu carrinho")
        print(100 * "==")

        if not carrinho:
            print("seu carrinho esta vazio, compre itens")
        else:
            subtotal_carrinho = 0

            for item in carrinho:
                nome = item['produto']['nome']
                preco = item['produto']['preco']
                qtd = item['quantidade']
                total_item = preco * qtd
                subtotal_carrinho += total_item
                print(f"subtotal atual: R$ {subtotal_carrinho:.2f}")

    elif opcao == 3:
        if not carrinho:
            print("o seu carrinho esta vazio, faça compras")

        print("=" * 100)
        print("resumo da compra")
        print("=" * 100)

        total_compra = 0

        for item in carrinho:
            nome = item['produto']['nome']
            preco = item['produto']['preco']
            qtd = item['quantidade']
            total_compra = qtd * preco 

            total_compra += total_item
            print(f"{qtd} x {nome} = R$ {total_item:.2f}")

        print("=" * 10)
        print("total a pagar")
        print("=" * 10)
        
        while True:
            pago = float(input("valor pago pelo cliente"))

            if pago >= total_compra:
                
                troco = pago - total_compra
                print(f'pagamento aprovado troco da compra: {troco}')
                break
            else:
                print("valor insuficiente")

                carrinho.clear()

                print("sistema reiniciado para proximo cliente")

                
    else:
        print("opcao invalida")
        continue
