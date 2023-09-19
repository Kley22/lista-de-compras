# Inicializa uma lista de compras vazia
lista_de_compras = []

while True:
    print("\n--- Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista de compras")
    print("4. Sair")
    
    escolha = input("Escolha uma opção (1/2/3/4): ")
    
    if escolha == '1':
        item = input("Digite o nome do item a ser adicionado: ")
        lista_de_compras.append(item)
        print(f"{item} foi adicionado à lista de compras.")
    elif escolha == '2':
        if not lista_de_compras:
            print("A lista de compras está vazia.")
        else:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
            numero_item = int(input("Digite o número do item a ser removido: "))
            if 1 <= numero_item <= len(lista_de_compras):
                item_removido = lista_de_compras.pop(numero_item - 1)
                print(f"{item_removido} foi removido da lista de compras.")
            else:
                print("Número de item inválido.")
    elif escolha == '3':
        if not lista_de_compras:
            print("A lista de compras está vazia.")
        else:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
    elif escolha == '4':
        print("Saindo do programa.")
        break
    else:
