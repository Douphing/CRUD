# Armazenamento dos produtos em memoria como dicionario
{
    "id": int,
    "nome": str,
    "preco": float,
    "quantidade": int
}


# Lista para armazenar produtos
produtos = []
proximo_id = 1

# Cadastrar Produtos
def cadastrar_produto():
    global proximo_id
    
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Digite um nome para o produto!")
        return

    preco = float(input("Preço: ").strip())
    if not preco:
        print("Digite um preco para o produto!")
        return 
    
    quantidade = input("Quantidade: ").strip() 
    if not quantidade:
        print("Digite a quantidade do produto!")
        return
    print("Digite Novamente!")

    
  

    produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    proximo_id += 1
    print("Produto cadastrado com sucesso!")
  

        


# Função para listar todos os produtos
def listar_produto():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R${p['preco']} | Quantidade: {p['quantidade']}")


# Função para atualizar um produto
def atualizar_produto():   
    entrada = input 
    try:
        id_produto = int(input("Digite o ID do produto a ser atualizado: ")) 
        for produto in produtos:
            if produto["id"] == id_produto:
                novo_nome = input("Digite o novo nome: ").strip()
                
                novo_preco = float(entrada("Digite o preço: ").strip())
                nova_quantidade = int(input("Digite a nova quantidade: ").strip())

                if not novo_nome or not novo_preco:
                    print("Digite os campos para atualizar!")
                    return



                produto["nome"] = novo_nome
                produto["preco"] = novo_preco
                produto['quantidade'] = nova_quantidade
                print("Produto atualizado com sucesso!\n")
                return
        print("Produto não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Digite um número.\n")

# Função para deletar um Produto
def deletar_produto():
    try:
        id_produto = int(input("Digite o ID do produto a ser deletado: "))
        for produto in produtos:
            if produto["id"] == id_produto:
                produtos.remove(produto)
                print("Produto removido com sucesso!\n")
                return
        print("Produto não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Digite um número.\n")

# Função principal (menu)


def menu():
    while True:
        print("========= MENU =========")
        print("1 - Criar Produto")
        print("2 - Listar Produto")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa
menu()
