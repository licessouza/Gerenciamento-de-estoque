def mostrar_estoque():      #chamamos esta função caso o usuário desejar excluir, editar ou visualizar o estoque, para conferir os itens presentes.
    if estoque:     #aqui, verificamos se a lista não está vazia
            contador = 1
            for produto in estoque:     #o loop irá iterar sobre a lista para verificar e immprimir cada produto presente no estoque.
                print(f'"{contador}: {produto['nome']}, Preço: R${produto['preco']: .2f}, Quantidade: {produto['quantidade']} item(s).')
                contador += 1
    else:
         print('O estoque está vazio.')

def pausar():   #utilizamos a função pausar() para pausar temporariamente a execução do programa, enquanto o usuário interage.
    input('Pressione ENTER para voltar ao menu principal.')
            
estoque = []    # iniciamos com uma lista vazia como o ESTOQUE zerado.

while True:     #loop WHILE para rodar a exibição do menu
    print('        [[MENU]]       ')
    print("[1] ADICIONAR PRODUTO")
    print("[2] EXCLUIR PRODUTO")
    print("[3] ATUALIZAR PRODUTO")
    print("[4] VISUALIZAR ESTOQUE")
    print("[0] SAIR DO SISTEMA")
    opcao = input("Selecione uma opção: ")     #entrada de dados do usuário

    if opcao == "1":    # ADICIONANDO UM PRODUTO
        produto = {'nome': input('Digite o nome do produto: '),
                        'preco': float(input('Insira o seu preço: ')),
                        'quantidade': int(input('Insira a quantidade: '))}      #cada produto será um dicionário, armazenando as informações solicitadas na entrada do usuário.
        estoque.append(produto)    #dicionário(produto) adicionado ao estoque[]
        print(f'"{produto['nome']}" adicionado ao estoque com {produto['quantidade']} item(s) à R${produto['preco']: .2f} cada.')
        pausar() # retornando para o menu
    

    elif opcao == "2":      # EXCLUINDO PRODUTO
        mostrar_estoque()
        produto_del = (input("Qual produto deseja excluir: "))

        for produto in estoque:     #iteramos sobre a lista com um loop para percorrer cada dicionário(produto) na lista estoque[].
            if produto['nome'] == produto_del:
                estoque.remove(produto)
                print(f'{produto_del} removido com sucesso.')
                break
        else:
            print('Produto não encontrado.')   #mensagem exibida caso o produto não esteja na lista.
        pausar()
    
    elif opcao == "3":      # ATUALIZANDO PRODUTO
        mostrar_estoque()
        produto_edit = input('Qual produto deseja editar? ')

        for produto in estoque:
            if produto['nome'] == produto_edit:
                novo_preco = float(input('Insira o novo valor: '))
                nova_quant = int(input('Insira a nova quantidade: '))

                produto['preco'] = novo_preco
                produto['quantidade'] = nova_quant
                print(f'{produto_edit} atualizado com sucesso. Novos dados: R${novo_preco: .2f}, {nova_quant} item(s)')
                break
        else:
            print('Produto não encontrado.')
        pausar()
         
    elif opcao == "4":     # MOSTRAR ESTOQUE
        mostrar_estoque()
        pausar()

    elif opcao == "0":  # SAIR DO SISTEMA
        print('Encerrando...')
        break
