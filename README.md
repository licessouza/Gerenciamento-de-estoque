# Sistema de Gerenciamento de Estoque

Este é um sistema simples de gerenciamento de estoque desenvolvido em Python. Ele permite adicionar, excluir, atualizar e visualizar produtos em um estoque. O sistema é baseado em um menu interativo que facilita a navegação e o uso.

## Funcionalidades

- **Adicionar Produto:** Permite adicionar um novo produto ao estoque, incluindo nome, preço e quantidade.
- **Excluir Produto:** Permite excluir um produto existente do estoque.
- **Atualizar Produto:** Permite atualizar as informações de um produto existente, como preço e quantidade.
- **Visualizar Estoque:** Lista todos os produtos no estoque, mostrando suas informações.
- **Sair do Sistema:** Encerra a execução do programa.

## Como Usar

1. Clone este repositório.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Execute o script `estoque.py`.
4. Siga as instruções do menu para interagir com o sistema.

## Estrutura do Código

O código é estruturado da seguinte forma:

- **`estoque`:** Uma lista que armazena os produtos. Cada produto é um dicionário com as chaves 'nome', 'preco' e 'quantidade'.
- **`mostrar_estoque()`:** Função que exibe os produtos no estoque.
- **`pausar()`:** Função que pausa a execução do programa.
- **`while True`:** Loop principal que exibe o menu e processa as opções do usuário.

## Exemplo de Uso

   [[MENU]]

[1] ADICIONAR PRODUTO  
[2] EXCLUIR PRODUTO  
[3] ATUALIZAR PRODUTO  
[4] VISUALIZAR ESTOQUE  
[0] SAIR DO SISTEMA  
Selecione uma opção: 1  
Digite o nome do produto: Caneta  
Insira o seu preço: 1.50  
Insira a quantidade: 10  
"Caneta" adicionado ao estoque com 10 item(s) à R$1.50 cada.  
Pressione ENTER para voltar ao menu principal.

[[MENU]]  
[1] ADICIONAR PRODUTO  
[2] EXCLUIR PRODUTO  
[3] ATUALIZAR PRODUTO  
[4] VISUALIZAR ESTOQUE  
[0] SAIR DO SISTEMA  
Selecione uma opção: 4  
"1: Caneta, Preço: R$ 1.50, Quantidade: 10 item(s).  
Pressione ENTER para voltar ao menu principal. 

## Observações

- O sistema não possui persistência de dados. Isso significa que os dados do estoque são perdidos ao encerrar o programa.
- O sistema é simples e pode ser aprimorado com funcionalidades adicionais, como busca de produtos, ordenação, etc.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
